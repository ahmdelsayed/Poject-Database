import pyodbc

def create_db():
   
    connection_string = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=***\\SQLEXPRESS;'  
        'DATABASE=master;'         
        'Trusted_Connection=yes;'
        'TrustServerCertificate=yes;'
    )
    
    try:
        # connect server SQL 
        con = pyodbc.connect(connection_string, autocommit=True)
        cur = con.cursor()
        
        
        cur.execute("IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'ims') CREATE DATABASE ims")
        print("Database 'ims' check/create: Done")
        
        
        cur.execute("USE ims")
        
    

        print("SQL Server Database and Table are ready!")
        
    except Exception as ex:
        print(f"Error: {str(ex)}")
    finally:
        if 'con' in locals():
            con.close()

if __name__ == "__main__":
    create_db()
