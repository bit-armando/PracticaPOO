from sympy import re


class Adopcion:
    __dateAdopcion = str
    __cost = float
    __idEmploy = int
    __idClient = int
    __idPayment = int

    def __init__(self,date=None,cost=None, idEmploy=None, idClient=None, idPayment=None):
        """Constructor\n
        date = str, cost = float, idEmploy = int, idClient = int"""
        self.__dateAdopcion = date
        self.__cost = cost
        self.__idEmploy = idEmploy
        self.__idClient = idClient
        self.__idPayment = idPayment
    
    def setDate(self, date):
        self.__date = date
    
    def getDate(self):
        return self.__date
    
    def setCost(self, cost):
        self.__cost = cost
    
    def getCost(self):
        return self.__cost
    
    def setIdEmploy(self,idEmploy):
        self.__idEmploy = idEmploy
    
    def getIdEmploy(self):
        return self.__idEmploy

    def setIdPayment(self,idPayment):
        self.__idPayment = idPayment
    
    def getIdPayment(self):
        return self.__idPayment

    def setIdClient(self,idClient):
        self.__idClient = idClient
    
    def getIdClient(self):
        return self.__idClient