import requests


r=requests.get("https://api.openweathermap.org/data/2.5/weather?q=Buenos%20Aires,AR&units=metric&appid=172b7c712bc4cac417008f085c75b7a3")
print(r.status_code)
api = r.json()
print(api["main"]["temp"])
print(api["main"]["pressure"])