from numpy.linalg import inv

class LinearRegression:
    def __init__(self, X, y):
        self.X = X
        self.y = y
        
    """Calculate m (the slope) and b (the y-intercept) 
    of the line of best fit
    """   
    def fit(self):
        X = self.X
        y = self.y
        sigma = inv(X.T.dot(X)).dot(X.T).dot(y)
        m = sigma[0]
        b = sigma[1]
        return (m,b)
    