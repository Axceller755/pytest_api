import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '73e63b4892d6cb2c8d764f1c7c7b9af5'
HEADER = {'Content_type': 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name": "generate",
    "photo_id": 1
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)

print(response_create.text)

body_putname = {
    "pokemon_id": "350384",
    "name": "Алекс",
    "photo_id": 5
}

response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_putname)

print(response_put.text)

body_pokeball = {
    "pokemon_id": "350384"
}

response_inpokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_putname)

print(response_inpokeball.text)