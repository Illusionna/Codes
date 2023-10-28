'''
# System --> Windows & Python3.8.0
# File ----> regression.py
# Author --> Illusionna
# Create --> 2023/10/24 09:19:22
'''
# -*- Encoding: UTF-8 -*-


from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression


class LINEAR_REGRESSION:
    def __init__(
            self,
            trainX:list,
            trainY:list,
            testX:list,
            testY:list,
            attribute:list
    ) -> None:
        self.trainX = trainX
        self.trainY = trainY
        self.testX = testX
        self.testY = testY
        self.attribute = attribute
        LINEAR_REGRESSION.__Regression(self)

    def __Regression(self) -> None:
        model = LinearRegression()
        model.fit(self.trainX, self.trainY)
        prediction = model.predict(self.testX)
        R2 = r2_score(self.testY, prediction)
        y = self.attribute[-1]
        coefs = model.coef_.tolist()
        string = ''
        for i in range(0, len(self.attribute)-1, 1):
            temp = self.attribute[i]
            coef = round(coefs[i], 3)
            string = string + f' + {coef}x{temp}'
        x = string[3:]
        result = y + ' = ' + x
        print('')
        print(result)
        print(f'拟合优度: {R2}')

