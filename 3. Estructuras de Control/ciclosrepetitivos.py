i = 0
while i < 2: 
    cantidad = int(input("Ingrese la cantidad de criptomoneda que tiene: "))
    valor = int(input("Ingrese el equivalente en dólares de la criptomoneda: "))
    acumulado = cantidad * valor
    print("Usted tiene $US ",acumulado)
    i += 1
