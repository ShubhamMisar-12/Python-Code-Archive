### Utility Functions
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

def insert_country(conn, values):
    # print(values)
    try:
        sql = ''' INSERT INTO Country(CountryID, Country, RegionID)
                VALUES(?, ?, ?) '''
        cur = conn.cursor()
        cur.execute(sql, values)
        return cur.lastrowid
    except Error as e:
        print(e)

def insert_customer(conn, values):
        try:
            sql = ''' INSERT INTO Customer(CustomerID, FirstName, LastName, Address, City, CountryID)
                    VALUES(?, ?, ?, ?, ?, ?) '''
            cur = conn.cursor()
            cur.execute(sql, values)
            return cur.lastrowid
        except Error as e:
            print(e)
def insert_product_category(conn, values):
    try:
        sql = ''' INSERT INTO ProductCategory(ProductCategoryID, ProductCategory, ProductCategoryDescription)
                VALUES(?, ?, ?) '''
        cur = conn.cursor()
        cur.execute(sql, values)
        return cur.lastrowid
    except Error as e:
        print(e)

def insert_product(conn, values):
    try:
        sql = ''' INSERT INTO Product(ProductID, ProductName, ProductUnitPrice, ProductCategoryID)
                VALUES(?, ?, ?, ?) '''
        cur = conn.cursor()
        cur.execute(sql, values)
        return cur.lastrowid
    except Error as e:
        print(e)

def insert_order_details(conn, values):
    try:
        #print(values)
        sql = ''' INSERT INTO OrderDetail(OrderID, CustomerID, ProductID, OrderDate, QuantityOrdered)
                VALUES(?, ?, ?, ?, ?) '''
        cur = conn.cursor()
        cur.execute(sql, values)
        return cur.lastrowid
    except Error as e:
        print(e)

def step1_create_region_table(data_filename, normalized_database_filename):
    # Inputs: Name of the data and normalized database filename
    # Output: None
    
    ### BEGIN SOLUTION

    ## creating table for Region
    conn_norm = create_connection(normalized_database_filename)
    
    create_table_sql = """CREATE TABLE IF NOT EXISTS [Region] (
            [RegionID] Integer not null primary key,
            [Region] Text not null
    ); """

    create_table(conn_norm, create_table_sql)
    
    ## Parsing data.csv file for getting region

    with open(data_filename) as file:
        file_data = file.read()

    header = None
    region_set = []
    for line in file_data.split("\n"):
        if header == None:
            header = line.split("\t")
            continue
        ln = line.split("\t")
        try:
            temp = ln[4]
            if temp not in region_set:
                region_set.append(temp)
        except:
            continue
    region_set.sort()

    ## Inserging values into Region table
    with conn_norm:
        region_id = 0
        for region in region_set:
            region_id += 1
            insert_region(conn_norm, (region_id, region ))
    conn_norm.close()

    ### END SOLUTION

def step2_create_region_to_regionid_dictionary(normalized_database_filename):
    
    
    ### BEGIN SOLUTION
    conn_norm = create_connection(normalized_database_filename)
    region_list = execute_sql_statement("SELECT * FROM Region", conn_norm)
    region_dict = dict(map(lambda x: (x[1], x[0]), sorted(region_list)))
    conn_norm.close()
    return region_dict
    ### END SOLUTION


def step3_create_country_table(data_filename, normalized_database_filename):
    # Inputs: Name of the data and normalized database filename
    # Output: None
    
    ### BEGIN SOLUTION

    ## Creating table Country
    conn_norm = create_connection(normalized_database_filename)
    sql_statement = """
    CREATE TABLE Country(
    [CountryID] integer not null Primary key,
    [Country] Text not null,
    [RegionID] integer not null, 
    FOREIGN KEY(RegionID) REFERENCES Region(RegionID)
    );"""


    create_table(conn_norm, sql_statement)

    with open(data_filename) as file:
        file_data = file.read()

    
    header = None
    country_set = []
    for line in file_data.split("\n"):
        if header == None:
            header = line.split("\t")
            continue
        ln = line.split("\t")
        try:
            if [ln[3], ln[4]] not in country_set:
                country_set.append([ln[3],ln[4]])
        except:
            continue
    country_set = sorted(country_set, key = lambda x : x[0])
    #print(country_set)
    ## Inserting into country Table
    region_dict = step2_create_region_to_regionid_dictionary(normalized_database_filename)
    with conn_norm:
        country_id = 0
        for country in country_set:
            country_id += 1

            insert_country(conn_norm, (country_id, country[0], region_dict[country[1]]))
    
    conn_norm.close()
    ### END SOLUTION


def step4_create_country_to_countryid_dictionary(normalized_database_filename):
    
    
    ### BEGIN SOLUTION
    conn_norm = create_connection(normalized_database_filename)
    country_list = execute_sql_statement("SELECT CountryID, Country FROM Country", conn_norm)
    country_dict = dict(map(lambda x: (x[1], x[0]), sorted(country_list)))
    conn_norm.close()
    return country_dict

    ### END SOLUTION
        
        
def step5_create_customer_table(data_filename, normalized_database_filename):

    ### BEGIN SOLUTION
    conn_norm = create_connection(normalized_database_filename)
    sql_statement = """CREATE TABLE Customer(
    [CustomerID] integer not null Primary Key,
    [FirstName] Text not null,
    [LastName] Text not null,
    [Address] Text not null,
    [City] Text not null,
    [CountryID] integer not null, 
    FOREIGN KEY(CountryID) REFERENCES Country(CountryID)
    );"""
    create_table(conn_norm, sql_statement)


    ## Inserting into Customer ta
    with open(data_filename) as file:
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
    country_dic = step4_create_country_to_countryid_dictionary(normalized_database_filename)
    customer_set = sorted(customer_set, key = lambda x: x[0])
    with conn_norm:
        customer_id = 0
        for customer in customer_set:
            customer_names = customer[0].split(" ")
            customer_last_name = " ".join(customer_names[1:])
            customer_id += 1
            insert_customer(conn_norm, (customer_id, customer_names[0], customer_last_name.strip() ,customer[1], customer[2], country_dic[customer[3]]))

    conn_norm.close()
    ### END SOLUTION


def step6_create_customer_to_customerid_dictionary(normalized_database_filename):
    
    
    ### BEGIN SOLUTION
    conn_norm = create_connection(normalized_database_filename)
    customer_list = execute_sql_statement("SELECT CustomerID, FirstName, LastName FROM Customer", conn_norm)
    customer_dict = dict(map(lambda x: (" ".join(x[1:]), x[0]), sorted(customer_list)))
    conn_norm.close()
    return customer_dict

    ### END SOLUTION
        
def step7_create_productcategory_table(data_filename, normalized_database_filename):
    # Inputs: Name of the data and normalized database filename
    # Output: None

    
    ### BEGIN SOLUTION

    ## Creating table ProductCategory

    conn_norm = create_connection(normalized_database_filename)
    sql_statement = """CREATE TABLE ProductCategory(
    [ProductCategoryID] integer not null Primary Key,
    [ProductCategory] Text not null,
    [ProductCategoryDescription] Text not null
    );"""
    create_table(conn_norm, sql_statement)


    ## Inserting into table ProductCategory
    with open(data_filename) as file:
        file_data = file.read()
    
    header = None
    product_category = []
    for line in file_data.split("\n"):
        if header == None:
            header = line.split("\t")
            continue
        ln = line.split("\t")
        try:
            ln6 = ln[6].split(";")
            ln7 = ln[7].split(";")
            for prd_cat, prd_cat_desc in zip(ln6, ln7):
                if [prd_cat, prd_cat_desc] not in product_category:
                    product_category.append([prd_cat, prd_cat_desc])
        except:
            continue
    product_category = sorted(product_category, key =  lambda x: x[0])
    with conn_norm:
        product_category_id = 0
        for prod_category in product_category:
            product_category_id += 1
            insert_product_category(conn_norm, (product_category_id, prod_category[0], prod_category[1]))

    conn_norm.close()
   
    ### END SOLUTION

def step8_create_productcategory_to_productcategoryid_dictionary(normalized_database_filename):
    
    
    ### BEGIN SOLUTION
    conn_norm = create_connection(normalized_database_filename)
    product_category_list = execute_sql_statement("SELECT ProductCategoryID, ProductCategory FROM ProductCategory", conn_norm)
    product_category_dict = dict(map(lambda x: (x[1], x[0]), sorted(product_category_list)))
    conn_norm.close()
    return product_category_dict

    ### END SOLUTION
        

def step9_create_product_table(data_filename, normalized_database_filename):
    # Inputs: Name of the data and normalized database filename
    # Output: None

    
    ### BEGIN SOLUTION
    
    # Create Product Table to store products

    conn_norm = create_connection(normalized_database_filename)
    sql_statement = """CREATE TABLE Product(
    [ProductID] integer not null Primary key,
    [ProductName] Text not null,
    [ProductUnitPrice] Real not null,
    [ProductCategoryID] integer not null,
    FOREIGN KEY(ProductCategoryID) REFERENCES ProductCategory(ProductCategoryID)
    );"""
    create_table(conn_norm, sql_statement)


    ## Inserting into Product Table


    with open(data_filename) as file:
        file_data = file.read()

    header = None
    product = []
    for line in file_data.split("\n"):
        if header == None:
            header = line.split("\t")
            continue
        ln = line.split("\t")
        try:
            ln5 = ln[5].split(";")
            ln6 = ln[6].split(";")
            ln8 = ln[8].split(";")
            
            
            for prod, prod_catg, prod_price  in zip(ln5, ln6, ln8):
                
                if [prod, prod_catg, prod_price] not in product:
                    product.append([prod, prod_catg, prod_price])
        except:
            continue
    #print(product)
    product = sorted(product, key = lambda x: x[0])
    product_category_dict = step8_create_productcategory_to_productcategoryid_dictionary(normalized_database_filename)
    with conn_norm:
        product_id = 0
        for prod in product:
            #print(prod)
            product_id += 1
            #print((product_id, prod[0], prod[2], product_category_dict[prod[1]]))
            insert_product(conn_norm, (product_id, prod[0], float(prod[2]), product_category_dict[prod[1]]))

    conn_norm.close()
   
    ### END SOLUTION


def step10_create_product_to_productid_dictionary(normalized_database_filename):
    
    ### BEGIN SOLUTION
    conn_norm = create_connection(normalized_database_filename)
    product_list = execute_sql_statement("SELECT ProductID, ProductName FROM Product", conn_norm)
    product_dict = dict(map(lambda x: (x[1], x[0]), sorted(product_list)))
    conn_norm.close()
    return product_dict


    ### END SOLUTION
        

def step11_create_orderdetail_table(data_filename, normalized_database_filename):
    # Inputs: Name of the data and normalized database filename
    # Output: None

    
    ### BEGIN SOLUTION
    conn_norm = create_connection(normalized_database_filename)
    sql_statement = """CREATE TABLE OrderDetail(
    [OrderID] integer not null Primary Key,
    [CustomerID] integer not null, 
    [ProductID] integer not null, 
    [OrderDate] integer not null, 
    [QuantityOrdered] integer not null,
    FOREIGN KEY(CustomerID) REFERENCES Customer(CustomerID)
    FOREIGN KEY(ProductID) REFERENCES Product(ProductID)
    );"""

    create_table(conn_norm, sql_statement)

    import datetime
    ## Inserting into Customer ta
    with open('data.csv') as file:
        file_data = file.read()
        header = None
        order = []
        for line in file_data.split("\n"):
            if header == None:
                header = line.split("\t")
                continue
            ln = line.split("\t")
            #print(header)
            try:
                ln4 = ln[5].split(";")
                ln9 = ln[9].split(";")
                ln10 = ln[10].split(";")
                #print(header)
                for prod, order_qnty, order_date in zip(ln4, ln9, ln10):
                    #print(prod)
                    order.append([ln[0], prod, order_qnty, order_date])
            except:
                continue

        customer_dict = step6_create_customer_to_customerid_dictionary(normalized_database_filename)
        product_dict = step10_create_product_to_productid_dictionary(normalized_database_filename)
        #print(product)
        with conn_norm:
            order_id = 0
            for ord in order:
                order_id += 1
                order_date = datetime.datetime.strptime(ord[3], '%Y%m%d').strftime('%Y-%m-%d')
                insert_order_details(conn_norm, (order_id, customer_dict[ord[0]], product_dict[ord[1]], order_date, int(ord[2])))

        conn_norm.close()
            ### END SOLUTION


def ex1(conn, CustomerName):
    
    # Simply, you are fetching all the rows for a given CustomerName. 
    # Write an SQL statement that SELECTs From the OrderDetail table and joins with the Customer and Product table.
    # Pull out the following columns. 
    # Name -- concatenation of FirstName and LastName
    # ProductName
    # OrderDate
    # ProductUnitPrice
    # QuantityOrdered
    # Total -- which is calculated from multiplying ProductUnitPrice with QuantityOrdered -- round to two decimal places
    # HINT: USE customer_to_customerid_dict to map customer name to customer id and then use where clause with CustomerID
    
    ### BEGIN SOLUTION
    sql_statement = """
    SELECT FirstName || " " || LastName as Name,  ProductName,order_customer.OrderDate,ProductUnitPrice, 
    order_customer.QuantityOrdered, Round(ProductUnitPrice * QuantityOrdered, 2) as Total FROM (SELECT * 
    FROM Customer JOIN OrderDetail ON Customer.CustomerID = OrderDetail.CustomerID) as 
    order_customer JOIN Product ON order_customer.ProductID = Product.ProductId WHERE name = '{}' """.format(CustomerName) 
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex2(conn, CustomerName):
    
    # Simply, you are summing the total for a given CustomerName. 
    # Write an SQL statement that SELECTs From the OrderDetail table and joins with the Customer and Product table.
    # Pull out the following columns. 
    # Name -- concatenation of FirstName and LastName
    # Total -- which is calculated from multiplying ProductUnitPrice with QuantityOrdered -- sum first and then round to two decimal places
    # HINT: USE customer_to_customerid_dict to map customer name to customer id and then use where clause with CustomerID
    
    ### BEGIN SOLUTION
    sql_statement =  """ SELECT FirstName || " " || LastName as Name, 
    Round(Sum(ProductUnitPrice * QuantityOrdered), 2) as Total 
    FROM (SELECT * FROM Customer JOIN OrderDetail ON Customer.CustomerID = OrderDetail.CustomerID) as 
    order_customer JOIN Product ON order_customer.ProductID = Product.ProductId 
    WHERE Name = '{}' GROUP BY Name """.format(CustomerName)
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex3(conn):
    
    # Simply, find the total for all the customers
    # Write an SQL statement that SELECTs From the OrderDetail table and joins with the Customer and Product table.
    # Pull out the following columns. 
    # Name -- concatenation of FirstName and LastName
    # Total -- which is calculated from multiplying ProductUnitPrice with QuantityOrdered -- sum first and then round to two decimal places
    # ORDER BY Total Descending 
    ### BEGIN SOLUTION
    sql_statement =  """ SELECT FirstName || " " || LastName as Name, 
    Round(Sum(ProductUnitPrice * QuantityOrdered), 2) as Total 
    FROM (SELECT * FROM Customer JOIN OrderDetail ON Customer.CustomerID = OrderDetail.CustomerID) as 
    order_customer JOIN Product ON order_customer.ProductID = Product.ProductId 
    GROUP BY Name ORDER BY Total DESC"""
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex4(conn):
    
    # Simply, find the total for all the region
    # Write an SQL statement that SELECTs From the OrderDetail table and joins with the Customer, Product, Country, and 
    # Region tables.
    # Pull out the following columns. 
    # Region
    # Total -- which is calculated from multiplying ProductUnitPrice with QuantityOrdered -- sum first and then round to two decimal places
    # ORDER BY Total Descending 
    ### BEGIN SOLUTION

    sql_statement = """ 
        SELECT Region.Region, Round(Sum(ProductUnitPrice * QuantityOrdered), 2) as Total FROM  Customer 
        INNER JOIN OrderDetail ON Customer.CustomerID = OrderDetail.CustomerID  
        INNER JOIN Product ON OrderDetail.ProductID = Product.ProductId
        INNER JOIN Country ON Customer.CountryID = Country.CountryID
        INNER JOIN Region ON Country.RegionID = Region.RegionID 
        GROUP BY Region.Region
        ORDER BY Total 
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex5(conn):
    
     # Simply, find the total for all the countries
    # Write an SQL statement that SELECTs From the OrderDetail table and joins with the Customer, Product, and Country table.
    # Pull out the following columns. 
    # Country
    # CountryTotal -- which is calculated from multiplying ProductUnitPrice with QuantityOrdered -- sum first and then round
    # ORDER BY Total Descending 
    ### BEGIN SOLUTION

    sql_statement = """
        SELECT Country.Country, Round(Sum(ProductUnitPrice * QuantityOrdered)) as CountryTotal FROM  Customer 
        INNER JOIN OrderDetail ON Customer.CustomerID = OrderDetail.CustomerID  
        INNER JOIN Product ON OrderDetail.ProductID = Product.ProductId
        INNER JOIN Country ON Customer.CountryID = Country.CountryID
        GROUP BY Country.country
        ORDER BY CountryTotal DESC
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement


def ex6(conn):
    
    # Rank the countries within a region based on order total
    # Output Columns: Region, Country, CountryTotal, CountryRegionalRank
    # Hint: Round the the total
    # Hint: Sort ASC by Region
    ### BEGIN SOLUTION

    sql_statement = """
        SELECT Region.Region, Country.Country, Round(Sum(ProductUnitPrice * QuantityOrdered)) As CountryTotal, 
        rank() OVER (PARTITION BY Region.Region ORDER BY Round(Sum(ProductUnitPrice * QuantityOrdered)) DESC) CountryRegionalRank
        FROM  Customer 
        INNER JOIN OrderDetail ON Customer.CustomerID = OrderDetail.CustomerID  
        INNER JOIN Product ON OrderDetail.ProductID = Product.ProductId
        INNER JOIN Country ON Customer.CountryID = Country.CountryID
        INNER JOIN Region ON Country.RegionID = Region.RegionID
        GROUP BY Country.country      
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement



def ex7(conn):
    
   # Rank the countries within a region based on order total, BUT only select the TOP country, meaning rank = 1!
    # Output Columns: Region, Country, CountryTotal, CountryRegionalRank
    # Hint: Round the the total
    # Hint: Sort ASC by Region
    # HINT: Use "WITH"
    ### BEGIN SOLUTION

    sql_statement = """
      
            WITH CRRank As(
            SELECT Region.Region, Country.Country, Round(Sum(ProductUnitPrice * QuantityOrdered)) As CountryTotal, 
            rank() OVER (PARTITION BY Region.Region ORDER BY Round(Sum(ProductUnitPrice * QuantityOrdered)) DESC) CountryRegionalRank
            FROM  Customer 
            INNER JOIN OrderDetail ON Customer.CustomerID = OrderDetail.CustomerID  
            INNER JOIN Product ON OrderDetail.ProductID = Product.ProductId
            INNER JOIN Country ON Customer.CountryID = Country.CountryID
            INNER JOIN Region ON Country.RegionID = Region.RegionID
            GROUP BY Country.country)
        SELECT * FROM CRRank WHERE CountryRegionalRank = 1
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex8(conn):
    
    # Sum customer sales by Quarter and year
    # Output Columns: Quarter,Year,CustomerID,Total
    # HINT: Use "WITH"
    # Hint: Round the the total
    # HINT: YOU MUST CAST YEAR TO TYPE INTEGER!!!!
    ### BEGIN SOLUTION

    sql_statement = """
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
        INNER JOIN Country ON Customer.CountryID = Country.CountryID
        INNER JOIN Region ON Country.RegionID = Region.RegionID 
        GROUP BY Quarter, Year, Customer.CustomerID
        ORDER BY Year 
        
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex9(conn):
    
    # Rank the customer sales by Quarter and year, but only select the top 5 customers!
    # Output Columns: Quarter, Year, CustomerID, Total
    # HINT: Use "WITH"
    # Hint: Round the the total
    # HINT: YOU MUST CAST YEAR TO TYPE INTEGER!!!!
    # HINT: You can have multiple CTE tables;
    # WITH table1 AS (), table2 AS ()
    ### BEGIN SOLUTION

    sql_statement = """
                    
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex10(conn):
    
    # Rank the monthly sales
    # Output Columns: Quarter, Year, CustomerID, Total
    # HINT: Use "WITH"
    # Hint: Round the the total
    ### BEGIN SOLUTION

    sql_statement = """
      
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex11(conn):
    
    # Find the MaxDaysWithoutOrder for each customer 
    # Output Columns: 
    # CustomerID,
    # FirstName,
    # LastName,
    # Country,
    # OrderDate, 
    # PreviousOrderDate,
    # MaxDaysWithoutOrder
    # order by MaxDaysWithoutOrder desc
    # HINT: Use "WITH"; I created two CTE tables
    # HINT: Use Lag

    ### BEGIN SOLUTION

    sql_statement = """
     
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement