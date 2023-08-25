import requests
nombre = "Saul"
r = requests.get('https://api.agify.io/',params={'name': f'{nombre}', "country_id":"SV"})
datos = r.json()
print(datos)