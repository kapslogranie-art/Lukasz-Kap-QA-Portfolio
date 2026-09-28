/* =====================================================================
   SQL dla testera — weryfikacja danych sklepu internetowego
   Dialekt: Microsoft SQL Server (T-SQL) — zgodnie ze stackiem z oferty.
   Autor: Łukasz Kap

   Scenariusz: po złożeniu zamówienia w UI (TC-022) sprawdzam, czy dane
   w bazie są kompletne i spójne. Skrypt tworzy przykładowe tabele z danymi,
   więc można go uruchomić na dowolnej instancji SQL Server
   (np. SQL Server Express / Docker / dbfiddle.uk).
   ===================================================================== */

-- ---------------------------------------------------------------------
-- 0. Przykładowa struktura i dane
-- ---------------------------------------------------------------------
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id  INT IDENTITY(1,1) PRIMARY KEY,
    username     NVARCHAR(50)  NOT NULL UNIQUE,
    first_name   NVARCHAR(100) NOT NULL,
    last_name    NVARCHAR(100) NOT NULL,
    postal_code  NVARCHAR(10)  NULL,
    is_locked    BIT           NOT NULL DEFAULT 0,
    created_at   DATETIME2     NOT NULL DEFAULT SYSDATETIME()
);

CREATE TABLE products (
    product_id   INT IDENTITY(1,1) PRIMARY KEY,
    name         NVARCHAR(100) NOT NULL,
    price        DECIMAL(10,2) NOT NULL CHECK (price >= 0)
);

CREATE TABLE orders (
    order_id     INT IDENTITY(1,1) PRIMARY KEY,
    customer_id  INT NOT NULL REFERENCES customers(customer_id),
    status       NVARCHAR(20)  NOT NULL,          -- NEW, PAID, CANCELLED
    item_total   DECIMAL(10,2) NOT NULL,
    tax          DECIMAL(10,2) NOT NULL,
    total        DECIMAL(10,2) NOT NULL,
    created_at   DATETIME2     NOT NULL DEFAULT SYSDATETIME()
);

CREATE TABLE order_items (
    order_item_id INT IDENTITY(1,1) PRIMARY KEY,
    order_id      INT NOT NULL REFERENCES orders(order_id),
    product_id    INT NOT NULL REFERENCES products(product_id),
    quantity      INT NOT NULL CHECK (quantity > 0),
    unit_price    DECIMAL(10,2) NOT NULL
);

INSERT INTO customers (username, first_name, last_name, postal_code, is_locked) VALUES
 (N'standard_user',   N'Jan',    N'Kowalski', N'50-051', 0),
 (N'locked_out_user', N'Anna',   N'Nowak',    N'00-001', 1),
 (N'problem_user',    N'Piotr',  N'',         NULL,      0),   -- dane niekompletne (por. BUG-003)
 (N'visual_user',     N'Ewa',    N'Zielińska',N'31-000', 0);

INSERT INTO products (name, price) VALUES
 (N'Sauce Labs Backpack', 29.99), (N'Sauce Labs Bike Light', 9.99),
 (N'Sauce Labs Bolt T-Shirt', 15.99), (N'Sauce Labs Fleece Jacket', 49.99),
 (N'Sauce Labs Onesie', 7.99), (N'Test.allTheThings() T-Shirt (Red)', 15.99);

INSERT INTO orders (customer_id, status, item_total, tax, total) VALUES
 (1, N'PAID', 39.98,  3.20,  43.18),   -- poprawne (TC-022)
 (1, N'PAID',  0.00,  0.00,   0.00),   -- zamówienie bez pozycji (por. BUG-005)
 (4, N'NEW',  49.99,  4.00,  53.00);   -- błędna suma (49.99 + 4.00 = 53.99)

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
 (1, 1, 1, 29.99), (1, 2, 1, 9.99),
 (3, 4, 1, 49.99);

-- ---------------------------------------------------------------------
-- 1. Czy zamówienie z testu TC-022 zapisało się poprawnie?
-- ---------------------------------------------------------------------
SELECT TOP (1) o.order_id, c.username, o.status, o.item_total, o.tax, o.total, o.created_at
FROM orders AS o
JOIN customers AS c ON c.customer_id = o.customer_id
WHERE c.username = N'standard_user'
ORDER BY o.created_at DESC, o.order_id DESC;

-- ---------------------------------------------------------------------
-- 2. Pozycje zamówienia z nazwami produktów (JOIN)
-- ---------------------------------------------------------------------
SELECT o.order_id, p.name, oi.quantity, oi.unit_price,
       oi.quantity * oi.unit_price AS line_total
FROM order_items AS oi
JOIN orders   AS o ON o.order_id  = oi.order_id
JOIN products AS p ON p.product_id = oi.product_id
WHERE o.order_id = 1;

-- ---------------------------------------------------------------------
-- 3. Spójność: czy item_total = suma pozycji? (GROUP BY + HAVING)
--    Wynik powinien być PUSTY. Każdy wiersz = potencjalny defekt.
-- ---------------------------------------------------------------------
SELECT o.order_id, o.item_total,
       SUM(oi.quantity * oi.unit_price) AS calculated_total
FROM orders AS o
JOIN order_items AS oi ON oi.order_id = o.order_id
GROUP BY o.order_id, o.item_total
HAVING o.item_total <> SUM(oi.quantity * oi.unit_price);

-- ---------------------------------------------------------------------
-- 4. Spójność: czy total = item_total + tax? (oczekiwany wynik: pusty)
-- ---------------------------------------------------------------------
SELECT order_id, item_total, tax, total, item_total + tax AS expected_total
FROM orders
WHERE total <> item_total + tax;

-- ---------------------------------------------------------------------
-- 5. Czy podatek to 8% zaokrąglone do 2 miejsc? (oczekiwany wynik: pusty)
-- ---------------------------------------------------------------------
SELECT order_id, item_total, tax, ROUND(item_total * 0.08, 2) AS expected_tax
FROM orders
WHERE tax <> ROUND(item_total * 0.08, 2);

-- ---------------------------------------------------------------------
-- 6. Zamówienia bez żadnej pozycji (LEFT JOIN + IS NULL) — por. BUG-005
-- ---------------------------------------------------------------------
SELECT o.order_id, o.customer_id, o.total
FROM orders AS o
LEFT JOIN order_items AS oi ON oi.order_id = o.order_id
WHERE oi.order_item_id IS NULL;

-- ---------------------------------------------------------------------
-- 7. Klienci z niekompletnymi danymi (NULL lub pusty string)
-- ---------------------------------------------------------------------
SELECT customer_id, username, first_name, last_name, postal_code
FROM customers
WHERE NULLIF(LTRIM(RTRIM(last_name)), N'') IS NULL
   OR postal_code IS NULL;

-- ---------------------------------------------------------------------
-- 8. Zablokowany użytkownik nie powinien mieć zamówień (oczekiwany wynik: pusty)
-- ---------------------------------------------------------------------
SELECT c.username, COUNT(o.order_id) AS orders_count
FROM customers AS c
JOIN orders AS o ON o.customer_id = c.customer_id
WHERE c.is_locked = 1
GROUP BY c.username;

-- ---------------------------------------------------------------------
-- 9. Statystyka: liczba zamówień i przychód per klient
-- ---------------------------------------------------------------------
SELECT c.username,
       COUNT(o.order_id)          AS orders_count,
       COALESCE(SUM(o.total), 0)  AS revenue
FROM customers AS c
LEFT JOIN orders AS o ON o.customer_id = c.customer_id AND o.status <> N'CANCELLED'
GROUP BY c.username
ORDER BY revenue DESC;

-- ---------------------------------------------------------------------
-- 10. Duplikaty loginów bez rozróżniania wielkości liter (por. TC-005)
-- ---------------------------------------------------------------------
SELECT LOWER(username) AS username_normalized, COUNT(*) AS cnt
FROM customers
GROUP BY LOWER(username)
HAVING COUNT(*) > 1;

-- ---------------------------------------------------------------------
-- 11. Produkty, które nigdy nie zostały sprzedane (NOT EXISTS)
-- ---------------------------------------------------------------------
SELECT p.product_id, p.name
FROM products AS p
WHERE NOT EXISTS (SELECT 1 FROM order_items AS oi WHERE oi.product_id = p.product_id);

-- ---------------------------------------------------------------------
-- 12. Przygotowanie danych testowych w transakcji (bez śmiecenia w bazie)
-- ---------------------------------------------------------------------
BEGIN TRANSACTION;
    UPDATE customers SET is_locked = 1 WHERE username = N'visual_user';
    SELECT username, is_locked FROM customers WHERE username = N'visual_user';
ROLLBACK TRANSACTION;   -- przywrócenie stanu sprzed testu
