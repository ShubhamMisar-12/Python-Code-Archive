import unittest
import pandas as pd
import assignment5
import sqlite3
from gradescope_utils.autograder_utils.decorators import (number, visibility,
                                                          weight)


class TestAssignment5(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        assignment5.normalize_database('non_normalized.db')
        cls.conn_normalized = sqlite3.connect("normalized.db")
        cls.conn_orders = sqlite3.connect("orders.db")

    def setUp(self):
        self.assignment5 = assignment5
              
    @weight(3)
    @visibility('visible')
    @number("ex1")
    def test_ex1(self):
        sql_statement = self.assignment5.ex1()
        data = pd.read_csv("ex1.csv")        
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

    @weight(3)
    @visibility('visible')
    @number("ex2")
    def test_ex2(self):
        sql_statement = self.assignment5.ex2()
        data = pd.read_csv("ex2.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)


    @weight(3)
    @visibility('visible')
    @number("ex3")
    def test_ex3(self):
        sql_statement = self.assignment5.ex3()
        data = pd.read_csv("ex3.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

    @weight(3)
    @visibility('visible')
    @number("ex4")
    def test_ex4(self):
        sql_statement = self.assignment5.ex4()
        data = pd.read_csv("ex4.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

    @weight(3)
    @visibility('visible')
    @number("ex5")
    def test_ex5(self):
        sql_statement = self.assignment5.ex5()
        data = pd.read_csv("ex5.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

    @weight(3)
    @visibility('visible')
    @number("ex6")
    def test_ex6(self):
        sql_statement = self.assignment5.ex6()
        data = pd.read_csv("ex6.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)


    @weight(3)
    @visibility('visible')
    @number("ex7")
    def test_ex7(self):
        sql_statement = self.assignment5.ex7()
        data = pd.read_csv("ex7.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

    @weight(3)
    @visibility('visible')
    @number("ex8")
    def test_ex8(self):
        sql_statement = self.assignment5.ex8()
        data = pd.read_csv("ex8.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

    @weight(3)
    @visibility('visible')
    @number("ex9")
    def test_ex9(self):
        sql_statement = self.assignment5.ex9()
        data = pd.read_csv("ex9.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

    @weight(3)
    @visibility('visible')
    @number("ex10")
    def test_ex10(self):
        sql_statement = self.assignment5.ex10()
        data = pd.read_csv("ex10.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

   
    @weight(3)
    @visibility('visible')
    @number("ex11")
    def test_ex11(self):
        sql_statement = self.assignment5.ex11()
        data = pd.read_csv("ex11.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

   
    @weight(3)
    @visibility('visible')
    @number("ex12")
    def test_ex12(self):
        sql_statement = self.assignment5.ex12()
        data = pd.read_csv("ex12.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

   
   
    @weight(3)
    @visibility('visible')
    @number("ex13")
    def test_ex13(self):
        sql_statement = self.assignment5.ex13()
        data = pd.read_csv("ex13.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

   
    @weight(3)
    @visibility('visible')
    @number("ex14")
    def test_ex14(self):
        sql_statement = self.assignment5.ex14()
        data = pd.read_csv("ex14.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)


    @weight(3)
    @visibility('visible')
    @number("ex15")
    def test_ex15(self):
        sql_statement = self.assignment5.ex15()
        data = pd.read_csv("ex15.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

   
    @weight(3)
    @visibility('visible')
    @number("ex16")
    def test_ex16(self):
        sql_statement = self.assignment5.ex16()
        data = pd.read_csv("ex16.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

   
    @weight(3)
    @visibility('visible')
    @number("ex17")
    def test_ex17(self):
        sql_statement = self.assignment5.ex17()
        data = pd.read_csv("ex17.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

   
    @weight(3)
    @visibility('visible')
    @number("ex18")
    def test_ex18(self):
        sql_statement = self.assignment5.ex18()
        data = pd.read_csv("ex18.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

   
    @weight(3)
    @visibility('visible')
    @number("ex19")
    def test_ex19(self):
        sql_statement = self.assignment5.ex19()
        data = pd.read_csv("ex19.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

    @weight(3)
    @visibility('visible')
    @number("ex20")
    def test_ex20(self):
        sql_statement = self.assignment5.ex20()
        data = pd.read_csv("ex20.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

    @weight(3)
    @visibility('visible')
    @number("ex21")
    def test_ex21(self):
        sql_statement = self.assignment5.ex21()
        data = pd.read_csv("ex21.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

    @weight(3)
    @visibility('visible')
    @number("ex22")
    def test_ex22(self):
        sql_statement = self.assignment5.ex22()
        data = pd.read_csv("ex22.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

     
    @weight(3)
    @visibility('visible')
    @number("ex22")
    def test_ex22(self):
        sql_statement = self.assignment5.ex22()
        data = pd.read_csv("ex22.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)


    @weight(3)
    @visibility('visible')
    @number("ex23")
    def test_ex23(self):
        sql_statement = self.assignment5.ex23()
        data = pd.read_csv("ex23.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

    @weight(3)
    @visibility('visible')
    @number("ex24")
    def test_ex24(self):
        sql_statement = self.assignment5.ex24()
        data = pd.read_csv("ex24.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

    @weight(3)
    @visibility('visible')
    @number("ex25")
    def test_ex25(self):
        sql_statement = self.assignment5.ex25()
        data = pd.read_csv("ex25.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)

    @weight(3)
    @visibility('visible')
    @number("ex26")
    def test_ex26(self):
        sql_statement = self.assignment5.ex26()
        data = pd.read_csv("ex26.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)


    @weight(3)
    @visibility('visible')
    @number("ex27")
    def test_ex27(self):
        sql_statement = self.assignment5.ex27()
        data = pd.read_csv("ex27.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)
   
           
    @weight(3)
    @visibility('visible')
    @number("ex28")
    def test_ex28(self):
        sql_statement = self.assignment5.ex28()
        data = pd.read_csv("ex28.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)
   

    @weight(3)
    @visibility('visible')
    @number("ex29")
    def test_ex29(self):
        sql_statement = self.assignment5.ex29()
        data = pd.read_csv("ex29.csv") 
        df = pd.read_sql_query(sql_statement, self.conn_orders)
        self.assertEqual(df.equals(data), True)
   

    @weight(6)
    @visibility('visible')
    @number("ex30")
    def test_ex30(self):           
        sql_statement = self.assignment5.ex30(self.conn_normalized)
        df = pd.read_sql_query(sql_statement, self.conn_normalized)
        data = pd.read_csv("ex30.csv")
        self.assertEqual(df.equals(data), True)

    @weight(6)
    @visibility('visible')
    @number("ex31")
    def test_ex31(self):           
        sql_statement = self.assignment5.ex31(self.conn_normalized)
        df = pd.read_sql_query(sql_statement, self.conn_normalized)
        data = pd.read_csv("ex31.csv")
        self.assertEqual(df.equals(data), True)

    @weight(6)
    @visibility('visible')
    @number("ex32")
    def test_ex32(self):         
        sql_statement = self.assignment5.ex32(self.conn_normalized)
        df = pd.read_sql_query(sql_statement, self.conn_normalized)
        data = pd.read_csv("ex32.csv")
        self.assertEqual(df.equals(data), True)

    @weight(6)
    @visibility('visible')
    @number("ex33")
    def test_ex33(self):            
        sql_statement = self.assignment5.ex33(self.conn_normalized)
        df = pd.read_sql_query(sql_statement, self.conn_normalized)
        data = pd.read_csv("ex33.csv")
        self.assertEqual(df.equals(data), True)

    @weight(6)
    @visibility('visible')
    @number("ex34")
    def test_ex34(self):         
        sql_statement = self.assignment5.ex34(self.conn_normalized)
        df = pd.read_sql_query(sql_statement, self.conn_normalized)
        data = pd.read_csv("ex34.csv")
        self.assertEqual(df.equals(data), True)

    @weight(6)
    @visibility('visible')
    @number("ex35")
    def test_ex35(self):          
        sql_statement = self.assignment5.ex35(self.conn_normalized)
        df = pd.read_sql_query(sql_statement, self.conn_normalized)
        data = pd.read_csv("ex35.csv")
        self.assertEqual(df.equals(data), True)