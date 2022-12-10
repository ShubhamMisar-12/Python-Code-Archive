import pandas as pd
import sqlite3
from sqlite3 import Error

def create_connection(db_file, delete_db=False):
    import os
    if delete_db and os.path.exists(db_file):
        os.remove(db_file)

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = 1")
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql, drop_table_name=None):
    
    if drop_table_name: # You can optionally pass drop_table_name to drop the table. 
        try:
            c = conn.cursor()
            c.execute("""DROP TABLE IF EXISTS %s""" % (drop_table_name))
        except Error as e:
            print(e)
    
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def execute_sql_statement(sql_statement, conn):
    cur = conn.cursor()
    cur.execute(sql_statement)

    rows = cur.fetchall()

    return rows

def insert_region(conn, values):
    try:
        sql = ''' INSERT INTO Region(RegionId, Region)
                VALUES(?, ?) '''
        cur = conn.cursor()
        cur.execute(sql, values)
        return cur.lastrowid
    except Error as e:
        print(e)


conn = sqlite3.connect("normalized.db")
#ProductName, ProductUnitPrice, ProductUnitPrice * QuantityOrdered as total
cust_name = 'Alejandra Camino'
# sql_statement =  """
#     SELECT Round(ProductUnitPrice * QuantityOrdered, 2) as total FROM (SELECT * 
#     FROM Customer JOIN OrderDetail ON Customer.CustomerID = OrderDetail.CustomerID) as 
#     order_customer JOIN Product ON order_customer.ProductID = Product.ProductId """

# sql_statement = """
#         SELECT Country.Country, Region.Region, Round(Sum(ProductUnitPrice * QuantityOrdered),2) as CountryTotal, 
#         RANK() OVER (ORDER BY CountryTotal) Rank FROM Customer 
#         INNER JOIN OrderDetail ON Customer.CustomerID = OrderDetail.CustomerID  
#         INNER JOIN Product ON OrderDetail.ProductID = Product.ProductId
#         INNER JOIN Country ON Customer.CountryID = Country.CountryID
#         INNER JOIN Region ON Country.RegionID = Region.RegionID
        
        
       
        
# """

sql_statement = """ 
        SELECT FirstName,
        Rank() OVER(ORDER BY LastName) Rank FROM Customer
          
"""
df = pd.read_sql_query(sql_statement, conn)
print(df)
conn.close()    
