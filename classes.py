import random
'''
REMINDER:
In addition to completing the Warrior and Mage classes, you need to create two more classes that inherit from Character, such as:
- Archer
- Paladin
You don't have to create these EXACT classes, you have creative freedom about which additional classes to create. It doesn't have to be Archer & Paladin.

Each custom class must have two unique abilities, such as:
- Archer: "Quick Shot" (double arrow attack) and "Evade" (avoid next attack).
- Paladin: "Holy Strike" (bonus damage) and "Divine Shield" (blocks the next attack).

Additionally, you need to implement a heal() method in the base Character class.
Lastly, you need to randomize the damage done in the Character class' attack() method.
'''
# ====================== BASE CHARACTER CLASS ============================
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    '''
    Modify this function so that the character does a random amount of damage.
    Hint: Look up the randint() function from Python's random library.
    '''
    def attack(self, opponent):
        damage = self.attack_power # Change this to a random number. Hint: use random.randint()
        
        # Check if the opponent has a 'evadeNextAttack' attribute. If they do not, proceed with the attack.
        if not hasattr(opponent, 'evadeNextAttack'):
            opponent.health -= damage
            print(f"\n{self.name} attacks {opponent.name} for {damage} damage!")
        # Else, if they do have an 'evadeNextAttack' attribute and the value is False, proceed with the attack.
        elif hasattr(opponent, 'evadeNextAttack') and opponent.evadeNextAttack == False:
            opponent.health -= damage
            print(f"\n{self.name} attacks {opponent.name} for {damage} damage!")
        # Else, if they do have an 'evadeNextAttack' attribute and the value is True, set the value back to False and display that the attack was evaded.
        elif hasattr(opponent, 'evadeNextAttack') and opponent.evadeNextAttack == True:
            print(f"\n{self.name} attacks {opponent.name}, but {opponent.name} evades the attack!")
            opponent.evadeNextAttack = False
        
    # You need to implement this method still.
    def heal(self):
        heal_amount = random.randint(10, 30)
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}/{self.max_health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
       
# ============================ SUBCLASSES ================================ 

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def special_ability(self, opponent):
        print("\nAbilities:")
        print("1. Heroic Strike")
        print("2. Bleeding Wound")
        print("3. Shield Block(Evade)")
        action = input("Which ability do you want to use? ")

        if action == "1":
            '''
            Ability: Heroic Strike
            Description: A powerful melee attack that deals 40 damage.
            '''
            heroic_strike_damage = 40
            opponent.health -= heroic_strike_damage
            print(f"\n{self.name} strikes {opponent.name} heroically, dealing {heroic_strike_damage} damage.")
        elif action == "2":
            '''
            Ability: Bleeding Wound
            Description: Deals 20 damage and causes the opponent to lose 10 more health next turn.
            '''
            bleeding_wound_damage = 20
            opponent.health -= bleeding_wound_damage
            if not hasattr(opponent, 'bleeding'):
                opponent.bleeding = 0
            opponent.bleeding += 10
            print(f"\n{self.name} inflicts a bleeding wound on {opponent.name}, dealing {bleeding_wound_damage} damage and causing bleeding!")
        elif action == "3":
            '''
            Ability: Shield Block (Evade)
            Description: Blocks the next attack.
            '''
            self.evadeNextAttack = True
            print(f"\n{self.name} uses Shield Block. {self.name} will block the next attack!")    
        
# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        
    def special_ability(self, opponent):
        print("\nAbilities:")
        print("1. Fireball")
        print("2. Frost Nova")
        print("3. Ice Shield (Evade)")
        action = input("Which ability do you want to use? ")
        
        if action == "1":
            '''
            Ability: Fireball
            Description: A powerful fire attack that deals 50 damage.
            '''
            fireball_damage = 50
            opponent.health -= fireball_damage
            print(f"\nA Fireabll channels infront of {self.name} and launches at {opponent.name}, dealing {fireball_damage} damage.")
        elif action == "2":
            '''
            Ability: Frost Nova
            Description: Freezes the opponent, dealing 20 damage and reducing their next attack's damage by half.
            '''
            frost_nova_damage = 20
        
            opponent.health -= frost_nova_damage
            opponent.attack_power //= 2 # Floor division rounds to the nearest integer (whole number) 
            print(f"\n{self.name} Freezes {opponent.name} with Frost Nova dealing {frost_nova_damage} damage and reducing {opponent.name} next attack by half.")
        elif action == "3":
            '''
            Ability: Ice Shield (Evade)
            Description: Dodges the next attack.
            '''
            self.evadeNextAttack = True
            print(f"\n{self.name} uses Ice Shield. {self.name} will block the next attack!")    

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=20)
        
    def special_ability(self, opponent):
        print("\nAbilities:")
        print("1. Quick Shot")
        print("2. Poison Arrow")
        print("3. Evasive Roll (Evade)")
        action = input("Which ability do you want to use? ")
        
        if action == "1":
            '''
            Ability: Quick Shot
            Description: Fires two arrows in quick succession, each dealing 15 damage.
            '''
            quick_shot_damage = 15
            total_damage = quick_shot_damage * 2
            opponent.health -= total_damage
            print(f"\n{self.name} fires two quick arrows at {opponent.name}, dealing a total of {total_damage} damage.")
        elif action == "2":
            '''
            Ability: Poison Arrow
             Description: Deals random damage (20-30) and poisons the opponent, causing them to lose 5 health for the next two turns.
            '''
            poison_arrow_damage = random.randint(20, 30)
            opponent.health -= poison_arrow_damage
            if not hasattr(opponent, 'poison'):
                opponent.poison = 0
            opponent.poison += 5 * 2  # 5 health for the next two turns
            print(f"\n{self.name} shoots a poison arrow at {opponent.name}, dealing {poison_arrow_damage} damage and poisoning them!")
        elif action == "3":
            '''
            Ability: Evasive Roll (Evade)
            Description: Dodges the next attack.
            '''
            self.evadeNextAttack = True
            print(f"\n{self.name} uses Evasive Roll. {self.name} will dodge the next attack!")

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=20)
        
    def special_ability(self, opponent):
        print("\nAbilities:")
        print("1. Holy Strike")
        print("2. Divine Shield (Evade)")
        action = input("Which ability do you want to use? ")
        
        if action == "1":
            '''
            Ability: Holy Strike
            Ability: Holy Strike
            Description: A powerful melee attack that deals between 25 and 40 damage and heals the paladin for 10 health.
            '''
            holy_strike_damage = random.randint(25, 40)  # Random damage between 25 and 40
            opponent.health -= holy_strike_damage
            self.health += 10
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"\n{self.name} strikes {opponent.name} with a Holy Strike, dealing {holy_strike_damage} damage and healing for 10 health.")
        elif action == "2":
            '''
            Ability: Divine Shield (Evade)
            Description: Blocks the next attack.
            '''
            self.evadeNextAttack = True
            print(f"\n{self.name} uses Divine Shield. {self.name} will block the next attack!")
# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")
        
class Rogue(Character):
    def __init__(self, name):
        # Call the superclass (parent class) __init__() method and pass required data to it.
        super().__init__(name, health=120, attack_power=30)
        self.evadeNextAttack = False
        
    def special_ability(self, opponent):
        print("\nAbilities:")
        print("1. Gathering Shadows")
        print("2. Siphoning Strikes")
        print("3. Preemptive Dodge (Evade)")
        action = input("Which ability do you want to use? ")
        
        if action == "1":
            '''
            Ability: Gathering Shadows
            Description: Increases the rogue's damage by 30 but does not attack.
            '''
            self.attack_power += 30
            print(f"\nShadows gather around {self.name} increasing their damage to {self.attack_power}.")
        elif action == "2":
            '''
            Ability: Siphoning Strikes
            Description: Strikes the opponent & heals for half of the damage dealt.
            '''
            opponent.health -= self.attack_power
            self.health += self.attack_power // 2 # Floor division rounds to the nearest integer (whole number)
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"\n{self.name} strikes {opponent.name} with vampiric daggers, dealing {self.attack_power} damage and siphoning the wizard's health to {self.health} health.")
        elif action == "3":
            '''
            Ability: Preemptive Dodge (Evade)
            Description: Dodges the next attack.
            '''
            self.evadeNextAttack = True
            print(f"\n{self.name} uses Preemptive Dodge. He will dodge the next attack!")