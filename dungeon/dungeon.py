import random
import time
import keyboard
import os



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

def narrate(name, line, verbose=True):
    os.system('cls' if os.name == 'nt' else 'clear')
    temp = line
    if verbose == True:
        temp = f"{name}: " + line
    print(temp)



print("welcome to revenge of the gosling")
print("press the up button to start introduction. down to go to next screen")
while keyboard.read_key() != "up": 
    os.system('cls' if os.name == 'nt' else 'clear') 
    print("press the up button to start introduction. down to go to next screen")
f = open("introduction.txt")
s = f.readlines()
line = 1
narrate("narrator", s[0], verbose=True)

while(line < len(s)):
    if(len(s[line]) > 5):
        while keyboard.read_key() != "down": 
            narrate("narrator", s[line-1], verbose=False)
        narrate("narrator", s[line], verbose=False)
        time.sleep(0.2)
    line += 1












