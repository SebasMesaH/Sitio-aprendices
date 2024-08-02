from urllib.request import urlopen
import json
url="https://api.nasa.gov/"
response = urlopen(url)
data= json.loads(response.read())


for i in data:
    print(i)
    break




'''
GET -> Obtener informacion
POST -> Crear informacion
PUT -> Actualizar informacion
DELETE -> eliminar informacion
'''