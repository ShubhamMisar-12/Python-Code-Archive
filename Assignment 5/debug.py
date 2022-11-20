import pandas as pd
import sqlite3
from sqlite3 import Error
#Degrees table has one column:
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
#SELECT Students.Degree, ROUND(AVG(StudentExamScores.score),2) as average FROM StudentExamScores JOIN Students  ON StudentExamScores.StudentID = Students.StudentID GROUP BY Students.Degree


conn_norm = sqlite3.connect("normalized.db")
cur = conn_norm.cursor()
sql_statement = "SELECT Students.Last_Name as First_Name, Students.First_Name as Last_Name, Students.Degree, ROUND(AVG(StudentExamScores.score),2) as average , AVG(StudentExamScores.score) as average2 FROM StudentExamScores JOIN Students  ON StudentExamScores.StudentID = Students.StudentID GROUP BY StudentExamScores.StudentID ORDER BY average DESC LIMIT 10"
print(pd.read_sql_query(sql_statement, conn_norm))
conn_norm.close()

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

def execute_sql_statement(sql_statement, conn):
    cur = conn.cursor()
    cur.execute(sql_statement)

    rows = cur.fetchall()

    return rows


'''
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
print(score_by_exam[98])'''