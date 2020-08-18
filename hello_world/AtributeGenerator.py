import random

def generator ():
    roll1 = int( random.random() * 7 )

    roll2 = int( random.random() * 7 )

    roll3 = int( random.random() * 7 )

    roll4 = int( random.random() * 7 )

    list1 = [roll1, roll2, roll3, roll4]

    list1.sort(key=None, reverse=False)

    dropMin = list1[1:] 
    
    atr = sum(dropMin) + 1
    return atr


STR = generator()
DEX = generator()
INT = generator()
CON= generator()
WIS = generator()
CHA = generator()

print('Strength:', STR, 
'Dexterity:', DEX,
'Intelligence:', INT,
'Constitution:', CON,
'Wisdom:', WIS,
'Charisma:', CHA)