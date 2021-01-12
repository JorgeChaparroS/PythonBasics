import requests

def esmoneda(cripto):
    return cripto in monedas

monedas=()
monedas_dict={}

COINMARKET_API_KEY = "f7ce32a1-3cf2-4857-9be8-d76a3d72ee9d"
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
}

data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()
for cripto in data["data"]:
    monedas_dict[cripto["symbol"]]=cripto["name"]

monedas = monedas_dict.keys()

moneda=input("Indique el nombre de la moneda a verificar: ")
while not esmoneda(moneda):
        print("Moneda Invalida.")
        moneda=input("Ingrese el nombre de la moneda: ")
else:
    print("La moneda con symbol:",moneda,"y nombre:",monedas_dict.get(moneda),
          "es valida porque existe en coimnmarketcap.com")
