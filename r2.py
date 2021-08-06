# Class for predicting Rsquared value
from typing import List


class R2:
    """
    Class for calculating the Rsquared value.
    Contains methods for working out the:
    - Mean of Yactual data points
    - Sum Squared Total Error (how well the mean works as an average)
    - Sum Squared Regression Error (how well the Regression works as an average)
    """
    def __init__(self,Yactual:List[List[float]],Ypred:List[List[float]]):
        """
        Args:
        - Yactual - List of actual y vaules
        - Ypred - List of predicted y values

        Note:Uses a List[List[float]] for compatability with sklearn's linear model module
        """
        self.Yactual = Yactual # array of actual y vaules
        self.Ypred = Ypred# array of predicted values
        
    def r2(self):
        """
        Calculates the Rsquared value of the data and returns it.
        """
        r2 = 1 - ((self.ssReg()/self.ssTotal()))
        return r2

    def mean(self):
        """
        Returns the mean of the Yactual data points.
        Needed for working out Sum Squared Error
        """
        temp = 0
        yMean = 0
        count = 0
        for y in self.Yactual:
            temp += y[0]
            count = count+1

        yMean = temp/count
        return yMean
    def ssTotal(self):
        """
        Calculates "Sum Squared Total Error" and returns it's values
        """
        yMean = self.mean()
        sum = 0
        for y in self.Yactual:
            # y[0] because dealing with 2d arrays
            sum += (y[0] - yMean)**2
        return sum

    def ssReg(self):
        """
        Calcualates the "Sum Square Regression Error" and returns it's value
        """
        i = 0
        sum = 0
        for y in self.Yactual:
            # y[0] because dealing with 2d arrays
            sum += (y[0] - self.Ypred[i])**2
            i = i+1
        return sum