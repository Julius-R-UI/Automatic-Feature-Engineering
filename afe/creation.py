import numpy as np
import pandas as pd

class Simple:
    def add(x):
        x_ = pd.DataFrame()
        for name in x.columns.tolist():
            column_names = x.columns.tolist()
            column_names.remove(name)
            for oth_name in column_names:
                new_col_name = "{} {} {}".format(name, '+', oth_name)
                x_[new_col_name] = x[name] + x[oth_name]
        return x_

    def multiply(x):
        x_ = pd.DataFrame()
        for name in x.columns.tolist():
            column_names = x.columns.tolist()
            column_names.remove(name)
            for oth_name in column_names:
                new_col_name = "{} {} {}".format(name, '*', oth_name)
                x_[new_col_name] = x[name] * x[oth_name]
        return x_

    def divide(x):
        x_ = pd.DataFrame()
        for name in x.columns.tolist():
            column_names = x.columns.tolist()
            column_names.remove(name)
            for oth_name in column_names:
                new_col_name = "{} {} {}".format(name, '/', oth_name)
                x_[new_col_name] = x[name] / x[oth_name]
        return x_

    def subtract(x):
        x_ = pd.DataFrame()
        for name in x.columns.tolist():
            column_names = x.columns.tolist()
            column_names.remove(name)
            for oth_name in column_names:
                new_col_name = "{} {} {}".format(name, '-', oth_name)
                x_[new_col_name] = x[name] - x[oth_name]
        return x_
    
    def log(x):
        x_ = pd.DataFrame()
        for name in x.columns.tolist():
            new_col_name = "log({})".format(name)
            x_[new_col_name] = np.log(x[name])
        return x_
    


