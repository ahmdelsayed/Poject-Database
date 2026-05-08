USE ims;
CREATE TABLE product (
    pid INT PRIMARY KEY IDENTITY(1,1),
    Category NVARCHAR(100),
    Supplier NVARCHAR(100),
    name NVARCHAR(100),
    price NVARCHAR(100),
    qty NVARCHAR(100),
    status NVARCHAR(50)
);

---------------------------------------------------------------------------------------------------

SET IDENTITY_INSERT [dbo].[product] ON 
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (1, N'Mobile', N'ahmed', N'iphone 14', N'64000 LE', N'84', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (3, N'Mobile', N'ahmed', N'Oppo Reno', N'24,999 EGP', N'45', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (4, N'Mobile', N'ahmed', N'HUAWEI nova', N'25,999 EGP', N'22', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (5, N'phone', N'ahmed', N'nokia', N'1000', N'5', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (6, N'Mobile Phones', N'Apple Distributor', N'iPhone Model', N'107', N'10', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (7, N'Laptops', N'Dell Technologies', N'Dell Laptop XPS', N'114', N'12', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (8, N'Home Appliances', N'LG Electronics', N'LG Washing Machine', N'121', N'13', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (9, N'Furniture', N'Local Wholesale Co', N'Office Chair', N'128', N'14', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (10, N'Groceries', N'Local Wholesale Co', N'Rice Bag 5kg', N'135', N'15', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (11, N'Clothing', N'Local Wholesale Co', N'T-Shirt Cotton', N'142', N'16', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (12, N'Accessories', N'Local Wholesale Co', N'Backpack', N'149', N'16', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (13, N'Sports Equipment', N'Local Wholesale Co', N'Football', N'156', N'18', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (14, N'Stationery', N'Local Wholesale Co', N'Notebook Set', N'163', N'19', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (15, N'Electronics', N'Samsung Egypt', N'Samsung Galaxy A Series', N'170', N'20', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (16, N'Mobile Phones', N'Apple Distributor', N'iPhone Model', N'177', N'21', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (17, N'Laptops', N'Dell Technologies', N'Dell Laptop XPS', N'184', N'22', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (18, N'Home Appliances', N'LG Electronics', N'LG Washing Machine', N'191', N'23', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (19, N'Furniture', N'Local Wholesale Co', N'Office Chair', N'198', N'24', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (20, N'Groceries', N'Local Wholesale Co', N'Rice Bag 5kg', N'205', N'10', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (21, N'Clothing', N'Local Wholesale Co', N'T-Shirt Cotton', N'212', N'11', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (22, N'Accessories', N'Local Wholesale Co', N'Backpack', N'219', N'12', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (23, N'Sports Equipment', N'Local Wholesale Co', N'Football', N'226', N'13', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (24, N'Stationery', N'Local Wholesale Co', N'Notebook Set', N'233', N'14', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (25, N'Electronics', N'Samsung Egypt', N'Samsung Galaxy A Series', N'240', N'15', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (26, N'Mobile Phones', N'Apple Distributor', N'iPhone Model', N'247', N'16', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (27, N'Laptops', N'Dell Technologies', N'Dell Laptop XPS', N'254', N'17', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (28, N'Home Appliances', N'LG Electronics', N'LG Washing Machine', N'261', N'18', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (29, N'Furniture', N'Local Wholesale Co', N'Office Chair', N'268', N'19', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (30, N'Groceries', N'Local Wholesale Co', N'Rice Bag 5kg', N'275', N'20', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (31, N'Clothing', N'Local Wholesale Co', N'T-Shirt Cotton', N'282', N'21', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (32, N'Accessories', N'Local Wholesale Co', N'Backpack', N'289', N'22', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (33, N'Sports Equipment', N'Local Wholesale Co', N'Football', N'296', N'23', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (34, N'Stationery', N'Local Wholesale Co', N'Notebook Set', N'303', N'24', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (35, N'Electronics', N'Samsung Egypt', N'Samsung Galaxy A Series', N'310', N'10', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (36, N'Mobile Phones', N'Apple Distributor', N'iPhone Model', N'317', N'11', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (37, N'Laptops', N'Dell Technologies', N'Dell Laptop XPS', N'324', N'12', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (38, N'Home Appliances', N'LG Electronics', N'LG Washing Machine', N'331', N'13', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (39, N'Furniture', N'Local Wholesale Co', N'Office Chair', N'338', N'14', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (40, N'Groceries', N'Local Wholesale Co', N'Rice Bag 5kg', N'345', N'15', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (41, N'Clothing', N'Local Wholesale Co', N'T-Shirt Cotton', N'352', N'16', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (42, N'Accessories', N'Local Wholesale Co', N'Backpack', N'359', N'17', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (43, N'Sports Equipment', N'Local Wholesale Co', N'Football', N'366', N'18', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (44, N'Stationery', N'Local Wholesale Co', N'Notebook Set', N'373', N'19', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (45, N'Electronics', N'Samsung Egypt', N'Samsung Galaxy A Series', N'380', N'20', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (46, N'Mobile Phones', N'Apple Distributor', N'iPhone Model', N'387', N'21', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (47, N'Laptops', N'Dell Technologies', N'Dell Laptop XPS', N'394', N'22', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (48, N'Home Appliances', N'LG Electronics', N'LG Washing Machine', N'401', N'23', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (49, N'Furniture', N'Local Wholesale Co', N'Office Chair', N'408', N'24', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (50, N'Groceries', N'Local Wholesale Co', N'Rice Bag 5kg', N'415', N'10', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (51, N'Clothing', N'Local Wholesale Co', N'T-Shirt Cotton', N'422', N'11', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (52, N'Accessories', N'Local Wholesale Co', N'Backpack', N'429', N'12', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (53, N'Sports Equipment', N'Local Wholesale Co', N'Football', N'436', N'13', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (54, N'Stationery', N'Local Wholesale Co', N'Notebook Set', N'443', N'14', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (55, N'Electronics', N'Samsung Egypt', N'Samsung Galaxy A Series', N'450', N'15', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (56, N'Mobile Phones', N'Apple Distributor', N'iPhone Model', N'457', N'16', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (57, N'Laptops', N'Dell Technologies', N'Dell Laptop XPS', N'464', N'17', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (58, N'Home Appliances', N'LG Electronics', N'LG Washing Machine', N'471', N'18', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (59, N'Furniture', N'Local Wholesale Co', N'Office Chair', N'478', N'19', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (60, N'Groceries', N'Local Wholesale Co', N'Rice Bag 5kg', N'485', N'20', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (61, N'Clothing', N'Local Wholesale Co', N'T-Shirt Cotton', N'492', N'21', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (62, N'Accessories', N'Local Wholesale Co', N'Backpack', N'499', N'22', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (63, N'Sports Equipment', N'Local Wholesale Co', N'Football', N'506', N'23', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (64, N'Stationery', N'Local Wholesale Co', N'Notebook Set', N'513', N'24', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (65, N'Electronics', N'Samsung Egypt', N'Samsung Galaxy A Series', N'520', N'10', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (66, N'Mobile Phones', N'Apple Distributor', N'iPhone Model', N'527', N'11', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (67, N'Laptops', N'Dell Technologies', N'Dell Laptop XPS', N'534', N'12', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (68, N'Home Appliances', N'LG Electronics', N'LG Washing Machine', N'541', N'13', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (69, N'Furniture', N'Local Wholesale Co', N'Office Chair', N'548', N'14', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (70, N'Groceries', N'Local Wholesale Co', N'Rice Bag 5kg', N'555', N'15', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (71, N'Clothing', N'Local Wholesale Co', N'T-Shirt Cotton', N'562', N'16', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (72, N'Accessories', N'Local Wholesale Co', N'Backpack', N'569', N'17', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (73, N'Sports Equipment', N'Local Wholesale Co', N'Football', N'576', N'18', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (74, N'Stationery', N'Local Wholesale Co', N'Notebook Set', N'583', N'19', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (75, N'Electronics', N'Samsung Egypt', N'Samsung Galaxy A Series', N'590', N'20', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (76, N'Mobile Phones', N'Apple Distributor', N'iPhone Model', N'597', N'21', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (77, N'Laptops', N'Dell Technologies', N'Dell Laptop XPS', N'604', N'22', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (78, N'Home Appliances', N'LG Electronics', N'LG Washing Machine', N'611', N'23', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (79, N'Furniture', N'Local Wholesale Co', N'Office Chair', N'618', N'24', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (80, N'Groceries', N'Local Wholesale Co', N'Rice Bag 5kg', N'625', N'10', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (81, N'Clothing', N'Local Wholesale Co', N'T-Shirt Cotton', N'632', N'11', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (82, N'Accessories', N'Local Wholesale Co', N'Backpack', N'639', N'12', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (83, N'Sports Equipment', N'Local Wholesale Co', N'Football', N'646', N'13', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (84, N'Stationery', N'Local Wholesale Co', N'Notebook Set', N'653', N'14', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (85, N'Electronics', N'Samsung Egypt', N'Samsung Galaxy A Series', N'660', N'15', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (86, N'Mobile Phones', N'Apple Distributor', N'iPhone Model', N'667', N'16', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (87, N'Laptops', N'Dell Technologies', N'Dell Laptop XPS', N'674', N'17', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (88, N'Home Appliances', N'LG Electronics', N'LG Washing Machine', N'681', N'18', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (89, N'Furniture', N'Local Wholesale Co', N'Office Chair', N'688', N'19', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (90, N'Groceries', N'Local Wholesale Co', N'Rice Bag 5kg', N'695', N'20', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (91, N'Clothing', N'Local Wholesale Co', N'T-Shirt Cotton', N'702', N'21', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (92, N'Accessories', N'Local Wholesale Co', N'Backpack', N'709', N'22', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (93, N'Sports Equipment', N'Local Wholesale Co', N'Football', N'716', N'23', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (94, N'Stationery', N'Local Wholesale Co', N'Notebook Set', N'723', N'24', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (95, N'Electronics', N'Samsung Egypt', N'Samsung Galaxy A Series', N'730', N'10', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (96, N'Mobile Phones', N'Apple Distributor', N'iPhone Model', N'737', N'11', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (97, N'Laptops', N'Dell Technologies', N'Dell Laptop XPS', N'744', N'12', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (98, N'Home Appliances', N'LG Electronics', N'LG Washing Machine', N'751', N'13', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (99, N'Furniture', N'Local Wholesale Co', N'Office Chair', N'758', N'14', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (100, N'Groceries', N'Local Wholesale Co', N'Rice Bag 5kg', N'765', N'15', N'Active') 
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (101, N'Clothing', N'Local Wholesale Co', N'T-Shirt Cotton', N'772', N'16', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (102, N'Accessories', N'Local Wholesale Co', N'Backpack', N'779', N'17', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (103, N'Sports Equipment', N'Local Wholesale Co', N'Football', N'786', N'18', N'Active')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (104, N'Stationery', N'Local Wholesale Co', N'Notebook Set', N'793', N'19', N'Inactive')
INSERT [dbo].[product] ([pid], [Category], [Supplier], [name], [price], [qty], [status]) VALUES (105, N'Electronics', N'Samsung Egypt', N'Samsung Galaxy A Series', N'800', N'20', N'Active')
SET IDENTITY_INSERT [dbo].[product] OFF
GO

-- =============================================
-- Display all records from the product table
-- =============================================
SELECT * FROM product;

-- =============================================
-- Display specific columns (name, category, price, qty, status)
-- =============================================
SELECT name, Category, price, qty, status 
FROM product;

-- =============================================
-- Display unique categories
-- =============================================
SELECT DISTINCT Category FROM product;

-- =============================================
-- Display unique suppliers
-- =============================================
SELECT DISTINCT Supplier FROM product;

-- =============================================
-- Add a new product
-- =============================================
SET IDENTITY_INSERT [dbo].[product] ON;
INSERT INTO product (pid, Category, Supplier, name, price, qty, status)
VALUES (106, N'Mobile Phones', N'Apple Distributor', N'iPhone 16 Pro', N'95000 LE', N'25', N'Active');
SET IDENTITY_INSERT [dbo].[product] OFF;

-- =============================================
-- Update price for a specific product
-- =============================================
UPDATE product
SET price = N'72000 LE'
WHERE name = 'iphone 14';

-- =============================================
-- Update status to Inactive for low quantity products
-- =============================================
UPDATE product
SET status = 'Inactive'
WHERE CAST(qty AS INT) < 15;

-- =============================================
-- Delete inactive products
-- =============================================
DELETE FROM product 
WHERE status = 'Inactive';

-- =============================================
-- Retrieve products in 'Mobile' or 'Mobile Phones' category
-- =============================================
SELECT * FROM product 
WHERE Category IN ('Mobile', 'Mobile Phones');

-- =============================================
-- Products with price containing 'LE'
-- =============================================
SELECT * FROM product 
WHERE price LIKE '%LE%';

-- =============================================
-- Products where quantity is less than 20
-- =============================================
SELECT * FROM product 
WHERE CAST(qty AS INT) < 20;

-- =============================================
-- Top 10 products ordered by quantity descending
-- =============================================
SELECT TOP 10 * FROM product 
ORDER BY CAST(qty AS INT) DESC;

-- =============================================
-- Count total number of products
-- =============================================
SELECT COUNT(*) AS Total_Products FROM product;

-- =============================================
-- Count products per category
-- =============================================
SELECT Category, COUNT(*) AS Product_Count
FROM product
GROUP BY Category
ORDER BY Product_Count DESC;

-- =============================================
-- Count products per supplier
-- =============================================
SELECT Supplier, COUNT(*) AS Product_Count
FROM product
GROUP BY Supplier
ORDER BY Product_Count DESC;

-- =============================================
-- Products by status
-- =============================================
SELECT status, COUNT(*) AS Count
FROM product
GROUP BY status;

-- =============================================
-- Classify products based on quantity
-- =============================================
SELECT 
    name,
    Category,
    qty,
    CASE 
        WHEN CAST(qty AS INT) >= 20 THEN 'High Stock'
        WHEN CAST(qty AS INT) BETWEEN 10 AND 19 THEN 'Medium Stock'
        ELSE 'Low Stock'
    END AS stock_level
FROM product;

-- =============================================
-- Find products supplied by 'Apple Distributor' or 'Samsung Egypt'
-- =============================================
SELECT * FROM product 
WHERE Supplier IN ('Apple Distributor', 'Samsung Egypt');

-- =============================================
-- Products whose name starts with 'iPhone'
-- =============================================
SELECT * FROM product 
WHERE name LIKE 'iPhone%';

-- =============================================
-- Maximum and Minimum quantity
-- =============================================
SELECT 
    MAX(CAST(qty AS INT)) AS Max_Quantity,
    MIN(CAST(qty AS INT)) AS Min_Quantity
FROM product;

-- =============================================
-- Show active products only
-- =============================================
SELECT * FROM product 
WHERE status = 'Active';

-- =============================================
-- ADDED QUERIES
-- =============================================

-- Total value of stock (price * qty) for each product
SELECT 
    name,
    price,
    qty,
    CAST(price AS DECIMAL(18,2)) * CAST(qty AS INT) AS Stock_Value
FROM product;

-- Average quantity per category
SELECT 
    Category,
    AVG(CAST(qty AS INT)) AS Avg_Quantity,
    COUNT(*) AS Product_Count
FROM product
GROUP BY Category
ORDER BY Avg_Quantity DESC;

-- Products with high stock and Active status
SELECT * FROM product 
WHERE status = 'Active' AND CAST(qty AS INT) >= 20;

-- Search for products containing 'Laptop' or 'Phone' in name
SELECT * FROM product 
WHERE name LIKE '%Phone%' OR name LIKE '%Laptop%';

-- Suppliers who have Inactive products
SELECT DISTINCT Supplier 
FROM product 
WHERE status = 'Inactive';

-- Number of products per supplier having more than 5 products
SELECT Supplier, COUNT(*) AS Product_Count
FROM product
GROUP BY Supplier
HAVING COUNT(*) > 5
ORDER BY Product_Count DESC;