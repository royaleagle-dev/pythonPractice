#Text based Adventure Game
#version 1.0
import time

gameName = "Jumanji"
playerProfile = {}

def setUser(name, age, weapon):
    playerName=name
    playerAge=age
    playerWeapon=weapon
    while type(weapon) != 'list':
        weapon = list(input("Please input at least 2 weapons for this user"))
    else:
        return (playerName, playerAge, playerWeapon)

def availableWeapons():
    availableWeapons = {1:'gun', 2:'knife', 3:'sword', 4:'martial arts'}
    selectorHelper1(availableWeapons)   
    choose = input("Please choose at least 2 weapons by its number e.g 3,4")
    weapons = choose.split(',')
    length = len(weapons)
    weaponsList = []
    count = 0
    while count < length:
        weapon = weapons[count]
        weaponsList.append(availableWeapons[int(weapon)])
        count+=1
    return weaponsList

def availableEnviron():
    availableEnvironment = {1:"City", 2:"Ruins", 3:"Desert", 4:"Wilderness"}
    selectorHelper1(availableEnvironment)
    choose = int(input("Please Input An Environment"))
    return availableEnvironment[choose]

def selectorHelper1(dictItem):
    for key, value in dictItem.items():
        print (key, value)

def chooseGender():
    gender = input("Please choose a gender: (M)ale, (F)emale?")
    if gender.lower() == 'm':
        gender = 'Male'
    elif gender.lower() == 'f':
        gender = 'Female'
    else:
        gender = 'None'
    return gender
    
def mainGame():
    print(f'Welcome to {gameName}')
    name = input("Please Input your Name\n")
    age = int(input("Please input your Age\n"))
    weapons = availableWeapons()
    print (f"You have selected the following weapons: {weapons}\n")
    environment = availableEnviron()
    print ("You have selected the environment: {0}".format(environment))
    gender = chooseGender()
    print(f"You have chosen to be a: {gender}")
    playerProfile['name'] = name
    playerProfile['age'] = age
    playerProfile['weapons']=weapons
    playerProfile['environment'] = environment
    playerProfile['gender'] = gender
    print ("Building User Profile")
    time.sleep(5)
    print(playerProfile)


def dersertGame(name):
    print f"Welcome to the Desert {name}, Your adventure begins here"
    #Desert game play goes here
    


mainGame()
