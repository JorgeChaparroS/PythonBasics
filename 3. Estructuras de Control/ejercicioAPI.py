import requests
_ENDPOINT = "https://api.binance.com"

def esMoneda(criptomoneda): 
    criptomonedas = ["BTC", "BCC", "LTC", "ETH", "ETC", "XRP"]
    if criptomoneda in criptomonedas: 
        return True
    else: 
        return False

def consultar(criptomoneda): 
    return requests.get(_ENDPOINT+"/api/v3/ticker/price?symbol="+criptomoneda)

moneda = ""
while not esMoneda(moneda): 
    moneda = input("Ingrese el nombre de la criptomoneda: ")

informacion = consultar(moneda+"USDT").json()
print("El precio de",moneda,"es",informacion["price"])

