from cat import Cat
from cliente import Client
from empleado import Empleado
from adopcion import Adopcion
from card import Card

gatito = Cat(1,"Hembra","Blanco","Persa")
cliente1 = Client("Armando Rosales","ROMA0112")
cliente1.setId(0)
empleado1 = Empleado("Roberto Gomez", "RBGZ282")
empleado1.setId(0)
pago = Card(0,235,"03/30")

documento = Adopcion("08/07/22",300,empleado1.getId(),cliente1.getId(),pago.getId())

print("El consto de un Gatito de {} años, es de {} MXN".format(gatito.getAge(),documento.getCost()))