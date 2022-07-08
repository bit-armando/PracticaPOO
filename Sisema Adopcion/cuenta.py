class Cuenta:
    __name = str
    __document = str
    __phoneNumber = str
    __id = int
    def __init__(self, name, document):
        """Constructor\n
            name = str, document = str
        """
        self.__name = name
        self.__document = document
    
    def set_phone_number(self,phoneNumber):
        self.__phoneNumber = phoneNumber

    def get_phone_number(self):
        return self.__phoneNumber
    
    def setname(self,name):
        if name != self.__name:
            self.__name = name
        else:
            print("Elije otro nombre que no sea el que estes usando")
    
    def getName(self):
        return self.__name
    
    def setDocument(self,document):
        self.__document = document
    
    def getDocument(self):
        return self.__document

    def setId(self,id):
        self.__id = id

    def getId(self):
        return self.__id