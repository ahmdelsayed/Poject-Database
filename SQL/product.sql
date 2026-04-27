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