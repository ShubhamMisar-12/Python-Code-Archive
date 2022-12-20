import unittest
import pandas as pd
import assignment7
import sqlite3
from gradescope_utils.autograder_utils.decorators import (number, visibility,
                                                          weight)


class Testassignment7(unittest.TestCase):

    def setUp(self):
        self.assignment7 = assignment7

    @weight(6)
    @visibility('visible')
    @number("step1")
    def test_step1(self):
        df_from_func = self.assignment7.step1()
        df_from_file = pd.read_csv('step1_output.csv')
        assert df_from_func.equals(df_from_file) == True

    @weight(6)
    @visibility('visible')
    @number("step2")
    def test_step2(self):
        df_from_step1 = self.assignment7.step1()
        df_from_func = self.assignment7.step2(df_from_step1)
        df_from_file = pd.read_csv('step2_output.csv')
        assert df_from_func.equals(df_from_file) == True

    @weight(6)
    @visibility('visible')
    @number("step3")
    def test_step3(self):
        df_from_step1 = self.assignment7.step1()
        df_from_step2 = self.assignment7.step2(df_from_step1)
        df_from_func = self.assignment7.step3(df_from_step2)
        df_from_file = pd.read_csv('step3_output.csv')
        assert df_from_func.equals(df_from_file) == True

    @weight(6)
    @visibility('visible')
    @number("step4")
    def test_step4(self):
        df_from_step1 = self.assignment7.step1()
        df_from_step2 = self.assignment7.step2(df_from_step1)
        df_from_step3 = self.assignment7.step3(df_from_step2)
        df_from_func = self.assignment7.step4(df_from_step3)
        df_from_file = pd.read_csv('step4_output.csv')
        df_from_file['Sex'] = df_from_file['Sex'].astype('int32')
        df_from_file['Embarked'] = df_from_file['Embarked'].astype('int32')
        df_from_func['Sex'] = df_from_file['Sex'].astype('int32')
        df_from_func['Embarked'] = df_from_file['Embarked'].astype('int32')
        assert df_from_func.equals(df_from_file) == True

    @weight(6)
    @visibility('visible')
    @number("step5")
    def test_step5(self):
        df_from_step1 = self.assignment7.step1()
        df_from_step2 = self.assignment7.step2(df_from_step1)
        df_from_step3 = self.assignment7.step3(df_from_step2)
        df_from_step4 = self.assignment7.step4(df_from_step3)
        df_from_func = self.assignment7.step5(df_from_step4)
        df_from_file = pd.read_csv('step5_output.csv', skiprows=[0], header=None)

        df_from_file.columns = ['', 1]
        df_from_file.set_index('', inplace=True)
        df_from_file.columns = ['']

        df_from_func = pd.DataFrame(df_from_func.dtypes)
        df_from_func.columns = ['']

        assert df_from_func.equals(df_from_file) == True

    @weight(6)
    @visibility('visible')
    @number("step6")
    def test_step6(self):
        df_from_step1 = self.assignment7.step1()
        df_from_step2 = self.assignment7.step2(df_from_step1)
        df_from_step3 = self.assignment7.step3(df_from_step2)
        df_from_step4 = self.assignment7.step4(df_from_step3)
        df_from_step5 = self.assignment7.step5(df_from_step4)
        accuracy, TN, FP, FN, TP = self.assignment7.step6(df_from_step5)

        assert accuracy == 0.7978
        assert TN == 90
        assert FP == 16
        assert FN == 20
        assert TP == 52
