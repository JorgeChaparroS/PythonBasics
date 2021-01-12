i = 0
nombre = []
cantidad = []
valor = []
while i < 5:
    nombre.append(input("Ingrese el nombre de la criptomoneda " + str(i + 1) + ": "))
    cantidad.append(float(input("Ingrese la cantidad de " + nombre[i] + ": ")))
    valor.append(float(input("Ingrese la cotización actual de " + nombre[i] + ": ")))
    i+=1

i = 0 
while i < 5: 
    print("Criptomoneda:",nombre[i],"Cantidad:",cantidad[i],"Cotización:",valor[i])
    i+=1