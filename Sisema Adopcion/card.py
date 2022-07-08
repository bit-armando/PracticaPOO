from payment import Payment

class Card(Payment):
    __cvv = int
    __date = str
    def __init__(self,id, cvv, date):
        """Construct\n
        id = int, cvv = int, date = str"""
        super().__init__(id)
        self.__date = date
        self.__cvv = cvv
    
    def setCvv(self, cvv):
        self.__cvv = cvv
    
    def getCvv(self):
        return self.__cvv
    
    def setDate(self, date):
        self.__date = date
    
    def getDate(self):
        return self.__date