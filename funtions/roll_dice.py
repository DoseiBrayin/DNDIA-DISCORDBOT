import random as rd
def roll(dice:str):
    rolled = rd.randint(1, 20)
    return [rolled,rolled+int(dice)]
