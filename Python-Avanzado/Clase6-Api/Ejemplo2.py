import requests

r = requests.get("https://www.dolarsi.com/api/api.php?type=cotizador")
#print(r.json())
ejemplo=r.json()

dolart= ejemplo[0]["casa"]["venta"]
dolart= dolart.replace(",",".")
dolar= float(dolart)
print(type(dolar))
print(round(dolar*1.3,2))
