#Importamos los módulos para utilizar las APIs y utilizar la hora y fecha. 
import requests 
from datetime import date, datetime

def esMoneda(miMoneda): #Método para verificar si lo almacenado en "miMoneda" es un código de criptomoneda válido en coinmarket. 
    monedas=()
    monedas_dict={}

    COINMARKET_API_KEY = "f7ce32a1-3cf2-4857-9be8-d76a3d72ee9d" #Mi llave, quizás deban cambiarla para probarlo desde su equipo. 
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
    }

    data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()
    for cripto in data["data"]:
        monedas_dict[cripto["symbol"]]=cripto["name"]

    monedas = monedas_dict.keys()

    return miMoneda in monedas

def getPrice(miMoneda): #Método para obtener el valor actual en USD de la criptomoneda cuyo símbolo se almacena en la variable "miMoneda" 
    if esMoneda(miMoneda): 
        _ENDPOINT = "https://api.binance.com"
        informacion = requests.get(_ENDPOINT+"/api/v3/ticker/price?symbol="+miMoneda+"USDT").json()
        return informacion["price"]

def esNumero(numero): #Método para verificar si lo que contiene la variable "numero" es un número real, entero o decimal. 
    return numero.replace('.','',1).isdigit()

def modificarFondos(criptomonedaCodigo,cantidad): #Método para modificar las cantidades de criptomonedas en mi archivo BilleteraDigital.txt
    nombre_archivo = "BilleteraDigital.txt"
    archivo = open(nombre_archivo,"r") #Abro el archivo en modo lectura. 
    texto = archivo.read() #Almaceno el contenido de mi archivo en la variable "texto"
    archivo.close()
    lineas = texto.splitlines() #Almaceno en "lineas" las líneas del archivo, en forma de arreglo. 
    arreglo = []
    conteo = 1
    cambio = False #Es una bandera que me indicará si realicé algún cambio en el archivo. 
    for linea in lineas: #Recorro todas las lineas del archivo 
        valor = 0
        componentes = linea.split(":") #El archivo está escrito de la forma codigoCriptomoneda:cantidadCriptomoneda. Entonces componentes[0] tendrá el codigo de la criptomoneda, y componentes[1] tendrá la cantidad existente
        if componentes[0] == criptomonedaCodigo: #Verifico si la criptomoneda que quiero modificar se encuentra ya en el archivo. 
            valor = float(componentes[1]) + cantidad #El nuevo valor de la criptomoneda es el que ya estaba antes mas lo que estoy agregando (valor positivo o negativo)
            arreglo.append(componentes[0]+":"+str(valor)) #Agrego a mi lista "arreglo" el par codigoCriptomoneda:cantidadCriptomoneda
            cambio = True #Indico que modifiqué una moneda ya existente. 
        else: #Si la criptomoneda que quiero cambiar no coincide con la de la iteración actual. 
            if conteo == len(lineas) and not cambio: #Verifico que llegué a la última criptomoneda almacenada y no se ha hecho ningún cambio. 
                arreglo.append(componentes[0]+":"+componentes[1]) #Agrego el par codigoCriptomoneda:cantidadCriptomoneda a la lista
                arreglo.append(criptomonedaCodigo+":"+str(cantidad)) #Agrego también la nueva criptomoneda a la lista. 
            else: #En caso de que no esté en la última criptomoneda
                arreglo.append(componentes[0]+":"+componentes[1]) #Agrego el par codigoCriptomoneda:cantidadCriptomoneda a la lista
        conteo+=1 #Esta variable me indica la posición +1 del par codigoCriptomoneda:cantidadCriptomoneda en el que me encuentro actualmente.  

    archivo = open(nombre_archivo,"w") #Abro mi archivo en modo escritura. 
    for i in arreglo: #Recorro el arreglo que llené previamente. 
        archivo.write(i+"\n") #Sobreescribo mi archivo con los pares codigoCriptomoneda:cantidadCriptomoneda que existen en el arreglo. 
    archivo.close()
    
def leerFondos(): #Método que muestra la cantidad de criptomonedas que tengo, y su total en USD. 
    nombre_archivo = "BilleteraDigital.txt"
    archivo = open(nombre_archivo,"r") #Abro el archivo de los fondos en modo lectura
    texto = archivo.read()
    archivo.close()
    lineas = texto.splitlines() #Separo el archivo según separaciones de línea. 
    valorizacion = 0.0 #Variable que almacenará el total en USD que tengo en mi billetera. 
    for linea in lineas: #Bucle hasta llegar a la última línea. 
        componentes = linea.split(":") #En componentes[0] almaceno codigoCriptomoneda y en componentes[1] cantidadCriptomoneda. 
        valorizacionMoneda = 0 #Inicializo siempre el valor para cada par. 
        valorizacionMoneda = float(getPrice(componentes[0])) * float(componentes[1]) #Llamo a la función getPrice, para calcular el precio actual de tal criptomoneda, la multiplico por la cantidad que tengo
        valorizacion += valorizacionMoneda #La voy acumulando en la variable.
        print(linea,". Valor USD:",valorizacionMoneda) #Muestro por pantalla cada una de las líneas, es decir, el par codigoCriptomoneda:cantidadCriptomoneda y su valor en USD. 
    print("Monto total de USD$",valorizacion,"\n") #Imprimo el total. 

def obtenerFondos(): #Método únicamente para obtener el valor en USD que tengo. 
    nombre_archivo = "BilleteraDigital.txt"
    archivo = open(nombre_archivo,"r") #Abro el archivo de los fondos en modo lectura
    texto = archivo.read()
    archivo.close()
    lineas = texto.splitlines() #Separo el archivo según separaciones de línea. 
    valorizacion = 0.0 #Variable que almacenará el total en USD que tengo en mi billetera. 
    for linea in lineas: #Bucle hasta llegar a la última línea. 
        componentes = linea.split(":") #En componentes[0] almaceno codigoCriptomoneda y en componentes[1] cantidadCriptomoneda. 
        valorizacion += float(getPrice(componentes[0])) * float(componentes[1]) #Llamo a la función getPrice, para calcular el precio actual de tal criptomoneda, la multiplico por la cantidad que tengo, y la voy acumulando en la variable.
    return valorizacion #Retorno mi monto en USD.  

def agregarTransferencia(criptomonedaCodigo,cantidad,codigo): #Método para agregar una transferencia al archivo de transferencias. 
    #Abro el archivo de transferencias en modo escritura
    nombre_archivo = "Transferencias.txt"
    archivo = open(nombre_archivo,"a") #Abro mi archivo en modo de escritura. 
    dx = datetime.now() #Hago llamado al módulo
    momento = dx.strftime("%d/%m/%Y a las %H:%M:%S") #Le doy formato a la fecha y la hora actual y lo almaceno en la variable. 
    #Escribo una nueva línea, con lo que contengan los parámetros
    montoActual = obtenerFondos()
    archivo.write(criptomonedaCodigo+","+str(cantidad)+","+codigo+","+momento+","+str(montoActual)+"\n") #Escribo en el archivo de las transacciones la transacción que se acaba de realizar.
    archivo.close() #Cierro el archivo. 

def leerTransferencias(): #Método para visualizar el contenido de mi archivo de transferencias. 
    nombre_archivo = "Transferencias.txt"
    archivo = open(nombre_archivo,"r") #Abro el archivo en forma de lectura. 
    texto = archivo.read() #Almaceno el contenido en la variable. 
    archivo.close()
    lineas = texto.splitlines() #Almaceno las lineas del contenido en una variable que será una lista. 
    for linea in lineas: #Recorro todos los elementos en la lista. 
        componentes = linea.split(",") #Separo los componentes que conforman cada línea, su formato es codigo,cantidad,billetera,fecha,montoActual
        if float(componentes[1]) >= 0: #Si la cantidad de la transferencia es positivo, significa que recibí la transferencia
            print("Recibió",componentes[1],componentes[0],"desde la cuenta con código",componentes[2],"el",componentes[3],". Monto actual: USD",componentes[4]) #Le doy formato a lo que mostraré
        else: #Si no es positivo, significa que yo realicé la trasnferencia. 
            print("Envió",-float(componentes[1]),componentes[0],"hacia la cuenta con código",componentes[2],"el",componentes[3],". Monto actual: USD",componentes[4]) #Le doy formato a lo que mostraré
    print("")
    
def realizarTrasnferencia(criptomonedaCodigo,cantidad,codigo): #Método para la realización de una transferencia. 
    nombre_archivo = "BilleteraDigital.txt"
    archivo = open(nombre_archivo,"r") #Abro mi archivo de fondos en modo lectura. 
    texto = archivo.read()
    archivo.close()
    lineas = texto.splitlines() 
    encontroCriptomoneda = False #Una bandera que me indica que sí poseo la criptomoneda que quiero transferir. 
    for linea in lineas: 
        componentes = linea.split(":")
        if componentes[0] == criptomonedaCodigo: #Si encuentro la criptomoneda que quiero transferir
            encontroCriptomoneda = True #Activo la bandera de que sí encontré la criptomoneda. 
            if float(componentes[1]) >= abs(cantidad): #Verifico que tenga fondos suficientes con respecto al valor que quiero transferir. 
                modificarFondos(criptomonedaCodigo,cantidad) #Llamo a la función que me permite cambiar mis fondos. 
                agregarTransferencia(criptomonedaCodigo,cantidad,codigo) #Llamo a la función que agrega la transferencia. 
                print("\nUsted ha realizado la transferencia por",abs(cantidad),criptomonedaCodigo,"a la billetera",codigo,"\n") #Imprimo un mensaje. 
            else: #En caso de no tener fondos suficientes. 
                print("No tiene fondos suficientes. No se ha podido realizar la transacción.")
    if not encontroCriptomoneda: #Se ejecuta si no encontré la criptomoneda. 
        print("Usted no cuenta con fondos de la criptomoneda",criptomonedaCodigo)

def ewallet():
    codigoPropio = "123ABC"
    print("BIENVENIDO A SU BILLETERA ELECTRÓNICA\n")
    print("Su código de billetera es",codigoPropio) #Esto es solo presentación. 
    opcion = 0
    while True: #Ingreso a un bucle "infinito" en el que se ejecuta la funcionalidad. 
        print("""Considere una de las siguientes opciones:  
            1. Ingrese '1' para recibir una cantidad. 
            2. Ingrese '2' para transferir un monto.
            3. Ingrese '3' para mostrar el balance de alguna moneda. 
            4. Ingrese '4' para mostrar el balance general en su e-wallet.
            5. Ingrese '5' para mostrar el histórico de transacciones. 
            6. Ingrese '6' para salir. 
            """) #Menu de opciones. 
        opcion = input("Ingrese alguna de las opciones(1, 2, 3, 4, 5 o 6): ") #Acá indico la opcion que quiero. 

        if opcion == "1": 
            print("+"*24+"\n+ RECIBIR UNA CANTIDAD +\n"+"+"*24)
            while True: #No salgo del while hasta ingresar un código de criptomoneda válido. 
                criptomonedaCodigo = ""
                criptomonedaCodigo = input("Ingrese el código de la criptomoneda que va a recibir: ")
                if esMoneda(criptomonedaCodigo): 
                    break
                else: 
                    print("\nEste no es código de criptomoneda válido, por favor intente nuevamente.\n")
            while True: #No salgo del while hasta indicar un valor númerico real. 
                cantidad = ""
                cantidad = input("Ingrese la cantidad que va a recibir: ")
                if esNumero(cantidad):
                    cantidad = float(cantidad)
                    break
                else: 
                    print("\nInténtelo nuevamente, con una cantidad válida.\n")
            while True: #No salgo del while hasta indicar un código de billetera distinto al mío. 
                codigo = ""
                codigo = input("Ingrese el código de la billetera de la cual está recibiendo la transferencia: ")
                if codigo == codigoPropio: 
                    print("\nUsted no puede recibir transferencias de su propia billetera. Intente nuevamente.\n")
                else: 
                    modificarFondos(criptomonedaCodigo,cantidad) #Se modifican mis fondos.
                    agregarTransferencia(criptomonedaCodigo,cantidad,codigo) #Se agrega la transferencia. 
                    print("\nUsted ha recibido la transferencia por",cantidad,criptomonedaCodigo,"desde la billetera",codigo,"\n") #Mensaje. 
                    break
            

        elif opcion == "2": 
            print("+"*23+"\n+ TRANSFERIR UN MONTO +\n"+"+"*23)
            while True: #No salgo del while hasta ingresar un código de criptomoneda válido. 
                criptomonedaCodigo = ""
                criptomonedaCodigo = input("Ingrese el código de la criptomoneda que va a transferir: ")
                if esMoneda(criptomonedaCodigo): 
                    break
                else: 
                    print("\nEste no es código de criptomoneda válido, por favor intente nuevamente.\n")
            while True: #No salgo del while hasta indicar un valor númerico real.
                cantidad = ""
                cantidad = input("Ingrese la cantidad que va a transferir: ")
                if esNumero(cantidad):
                    cantidad = -float(cantidad)
                    break
                else: 
                    print("\nInténtelo nuevamente, con una cantidad válida.\n")
            while True: #No salgo del while hasta indicar un código de billetera distinto al mío.
                codigo = ""
                codigo = input("Ingrese el código de la billetera a la que realizará la transferencia: ")
                if codigo == codigoPropio: 
                    print("\nUsted no puede realizar transferencias a su propia billetera. Intente nuevamente.\n")
                else: 
                    realizarTrasnferencia(criptomonedaCodigo,cantidad,codigo) #Realizo la transferencia. 
                    break
            
        elif opcion == "3": 
            print("+"*41+"\n+ CONSULTAR EL BALANCE DE ALGUNA MONEDA +\n"+"+"*41)
            criptomonedaCodigo = ""
            criptomonedaCodigo = input("Ingrese el código de la criptomoneda de la cual desea consultar: ")
            if esMoneda(criptomonedaCodigo): #verifico que sea un código válido. 
                print("\nEl precio de",criptomonedaCodigo,"es de $US",getPrice(criptomonedaCodigo),"\n") #Muestro el precio actual. 
            else: 
                print("\nEste no es código de criptomoneda válido, por favor intente nuevamente.\n")

        elif opcion == "4": 
            print("+"*39+"\n+ CONSULTAR EL BALANCE EN SU E-WALLET +\n"+"+"*39)
            leerFondos() #Llamo a la función que me lee los fondos en mi billetera. 

        elif opcion == "5": 
            print("+"*30+"\n+ HISTÓRICO DE TRANSACCIONES +\n"+"+"*30)
            leerTransferencias() #Llamo a la función que me lee las transacciones realizadas. 

        elif opcion == "6": 
            print("+"*56+"\n+ GRACIAS POR UTILIZAR SU E-WALLET. QUE TENGA BUEN DÍA +\n"+"+"*56) #Se cierra la aplicación. 
            break
        else: 
            print("\nEsta opción no se encuentra disponible, por favor intente de nuevo.\n")

ewallet() #Llamo a la función que me despliega el menú de opciones. 