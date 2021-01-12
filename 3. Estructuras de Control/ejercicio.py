criptomonedas = ["Moneda1","Moneda2","Moneda3"]
posesion = 0.0
conteo = 1
while conteo < 4: 
    nombre = input("Ingrese el nombre de la criptomoneda: ")
    if nombre in criptomonedas:
        cantidad = float(input("Ingrese la cantidad de que posee: "))
        valor = float(input("Ingrese la valorización de la criptomoneda: "))
        posesion += cantidad * valor 
        conteo += 1
    else: 
        print("Esta no es una criptomoneda válida")

print("El monto total según sus criptomonedas es de",posesion)