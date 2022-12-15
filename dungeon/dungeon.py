import random

def roll():
    return random.randint(1, 20)

class Character:
    def __init__(self, name="unnamed", health=10):
        #BASIC INFO
        self.name = name
        self.health = health
        self.inventory = dict()
        self.species = "HOM"
        self.mana = True
        #STATS
        self.strength = roll()
        self.dexterity = roll()
        self.vitality = roll()
        self.wisdom = roll()
        self.intelligence = roll()
        self.charisma = roll()

    def __iter__(self):
        return self
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

    #def applyEffect(s):

    def displayCharacter(self):
        print(f"Hello, {self.name}. Here are your stats: ")
        print(f"STRENGTH        {self.strength}")
        print(f"DEXTERITY       {self.dexterity}")
        print(f"VITALITY        {self.vitality}")
        print(f"WISDOM          {self.wisdom}")
        print(f"INTEL           {self.intelligence}")
        print(f"CHARISMA        {self.charisma}")


goose = Character(name="lord gosling")
goose.displayCharacter()



