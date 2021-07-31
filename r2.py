# Class for predicting Rsquared value
class R2:
    def __init__(self,Yactual,Ypred):
        self.Yactual = Yactual # array of actual y vaules
        self.Ypred = Ypred# array of predicted values
        
        
    
    def r2(self):
        r2 = 1 - ((self.ssReg()**2/self.ssTotal()**2))
        return r2

    def mean(self):
        temp = 0
        yMean = 0
        count = 0
        for y in self.Yactual:
            temp += y[0]
            count = count+1

        yMean = temp/count
        return yMean
    def ssTotal(self):
        yMean = self.mean()
        sum = 0
        for y in self.Yactual:
            # y[0] because dealing with 2d arrays
            sum += (y[0] - yMean)**2
        return sum

    def ssReg(self):
        i = 0
        sum = 0
        for y in self.Yactual:
            # y[0] because dealing with 2d arrays
            sum += (y - self.Ypred[i])
            i = i+1
        return sum