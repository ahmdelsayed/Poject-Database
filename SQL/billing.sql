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