nombre1 = input("Cuál es el nombre de la primer criptomoneda? ")
cantidad1 = int(input("Ingrese la cantidad de la criptomoneda: "))

nombre2 = input("Cuál es el nombre de la segunda criptomoneda? ")
cantidad2 = int(input("Ingrese la cantidad de la criptomoneda: "))

nombre3 = input("Cuál es el nombre de la tercera criptomoneda? ")
cantidad3 = int(input("Ingrese la cantidad de la criptomoneda: "))

if cantidad1 > cantidad2 and cantidad1 > cantidad3: 
    print(nombre1 + " con una cantidad de " + str(cantidad1))
    if cantidad2 > cantidad3:         
        print(nombre2 + " con una cantidad de " + str(cantidad2))
        print(nombre3 + " con una cantidad de " + str(cantidad3))
    else: 
        print(nombre3 + " con una cantidad de " + str(cantidad3))
        print(nombre2 + " con una cantidad de " + str(cantidad2))

elif cantidad2 > cantidad1 and cantidad2 > cantidad3: 
    print(nombre2 + " con una cantidad de " + str(cantidad2))
    if cantidad1 > cantidad3:         
        print(nombre1 + " con una cantidad de " + str(cantidad1))
        print(nombre3 + " con una cantidad de " + str(cantidad3))
    else: 
        print(nombre3 + " con una cantidad de " + str(cantidad3))
        print(nombre1 + " con una cantidad de " + str(cantidad1))

else: 
    print(nombre3 + " con una cantidad de " + str(cantidad3))
    if cantidad1 > cantidad2:         
        print(nombre1 + " con una cantidad de " + str(cantidad1))
        print(nombre2 + " con una cantidad de " + str(cantidad2))
    else: 
        print(nombre2 + " con una cantidad de " + str(cantidad2))
        print(nombre1 + " con una cantidad de " + str(cantidad1))
