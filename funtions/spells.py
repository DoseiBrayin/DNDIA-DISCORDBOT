import random as rd
import urllib.request
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv('API_DND')

def spell_dice(name,level:int=0):
    spell = []
    url = API_URL + f'/spells/{name}'
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    parsed_data = json.loads(data)
    spell_name = parsed_data['damage']['damage_type']['name']
    for key,value in parsed_data['damage']['damage_at_slot_level'].items():
        if level == 0:
            spell_dice = list(parsed_data['damage']['damage_at_slot_level'].values())[0]
        elif key == str(level):
            spell_dice = value
    spell.append(spell_name)
    spell.append(spell_dice)
    return spell