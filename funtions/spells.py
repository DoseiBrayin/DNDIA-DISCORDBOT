import random as rd
import urllib.request
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv('API_DND')

def spell_dice(name,level:int=0):
    url = API_URL + f'/spells/{name}'
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    parsed_data = json.loads(data)
    return parsed_data