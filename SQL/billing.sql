USE ims;
CREATE TABLE billing (
    bill_id INT IDENTITY(1,1) PRIMARY KEY,
    bill_no NVARCHAR(50) NOT NULL,
    bill_date NVARCHAR(20),
    customer_name NVARCHAR(100),
    customer_contact NVARCHAR(20),
    total_amount DECIMAL(10, 2),
    discount_val DECIMAL(10, 2),
    net_pay DECIMAL(10, 2)
);

-- =============================================
-- Display all records from the billing table
-- =============================================
SELECT * FROM billing;

-- =============================================
-- Display specific columns
-- =============================================
SELECT bill_id, bill_no, bill_date, customer_name, total_amount, net_pay 
FROM billing;

-- =============================================
-- Add a new bill
-- =============================================
INSERT INTO billing (bill_no, bill_date, customer_name, customer_contact, total_amount, discount_val, net_pay)
VALUES ('BILL-2025001', '2025-05-08', 'Mohamed Ali', '01123456789', 12500.00, 500.00, 12000.00);

-- =============================================
-- Update discount and net pay for a specific bill
-- =============================================
UPDATE billing
SET discount_val = 1000.00,
    net_pay = total_amount - 1000.00
WHERE bill_no = 'BILL-2025001';

-- =============================================
-- Delete a specific bill
-- =============================================
DELETE FROM billing 
WHERE bill_id = 5;

-- =============================================
-- Retrieve bills for a specific customer
-- =============================================
SELECT * FROM billing 
WHERE customer_name = 'Mohamed Ali';

-- =============================================
-- Bills with total_amount greater than 10000
-- =============================================
SELECT * FROM billing 
WHERE total_amount > 10000;

-- =============================================
-- Bills with discount applied
-- =============================================
SELECT * FROM billing 
WHERE discount_val > 0;

-- =============================================
-- Top 10 highest bills
-- =============================================
SELECT TOP 10 * FROM billing 
ORDER BY total_amount DESC;

-- =============================================
-- Count total number of bills
-- =============================================
SELECT COUNT(*) AS Total_Bills FROM billing;

-- =============================================
-- Total revenue (Sum of net_pay)
-- =============================================
SELECT SUM(net_pay) AS Total_Revenue FROM billing;

-- =============================================
-- Average bill amount
-- =============================================
SELECT AVG(total_amount) AS Average_Bill_Amount FROM billing;

-- =============================================
-- Count bills per customer
-- =============================================
SELECT customer_name, COUNT(*) AS Bill_Count, SUM(net_pay) AS Total_Paid
FROM billing
GROUP BY customer_name
ORDER BY Total_Paid DESC;

-- =============================================
-- Bills by date (if bill_date is used)
-- =============================================
SELECT bill_date, COUNT(*) AS Bills_Per_Day, SUM(net_pay) AS Revenue_Per_Day
FROM billing
GROUP BY bill_date
ORDER BY bill_date DESC;

-- =============================================
-- Classify bills based on amount
-- =============================================
SELECT 
    bill_no,
    customer_name,
    total_amount,
    CASE 
        WHEN total_amount >= 20000 THEN 'High Value'
        WHEN total_amount BETWEEN 10000 AND 19999 THEN 'Medium Value'
        ELSE 'Small Value'
    END AS bill_category
FROM billing;

-- =============================================
-- Bills with high discount percentage
-- =============================================
SELECT 
    bill_no,
    customer_name,
    total_amount,
    discount_val,
    (discount_val / total_amount * 100) AS Discount_Percentage
FROM billing
WHERE total_amount > 0
ORDER BY Discount_Percentage DESC;

-- =============================================
-- Customers who have more than 3 bills
-- =============================================
SELECT customer_name, COUNT(*) AS Bill_Count
FROM billing
GROUP BY customer_name
HAVING COUNT(*) > 3;

-- =============================================
-- Search bills by customer contact
-- =============================================
SELECT * FROM billing 
WHERE customer_contact LIKE '011%';

-- =============================================
-- Show latest 5 bills
-- =============================================
SELECT TOP 5 * FROM billing 
ORDER BY bill_id DESC;