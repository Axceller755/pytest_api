import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '73e63b4892d6cb2c8d764f1c7c7b9af5'
HEADER = {'Content_type': 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '36316'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
    assert response.status_code == 200