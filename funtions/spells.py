import random as rd
import urllib.request
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv('API_DND')

def spell_dice(name,level:int=0):
    spell = [] #Declaramos un vector donde ira la informacion 

    ## Se hace la peticion a la API de DND y se guarda la informacion en un diccionario
    url = API_URL + f'/spells/{name}'
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    parsed_data = json.loads(data)
    spell_name = parsed_data['damage']['damage_type']['name']

    #Se recorre el diccionario para saber a que nivel se lanza el dado
    for key,value in parsed_data['damage']['damage_at_slot_level'].items():
        if level == 0:
            spell_dice = list(parsed_data['damage']['damage_at_slot_level'].values())[0]
        elif key == str(level):
            spell_dice = value
        else:
            spell_dice = f'Not find dice in this level {level}'
    ##Añadimos a la lista los datos que nos interesan (Nombre y dados)
    spell.append(spell_name)
    spell.append(spell_dice)
    return spell