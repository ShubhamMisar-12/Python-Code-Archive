import sqlite3
import pandas as pd
conn = sqlite3.connect("normalized.db")
sql_statement = """ 
        SELECT FirstName,
        Rank() OVER(ORDER BY LastName) cust FROM Customer          
"""
df = pd.read_sql_query(sql_statement, conn)
print(df)
conn.close()   