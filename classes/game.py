import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Character:
    def __init__(self, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic", "Use Item"]
        self.items = items
    
    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)
    
    def generate_spell_damage(self, i):
        magdmgl = self.magic[i]["dmg"] - 10
        magdmgh = self.magic[i]["dmg"] + 10
        return random.randrange(magdmgl, magdmgh)
    
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
    
    def get_hp(self):
        return self.hp
    
    def get_max_hp(self):
        return self.maxhp
    
    def get_mp(self):
        return self.mp
    
    def get_max_mp(self):
        return self.maxmp
    
    def reduce_mp(self, cost):
        self.mp -= cost
    
    def heal(self, heal):
        self.hp += heal
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_spell_name(self, i):
        return self.magic[i]["name"]
    
    def get_spell_cost(self, i):
        return self.magic[i]["cost"]
    
    def get_item_name(self, i):
        return self.items[i]["name"]
    
    def get_item_quantity(self, i):
        return self.items[i]["quantity"]
    
    def get_item_prop(self, i):
        return self.items[i]["prop"]
    
    def reduce_item_quantity(self, i):
        self.items[i]["quantity"] -= 1
    
    def choose_action(self):
        i = 1
        print("Actions")
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("Magic")
        for spell in self.magic:
            print(str(i) + ":", spell["name"], "(cost:", str(spell["cost"]) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("Items")
        for item in self.items:
            print(str(i) + ".", item["name"], ":", item["description"], "(x" + str(item["prop"]) + ")" + " (x" + str(item["quantity"]) + ")" )
            i += 1

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
            {"name": "Thunder", "cost": 15, "dmg": 80},
            {"name": "Blizzard", "cost": 10, "dmg": 60}]

items = [{"name": "Potion", "type": "health", "description": "Heals 50 HP", "prop": 50, "quantity": 5},
            {"name": "Hi-Potion", "type": "health", "description": "Heals 100 HP", "prop": 100, "quantity": 5},
            {"name": "Elixir", "type": "health", "description": "Restore HP and Mana", "prop": 999, "quantity": 1}]