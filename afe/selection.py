import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

from .creation import Simple

class Models:
    def RandomForestC(x,y,n_estimators):
        model = RandomForestClassifier(n_estimators = n_estimators)
        model.fit(x,y)
        x_ = model.feature_importances_

        return x_, model
    
class Selection:
    def 
