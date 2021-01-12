import random
moneda=input("Ingrese la moneda: ")
cantidad=float(input("Ingrese la cantidad de "+moneda+": "))
count=0
while count < 7:
    profit=random.uniform(-0.03,0.03) #Para generar números decimales. 
    cantidad=cantidad+(cantidad*profit)
    count=count+1
    print("Saldo de",moneda,"el dia",count,"es de: %6.7f"%cantidad+". Ganacia de %6.2f"%(profit*100),"%") #6 unidades y 7 decimales, o 6 unidades y 2 decimales.
