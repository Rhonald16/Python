import requests
import json

#personajes

url = (f'https://rickandmortyapi.com/api/character/2')
req = requests.get(url)
res = req.json()

Name = res['name']
Status = res['status']
#print('Nombre del personaje: {}\nEstatus del personaje: {}'.format(Name, Status) )
i = 1
while i < 6:
    url = 'https://rickandmortyapi.com/api/character/{}'.format(i)
    req = requests.get(url)
    res = req.json()
    Name = res['name']
    Status = res['status']
    print('Nombre del personaje: {} Estatus del personaje: {}'.format(Name, Status) )
    i += 1


#episodio

url = ('https://rickandmortyapi.com/api/episode/1')

req = requests.get(url)
res = req.json()
personajes = res['characters']
lista_personajes = list()
lista_personajes_other = list()

for p in personajes:
    req = requests.get(p)
    js = req.json()
    name = js['name']
    if js['species'] == 'Human':
        lista_personajes.append(name)
    else:
        lista_personajes_other.append(name)

print(lista_personajes)
print(lista_personajes_other)
    

