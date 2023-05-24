import numpy as np

class metric:
    def R_Squared(y_true, y_pred):
        SSE = np.sum((y_true - y_pred)**2)
        SSW = np.sum((y_true - np.mean(y_true))**2)

        return 1 - SSE/SSW