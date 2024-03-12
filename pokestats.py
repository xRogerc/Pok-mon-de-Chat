from random import *

level = int(1)
base_life = int(randrange(40,60))
bonus_life = level * randrange(2,4)

current_xp = 0
current_life = base_life + bonus_life


mypokexp = {
    "1": 0,
    "2": 15,
    "3": 45,
    "4": 100,
    "5": 250,
    "6": 570,
    "7": 700,
    "8": 900,
    "9": 1100,
    "10": 1300,
    "11": 1500,
    "12": 1750,
    "14": 1970,
    "15": 2300,
    "16": 2660
    }

def update_exp(value: int):
    global current_xp, level
    current_xp += value
    if current_xp >= mypokexp[str(level)]:
        leftover = current_xp - mypokexp[str(level)]
        current_xp = leftover
        level += 1
        on_level_up()

def on_level_up():
    global current_life
    current_life = base_life + bonus_life

def update_healt(value: int):
    global current_life
    current_life -= value
    if current_life < 0:
        current_life = 0