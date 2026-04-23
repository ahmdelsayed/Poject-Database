import pyodbc

def create_db():
   
    connection_string = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=AMD\\SQLEXPRESS;'  
        'DATABASE=master;'         
        'Trusted_Connection=yes;'
        'TrustServerCertificate=yes;'
    )
    
    try:
        # الاتصال بالسيرفر
        con = pyodbc.connect(connection_string, autocommit=True)
        cur = con.cursor()
        
        
        cur.execute("IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'ims') CREATE DATABASE ims")
        print("Database 'ims' check/create: Done")
        
        
        cur.execute("USE ims")
        
        
        cur.execute("""
        IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[employee]') AND type in (N'U'))
        BEGIN
            CREATE TABLE employee(
                eid INT PRIMARY KEY IDENTITY(1,1),
                name VARCHAR(100),
                email VARCHAR(100),
                gender VARCHAR(20),
                contact VARCHAR(20),
                dob VARCHAR(50),
                doj VARCHAR(50),
                pass VARCHAR(50),
                utype VARCHAR(50),
                address VARCHAR(MAX),
                salary VARCHAR(50)
            )
            PRINT 'Table employee created successfully!'
        END
        """)
        
        print("SQL Server Database and Table are ready!")
        
    except Exception as ex:
        print(f"Error: {str(ex)}")
    finally:
        if 'con' in locals():
            con.close()

if __name__ == "__main__":
    create_db()