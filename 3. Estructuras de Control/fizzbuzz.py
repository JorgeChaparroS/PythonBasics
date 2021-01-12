numero = int(input("Ingrese el número que desea comprobar: "))
if numero % 5 == 0 and numero % 3 == 0: 
    print("FizzBuzz")
elif numero % 5 == 0: 
    print("Buzz")
elif numero % 3 == 0: 
    print("Fizz")
else: 
    print(numero)