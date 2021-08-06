from typing import List


class Hyperplane:
    """
    Class for working out multiple regression / hyperplane.
    i.e.:
    y = a + b1x1 + b2x2 + b3x3
    """
    def __init__(self,a:float,bxArr:List[List[float]]):
        """
        Args:
        - a - intercept
        - bxArr - List of [b,x] pairs i.e. [[b1,x1],[b2,x2],[b3,x3]]:
            - b (slope coefficient) and 
            - x - the associated x value
        """
        self.a = a
        self.bxArr = bxArr

    # Multiple regression
    # y = a + b1x1 + b2x2 + b3x3 
    def y(self):
        """
        Multiple regression
        y = a + b1x1 + b2x2 + b3x3 
        """
        sumBX = 0
        for bx in self.bxArr:
            b = bx[0]
            x = bx[1]
            sumBX += (b*x)

        y = self.a + sumBX
        return y
        


        