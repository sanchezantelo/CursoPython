import requests


r=requests.get("https://www.dolarsi.com/api/api.php?type=cotizador")
api = r.json()
dolart=api[0]["casa"]["venta"]
print("Dolar desde la plataforma: ", dolart)
dolar=dolart.replace(",",".")
dolar=float(dolar)

dolars= dolar * 1.3

print("El dolar solidario vale: ",round(dolars,2))