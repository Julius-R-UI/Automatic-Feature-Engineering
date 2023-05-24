import numpy as np
import pandas as pd

class create:
    def __init__(self, x, categorical_columns = []):
        self.x = x
        self.cat = categorical_columns

    def add(self):
        x_ = pd.DataFrame()
        for name in self.x.columns.tolist():
            column_names = self.x.columns.tolist()
            column_names.remove(name)
            for oth_name in column_names:
                new_col_name = "{} {} {}".format(name, '+', oth_name)
                x_[new_col_name] = x[name] + x[oth_name]
        return x_

    def multiply(self):
        x_ = pd.DataFrame()
        for name in self.x.columns.tolist():
            column_names = self.x.columns.tolist()
            column_names.remove(name)
            for oth_name in column_names:
                new_col_name = "{} {} {}".format(name, '*', oth_name)
                x_[new_col_name] = x[name] * x[oth_name]
        return x_

    def divide(self):
        x_ = pd.DataFrame()
        for name in self.x.columns.tolist():
            column_names = self.x.columns.tolist()
            column_names.remove(name)
            for oth_name in column_names:
                new_col_name = "{} {} {}".format(name, '/', oth_name)
                x_[new_col_name] = x[name] / x[oth_name]
        return x_

    def subtract(self):
        x_ = pd.DataFrame()
        for name in self.x.columns.tolist():
            column_names = self.x.columns.tolist()
            column_names.remove(name)
            for oth_name in column_names:
                new_col_name = "{} {} {}".format(name, '-', oth_name)
                x_[new_col_name] = x[name] - x[oth_name]
        return x_
    
    def log(self):
        x_ = pd.DataFrame()
        for name in self.x.columns.tolist():
            new_col_name = "log({})".format(name)
            x_[new_col_name] = np.log(x[name])
        return x_
