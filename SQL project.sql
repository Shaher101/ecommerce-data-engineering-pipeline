
CREATE DATABASE EcommerceDW;
GO


SELECT
    name AS database_name,
    state_desc AS database_status
FROM sys.databases
WHERE name = 'EcommerceDW';

--  Build Schema for EcommerceDW

USE EcommerceDW;
GO

CREATE SCHEMA raw;
GO

CREATE SCHEMA staging;
GO

CREATE SCHEMA warehouse;
GO

CREATE SCHEMA mart;
GO

--Sure 4 Schemas have been created successfully.


SELECT
    name AS schema_name
FROM sys.schemas
WHERE name IN ('raw', 'staging', 'warehouse', 'mart')
ORDER BY name;

--Build Tables for EcommerceDW in raw schema.


USE EcommerceDW;
GO

CREATE TABLE raw.Customers (
    customer_id INT,
    full_name NVARCHAR(100),
    email NVARCHAR(255),
    city NVARCHAR(100)
);
GO

CREATE TABLE raw.Products (
    product_id INT,
    product_name NVARCHAR(150),
    category NVARCHAR(100),
    price DECIMAL(10, 2)
);
GO

CREATE TABLE raw.Orders (
    order_id INT,
    customer_id INT,
    order_date DATETIME2,
    status NVARCHAR(50)
);
GO

CREATE TABLE raw.OrderItems (
    order_item_id INT,
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10, 2)
);
GO

-- Shure 4 Tables have been created successfully in raw schema.


SELECT
    TABLE_SCHEMA,
    TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'raw'
ORDER BY TABLE_NAME;

--Insert Sample Data into raw schema tables.


USE EcommerceDW;
GO

INSERT INTO raw.Customers
    (customer_id, full_name, email, city)
VALUES
    (1, N'Ahmed Ali', 'ahmed@example.com', N'Cairo'),
    (2, N'Mona Hassan', 'mona@example.com', N'Alexandria'),
    (3, N'Omar Samir', 'omar@example.com', N'Assiut'),
    (4, N'Sara Mohamed', 'sara@example.com', N'Giza'),
    (5, N'Youssef Adel', 'youssef@example.com', N'Mansoura');

INSERT INTO raw.Products
    (product_id, product_name, category, price)
VALUES
    (101, N'Laptop', N'Electronics', 25000.00),
    (102, N'Headphones', N'Electronics', 1200.00),
    (103, N'Office Chair', N'Furniture', 3500.00),
    (104, N'Notebook', N'Stationery', 50.00),
    (105, N'Keyboard', N'Electronics', 800.00);

INSERT INTO raw.Orders
    (order_id, customer_id, order_date, status)
VALUES
    (1001, 1, '2026-10-01', N'Delivered'),
    (1002, 2, '2026-10-02', N'Delivered'),
    (1003, 1, '2026-10-03', N'Shipped'),
    (1004, 3, '2026-10-04', N'Pending'),
    (1005, 5, '2026-10-05', N'Cancelled');

INSERT INTO raw.OrderItems
    (order_item_id, order_id, product_id, quantity, unit_price)
VALUES
    (1, 1001, 101, 1, 25000.00),
    (2, 1001, 102, 2, 1200.00),
    (3, 1002, 103, 1, 3500.00),
    (4, 1003, 105, 2, 800.00),
    (5, 1004, 104, 5, 50.00),
    (6, 1005, 102, 1, 1200.00);
GO

--Sure Sample Data has been inserted successfully into raw schema tables.

SELECT 'customers' AS table_name, COUNT(*) AS record_count FROM raw.Customers
UNION ALL
SELECT 'products' AS table_name, COUNT(*) AS record_count FROM raw.Products
UNION ALL
SELECT 'orders' AS table_name, COUNT(*) AS record_count FROM raw.Orders
UNION ALL
SELECT 'order_items' AS table_name, COUNT(*) AS record_count FROM raw.OrderItems;

--Now Check Data Quality in raw schema tables.


USE EcommerceDW;
GO

SELECT
    o.order_id,
    o.customer_id
FROM raw.Orders AS o
LEFT JOIN raw.Customers AS c
    ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;



SELECT
    oi.order_item_id,
    oi.order_id,
    oi.product_id
FROM raw.OrderItems AS oi
LEFT JOIN raw.Products AS p
    ON oi.product_id = p.product_id
WHERE p.product_id IS NULL;


--Check for duplicate records and invalid data in raw schema tables.

-- 1. Check duplicate customer IDs
SELECT customer_id, COUNT(*) AS record_count
FROM raw.Customers
GROUP BY customer_id
HAVING COUNT(*) > 1;

-- 2. Check duplicate product IDs
SELECT product_id, COUNT(*) AS record_count
FROM raw.Products
GROUP BY product_id
HAVING COUNT(*) > 1;

-- 3. Check invalid quantities or prices
SELECT *
FROM raw.OrderItems
WHERE quantity <= 0 OR unit_price < 0;

-- 4. Check invalid product prices
SELECT *
FROM raw.Products
WHERE price < 0;

