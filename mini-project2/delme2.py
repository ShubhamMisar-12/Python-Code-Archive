import sqlite3
import pandas as pd
conn = sqlite3.connect("normalized.db")
sql_statement = """ 
    WITH QuaterYear AS(
    SELECT
        CASE
            WHEN 0 + strftime('%m', OrderDetail.OrderDate) BETWEEN 1
            AND 3 THEN 'Q1'
            WHEN 0 + strftime('%m', OrderDetail.OrderDate) BETWEEN 4
            AND 6 THEN 'Q2'
            WHEN 0 + strftime('%m', OrderDetail.OrderDate) BETWEEN 7
            AND 9 THEN 'Q3'
            WHEN 0 + strftime('%m', OrderDetail.OrderDate) BETWEEN 10
            AND 12 THEN 'Q4'
        END Quarter,
        cast(strftime('%Y', OrderDetail.OrderDate) AS INT) Year,
        Customer.CustomerID, Round(Sum(ProductUnitPrice * QuantityOrdered), 2) as Total 
        FROM  Customer 
        INNER JOIN OrderDetail ON Customer.CustomerID = OrderDetail.CustomerID  
        INNER JOIN Product ON OrderDetail.ProductID = Product.ProductId
        GROUP BY Year, Quarter, Customer.CustomerID
        ORDER BY Year
        ) 
        
    SELECT *,
    rank() OVER(Partition by Year, Quarter ORDER BY Total DESC) CustomerRank
    FROM QuaterYear Order by year
    """
df = pd.read_sql_query(sql_statement, conn)
display(df)
conn.close()   