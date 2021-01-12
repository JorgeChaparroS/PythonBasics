class Criptomoneda(object):
    def __init__(self,nombre,saldo,cotizacion):  #Esto es como el constructor. 
        self.nombre = nombre
        self.saldo = saldo
        self.cotizacion = cotizacion

    def indicarNombre(self,nombre): #Esto es como el setter para nombre
        self.nombre = nombre
    
    def indicarSaldo(self,saldo): #Esto es como el setter para nombre
        self.saldo = saldo
    
    def indicarCotizacion(self,cotizacion): #Esto es como el setter para nombre
        self.cotizacion = cotizacion

    def mostrarNombre(self): #Esto es como el getter
        return self.nombre

    def mostrarSaldo(self): #Esto es como el getter
        return self.saldo

    def mostrarCotizacion(self): #Esto es como el getter
        return self.cotizacion

    def calcularSaldo(self,moneda): #Esto es como cualquier otro método. 
        if moneda == "USD": 
            return self.saldo * self.cotizacion
        else: 
            return self.saldo

#Asi instancian objetos de la clase creada. 
Bitcoin = Criptomoneda("Bitcoin",0.234,6435.321)
Ethereum = Criptomoneda("Ethereum",0.6734,467.563)
print(Bitcoin.mostrarNombre())
print(Ethereum.mostrarSaldo())
print(Bitcoin.calcularSaldo("USD"))

    