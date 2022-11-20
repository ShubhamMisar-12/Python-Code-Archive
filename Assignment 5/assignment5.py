import pandas as pd
import sqlite3
from sqlite3 import Error

conn_orders = sqlite3.connect("orders.db")
cur = conn_orders.cursor()


# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from customers;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from orders;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from vendors;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from products;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# print(df.columns)

#sql_statement = "select * from orderitems;"
#df = pd.read_sql_query(sql_statement, conn_orders)
#print(df)

# sql_statement = "select * from productnotes;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)


def ex1():
    # Write an SQL statement that SELECTs all rows from the `customers` table
    # output columns: cust_name, cust_email

    ### BEGIN SOLUTION
    sql_statement = "SELECT cust_name, cust_email FROM customers"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex2():
    # Write an SQL statement that SELECTs all rows from the `products` table
    # output columns: vend_id

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id FROM products"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex3():
    # Write an SQL statement that SELECTs distinct rows for vend_id from the `products` table
    # output columns: vend_id

    ### BEGIN SOLUTION
    sql_statement = "SELECT DISTINCT vend_id FROM products"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex4():
    # Write an SQL statement that SELECTs the first five rows from the `products` table
    # output columns: prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_name FROM products LIMIT 5"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex5():
    # Write an SQL statement that SELECTs 4 rows starting from row 3 from `products` table
    # output columns: prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_name FROM products LIMIT 4 OFFSET 3"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex6():
    # Write an SQL statement that SELECTs all rows from `products` table and sorts by prod_name
    # output columns: prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_name FROM products ORDER BY prod_name"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex7():
    # Write an SQL statement that SELECTs all rows from `products` table and sorts by prod_price and then prod_name 
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products ORDER BY prod_price, prod_name"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex8():
    # Write an SQL statement that SELECTs all rows from `products` table and sorts by prod_price (descending order)
    # and then prod_name 
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products ORDER by prod_price DESC, prod_name"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex9():
    # Write an SQL statement that SELECTs all rows from `products` table where the price of product is 2.50
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products WHERE prod_price = 2.50"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex10():
    # Write an SQL statement that SELECTs all rows from `products` table where the name of product is Oil can
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products WHERE prod_name = 'Oil can' "
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex11():
    # Write an SQL statement that SELECTs all rows from `products` table where the price of product is 
    # less than or equal to 10
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products WHERE prod_price <= 10" 
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex12():
    # Write an SQL statement that SELECTs all rows from `products` table where the vendor id is not equal to 1003
    # output columns: vend_id, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id, prod_name FROM products WHERE vend_id != 1003"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex13():
    # Write an SQL statement that SELECTs all rows from `products` table where the product prices are between 5 and 10
    # output columns: prod_name, prod_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_name, prod_price FROM products WHERE prod_price BETWEEN 5 AND 10"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex14():
    # Write an SQL statement that SELECTs all rows from the `customers` table where the customer email is empty
    # output columns: cust_id, cust_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT cust_id, cust_name FROM customers WHERE cust_email IS NULL"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex15():
    # Write an SQL statement that SELECTs all rows from the `products` table where the vender id is 1003 and
    # the price is less than or equal to 10. 
    # output columns: vend_id, prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id, prod_id, prod_price, prod_name FROM products WHERE vend_id = 1003 AND prod_price <= 10"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex16():
    # Write an SQL statement that SELECTs all rows from the `products` table where the vender id is 1002 or 1003 and
    # the price is greater than or equal to 5. 
    # output columns: vend_id, prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id, prod_id, prod_price, prod_name FROM products WHERE vend_id IN (1002,1003) AND prod_price >= 5"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex17():
    # Write an SQL statement that SELECTs all rows from the `products` table where the vender id is 1002 or 1003 or 1005.
    # Use the IN operator for this!
    # output columns: vend_id, prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id, prod_id, prod_price, prod_name FROM products WHERE vend_id IN (1002, 1003, 1005)"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex18():
    # Write an SQL statement that SELECTs all rows from the `products` table where the vender id is NOT 1002 or 1003.
    # Use the NOT IN operator for this!
    # output columns: vend_id, prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id, prod_id, prod_price, prod_name FROM products WHERE vend_id NOT IN (1002, 1003)"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex19():
    # Write an SQL statement that SELECTs all rows from the `products` table where the product name starts with 'jet'
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products WHERE prod_name LIKE 'jet%' "
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex20():
    # Write an SQL statement that SELECTs all rows from the `products` table where the product name ends with 'anvil'
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products WHERE prod_name LIKE '%anvil'"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex21():
    # Write an SQL statement that SELECTs all rows from the `vendors` table. Concatenate vendor name and vendor country
    # as vend_title. Order by vend_title. Leave space in between -- example `ACME (USA)`
    # output columns: vend_title

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_name|| ' ' || '(' || vend_country || ')' AS vend_title FROM vendors ORDER BY vend_title"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex22():
    # Write an SQL statement that SELECTs all rows from the `orderitems` table where order number is 20005. 
    # Display an extra calculated column called `expanded_price` that is the result of quantity multiplied by item_price.
    # Round the value to two decimal places. 
    # output columns: prod_id, quantity, item_price, expanded_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, quantity, item_price, ROUND(quantity * item_price,2) AS expanded_price FROM orderitems WHERE order_num = 20005"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex23():
    # Write an SQL statement that SELECTs all rows from the `orders` table where the order date is between 
    # 2005-09-13 and 2005-10-04
    # output columns: order_num, order_date
    # https://www.sqlitetutorial.net/sqlite-date-functions/sqlite-date-function/
    
    ### BEGIN SOLUTION
    sql_statement = "SELECT order_num, order_date FROM orders WHERE order_date BETWEEN DATE('2005-09-13') AND DATE('2005-10-04')"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex24():
    # Write an SQL statement that calculates the average price of all rows in the `products` table. 
    # Call the average column avg_price
    # output columns: avg_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT AVG(prod_price) AS avg_price FROM products"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex25():
    # Write an SQL statement that calculates the average price of all rows in the `products` table 
    # where the vendor id is 1003 . Call the average column avg_price
    # output columns: avg_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT AVG(prod_price) AS avg_price FROM products WHERE vend_id =1003"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement



def ex26():
    # Write an SQL statement that counts the number of customers in the `customers` table 
    # Call the count column num_cust
    # output columns: num_cust

    ### BEGIN SOLUTION
    sql_statement = "SELECT COUNT(*) AS num_cust FROM customers"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex27():
    # Write an SQL statement that calculates the max price in the `products` table 
    # Call the max column max_price. Round the value to two decimal places. 
    # output columns: max_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT ROUND(MAX(prod_price),2) AS max_price FROM products"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex28():
    # Write an SQL statement that calculates the min price in the `products` table 
    # Call the min column min_price. Round the value to two decimal places. 
    # output columns: min_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT ROUND(MIN(prod_price), 2) AS min_price FROM products"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex29():
    # Write an SQL statement that sums the quantity in the `orderitems` table where order number is 20005. 
    # Call the sum column items_ordered
    # output columns: items_ordered

    ### BEGIN SOLUTION
    sql_statement = "SELECT SUM(quantity) AS items_ordered FROM orderitems WHERE order_num = 20005"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


#---------------------------------------------------------------------------------------------------------------------------------------------#

# You cannot use Pandas! I will deduct points after manual check if you use Pandas. You CANNOT use the 'csv' module to read the file

# Hint: Ensure to strip all strings so there is no space in them

# DO NOT use StudentID from the non_normalized table. Let the normalized table automatically handle StudentID. 


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


def create_table(conn, create_table_sql):
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

def insert_Exams(conn, values):
    try:    
        sql = ''' INSERT INTO Exams(Exam, Year)
                VALUES(?,?) '''
        cur = conn.cursor()
        cur.execute(sql, values)
        return cur.lastrowid
    except:
        return None

def insert_degrees(conn, values):
    try:
        sql = ''' INSERT INTO Degrees(Degree)
                VALUES(?) '''
        cur = conn.cursor()
        cur.execute(sql, values)
        return cur.lastrowid
    except:
        return None

def insert_StudentExamScores(conn, values):
    try:    
        sql = ''' INSERT INTO StudentExamScores(PK, StudentID, Exam, Score)
                VALUES(?, ?, ?, ?) '''
        cur = conn.cursor()
        cur.execute(sql, values)
        return cur.lastrowid
    except:
        return None

def insert_Students(conn, values):
    try:    
        sql = ''' INSERT INTO Students(StudentID, First_Name, Last_Name, Degree)
                VALUES(?, ?, ?, ?) '''
        cur = conn.cursor()
        cur.execute(sql, values)
        return cur.lastrowid
    except:
        return None
# conn_non_normalized = create_connection('non_normalized.db')
# sql_statement = "select * from Students;"
# df = pd.read_sql_query(sql_statement, conn_non_normalized)
# display(df)


def normalize_database(non_normalized_db_filename):
#     Normalize 'non_normalized.db'
#     Call the normalized database 'normalized.db'
#     Function Output: No outputs
#     Requirements:
#     Create four tables
#     Degrees table has one column:
#         [Degree] column is the primary key
    
#     Exams table has two columns:
#         [Exam] column is the primary key column
#         [Year] column stores the exam year
    
#     Students table has four columns:
#         [StudentID] primary key column 
#         [First_Name] stores first name
#         [Last_Name] stores last name
#         [Degree] foreign key to Degrees table
        
#     StudentExamScores table has four columns:
#         [PK] primary key column,
#         [StudentID] foreign key to Students table,
#         [Exam] foreign key to Exams table ,
#         [Score] exam score

    
    ### BEGIN SOLUTION


    conn_non_normalized = create_connection('non_normalized.db')

    sql_statement = "SELECT DISTINCT Degree FROM students"
    degrees = execute_sql_statement(sql_statement, conn_non_normalized)
    degrees = list(map(lambda row: row[0], degrees))

    sql_statement = "SELECT Exams, scores FROM students"
    exams_scores = execute_sql_statement(sql_statement, conn_non_normalized)
    exam_year = {}
    score_by_exam = []
    for ex in exams_scores:
        dic1 = dict(map(lambda x: (x.strip().split(" ")[0], int(x.strip().split(" ")[1][1:-1])), ex[0].split(",")))
        lst2 = list(map(lambda x: int(x.strip().split(" ")[0]), ex[1].split(",")))
        lst_exams = list(map(lambda x: x.strip().split(" ")[0], ex[0].split(",")))
        score_exam = list(zip(lst_exams,lst2))
        score_by_exam.append(score_exam)
        for key in dic1.keys():
            if key not in exam_year:
                exam_year[key] = dic1[key]
    
    
    ## Exams Table

    conn_norm = create_connection('normalized.db')
 
    create_table_sql = """CREATE TABLE IF NOT EXISTS [Exams] (
        [Exam] TEXT NOT NULL PRIMARY KEY,
        [Year] INTEGER NOT NULL
    );
    """
   
    create_table(conn_norm, create_table_sql)


    ## Insert into Exams Table

    with conn_norm:
        for exam, year in exam_year.items():
            insert_Exams(conn_norm, (exam, year))


    ## Degree Table

    create_table_sql = """CREATE TABLE IF NOT EXISTS [Degrees] (
    [Degree] TEXT NOT NULL PRIMARY KEY
    );
    """

    create_table(conn_norm, create_table_sql)


    ## Inserting into Degreee
    with conn_norm:
        for d in degrees:
            insert_degrees(conn_norm, (d, ))
            

    
    ## Students

    create_table_sql = """CREATE TABLE IF NOT EXISTS [Students] (
    [StudentID] INTEGER NOT NULL PRIMARY KEY,
    [First_Name] INTEGER NOT NULL, 
    [Last_Name] TEXT NOT NULL,
    [Degree] TEXT NOT NULL,
    FOREIGN KEY(Degree) REFERENCES Degrees(Degree)
    );
    """
    conn_norm = create_connection('normalized.db')
    create_table(conn_norm, create_table_sql)


    ## Inserting into students

    with conn_norm:
        sql_statement = "SELECT studentID,name, Degree FROM Students"
        ID_name_degree = execute_sql_statement(sql_statement, conn_non_normalized)
        names = list(map(lambda x: x[1].split(","), ID_name_degree))
        for i in range(len(names)):
            insert_Students(conn_norm, (ID_name_degree[i][0],names[i][0].strip(),names[i][1].strip(),ID_name_degree[i][2]))

    ## StudentExamScores

    create_table_sql = """CREATE TABLE IF NOT EXISTS [StudentExamScores] (
    [PK] INTEGER NOT NULL PRIMARY KEY,
    [StudentID] INTEGER NOT NULL, 
    [Exam] TEXT NOT NULL,
    [Score] INTEGER NOT NULL,
    FOREIGN KEY(Exam) REFERENCES Exams(Exam)
    );
    """
    
    create_table(conn_norm, create_table_sql)


    ## Inserting StudentExamScores insert_StudentExamScores(conn_norm,(count,i+1,exam,score))
    with conn_norm:
        count = 1
        for i in range(len(score_by_exam)):
            for se in score_by_exam[i]:
                insert_StudentExamScores(conn_norm,(count,i+1,se[0],se[1]))
                count = count + 1

    conn_non_normalized.close()

    
    ### END SOLUTION
        

# normalize_database('non_normalized.db')
# conn_normalized = create_connection('normalized.db')

def ex30(conn):
    # Write an SQL statement that SELECTs all rows from the `Exams` table and sort the exams by Year
    # output columns: exam, year
    
    ### BEGIN SOLUTION
    sql_statement = "SELECT Exam, Year FROM Exams ORDER BY Year, Exam"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement


def ex31(conn):
    # Write an SQL statement that SELECTs all rows from the `Degrees` table and sort the degrees by name
    # output columns: degree
    
    ### BEGIN SOLUTION
    sql_statement = "SELECT Degree FROM Degrees ORDER BY Degree"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement


def ex32(conn):
    # Write an SQL statement that counts the numbers of gradate and undergraduate students
    # output columns: degree, count_degree
    
    ### BEGIN SOLUTION
    sql_statement = "SELECT Degree, count(*) as count_degree FROM Students GROUP BY Degree"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement


def ex33(conn):
    # Write an SQL statement that calculates the exam averages for exams; sort by average in descending order.
    # output columns: exam, year, average
    # round to two decimal places
    
    
    ### BEGIN SOLUTION
    sql_statement = "SELECT StudentExamScores.Exam, Exams.Year, ROUND(AVG(StudentExamScores.score),2) as average FROM StudentExamScores JOIN Exams  ON StudentExamScores.Exam = Exams.Exam GROUP BY StudentExamScores.Exam ORDER BY average DESC"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement


def ex34(conn):
    # Write an SQL statement that calculates the exam averages for degrees; sort by average in descending order.
    # output columns: degree, average 
    # round to two decimal places
    
    ### BEGIN SOLUTION
    sql_statement = "SELECT Students.Degree, ROUND(AVG(StudentExamScores.score),2) as average FROM StudentExamScores JOIN Students  ON StudentExamScores.StudentID = Students.StudentID GROUP BY Students.Degree"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement

def ex35(conn):
    # Write an SQL statement that calculates the exam averages for students; sort by average in descending order. Show only top 10 students
    # output columns: first_name, last_name, degree, average
    # round to two decimal places
    # Order by average in descending order
    # Warning two of the students have the same average!!!
    
    ### BEGIN SOLUTION
    sql_statement = "SELECT Students.Last_Name as First_Name, Students.First_Name as Last_Name, Students.Degree, ROUND(AVG(StudentExamScores.score),2) as average FROM StudentExamScores JOIN Students  ON StudentExamScores.StudentID = Students.StudentID GROUP BY StudentExamScores.StudentID ORDER BY average DESC LIMIT 10"
    ### END SOLUTION 
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement
