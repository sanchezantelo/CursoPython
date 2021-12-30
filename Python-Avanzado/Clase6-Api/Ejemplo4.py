import requests


r=requests.get("https://iol.invertironline.com/titulo/cotizacion/BCBA/GGAL/GRUPO-FINANCIERO-GALICIA-S.A/")

html = r.text

print(html.find('"UltimoPrecio"'))

inicio=54835+15
fin=54835+15+6
print(html[inicio:fin])
