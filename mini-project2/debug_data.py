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


conn_orders = sqlite3.connect("normalized.db")
with open('data.csv') as file:
        file_data = file.read()
    
header = None
customer_set = []
for line in file_data.split("\n"):
    if header == None:
        header = line.split("\t")
        continue
    ln = line.split("\t")
    try:
        if [ln[0], ln[1], ln[2], ln[3]] not in customer_set:
            customer_set.append([ln[0], ln[1], ln[2], ln[3]])
    except:
        continue
customer_set = sorted(customer_set, key = lambda x: x[0])
conn_orders.close()
customer_id = 0
for customer in customer_set:
    customer_names = customer[0].split(" ")
    customer_last_name = " ".join(customer_names[1:])
    customer_id += 1
    print(customer_id, customer_names[0],customer_last_name.strip(),customer[1], customer[2], customer[3])
