import random
import time

def roll():
    return random.randint(1, 20)

class Character:
    def __init__(self, name="unnamed", health=10, species="HOM"):
        #BASIC INFO
        self.name = name
        self.health = health
        self.inventory = dict()
        self.species = species
        self.mana = True
        #STATS
        self.strength = roll()
        self.dexterity = roll()
        self.vitality = roll()
        self.wisdom = roll()
        self.intelligence = roll()
        self.charisma = roll()

    #HEALTH MODIFIERS
    def Punch(self,  Character):
        Character.health -= int(max(self.strength, self.dexterity)/10)
    def Rest(self):
        self.health += int(self.vitality/3)

    #SET SPECIES
    def setSpecies(self, s):
        self.species = s

    #SPECIES BOOST
    def speciesBoost(self, roll_number):
        if(self.species == "GEE"):
            self.dexterity += int(roll_number/5)
            self.charisma += int(roll_number/10)
            self.strength -= int(roll_number/10)
            self.wisdom -= int(roll_number/10)
        if(self.species == "SEA"):
            self.strength += int(roll_number/5)
            self.vitality += int(roll_number/5)
            self.dexterity -= int(roll_number/10)
            self.mana = False
        if(self.species == "MON"):
            self.strength += int(roll_number/5)
            self.health += int(self.vitality/10)
            self.dexterity -= int(roll_number/5)
    
    def finishBoost(self, roll_number):
        if(self.species == "GEE"):
            self.dexterity -= int(roll_number/5)
            self.charisma -= int(roll_number/10)
            self.strength += int(roll_number/10)
            self.wisdom += int(roll_number/10)
        if(self.species == "SEA"):
            self.strength -= int(roll_number/5)
            self.vitality -= int(roll_number/5)
            self.dexterity += int(roll_number/10)
            self.mana = False
        if(self.species == "MON"):
            self.strength -= int(roll_number/5)
            self.health -= int(self.vitality/10)
            self.dexterity += int(roll_number/5)


    #def applyEffect(s):

    #INFO
    def displayCharacter(self):
        print(f"Hello, {self.name}. Here are your stats: ")
        print(f"STRENGTH        {self.strength}")
        print(f"DEXTERITY       {self.dexterity}")
        print(f"VITALITY        {self.vitality}")
        print(f"WISDOM          {self.wisdom}")
        print(f"INTEL           {self.intelligence}")
        print(f"CHARISMA        {self.charisma}")

def narrate(name, line):
    line = f"{name}: " + line
    for i in range(len(line)-1):
        print(line[0:i], end="\r")
        time.sleep(0.01)
    print(line[0:len(line)], end="\n")
narrate("the spirit", "welcome to the void young adventurer")
time.sleep(0.5)
narrate("the spirit", "this is a land of many friends and foes.")

#EXAMPLE CODE FROM 12/15/2022

# #Test Character of type Seafolk and name lord gosling
# goose = Character(name="lord gosling", species="GEE")
# goose.displayCharacter()
# roll = roll()
# #Adjusting Attributes of Characters based on roll
# goose.speciesBoost(roll)
# goose.displayCharacter()
# #Reseting Character after the round
# goose.finishBoost(roll)
# goose.displayCharacter()










