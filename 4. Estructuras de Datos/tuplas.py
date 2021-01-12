valid_alpha_user = "qwerrtyuiuiopasdfghjkllñzxcvbnmQWERRTYUIIOOPAASDFGHJKLÑZXCVBNM1234567890-_."

while True: 
    user = input("Ingrese el nombre de usuario: ")
    if len(user) > 4:
        a = set(valid_alpha_user) #Estoy creando un conjunto "a" con todos los elementos en la variable
        b = set(user) #Estoy creando un conjunto "b" con todos los elementos en la variable "user"
        if len(b-a) > 0: #Si algún caracter de "b" no pertenece a "a", arroja false.  
            print("No es un código de usuario válido")
            continue
        else:
            print("Usuario válido") 
            break
    else: 
        print("Usuario no válido")
        
