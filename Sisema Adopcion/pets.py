class Pets:
    __age = int
    __sex = str
    __color = str
    __race = str

    def __init__(self, age, sex, color, race):
        """Construct\n
        age = int, sex = str, color = str, race = str
        """
        self.__age = age
        self.__sex = sex
        self.__color = color
        self.__race = race
    
    def setAge(self, age):
        self.__age = age
    
    def getAge(self):
        return self.__age
    
    def setColor(self, color):
        self.__color = color
    
    def getColor(self):
        return self.__color

    def setRace(self, race):
        self.__race = race
    
    def getRace(self):
        return self.__race
    
    def setSex(self, sex):
        self.__sex = sex
    
    def getSex(self):
        return self.__sex