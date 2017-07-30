import random


class Enemy:
    hp = 100
    strength = 0
    oppStrength = 0
    numPot = 2
    dodgeChance = 0
    heavyChance = 0

    def attack(self):
        self.strength = random.randrange(10, 20)

    def heavy(self):
        self.heavyChance = random.randrange(3)
        if self.heavyChance > 1:
            self.strength = 40
        else:
            self.strength = 0
            print("The enemy's heavy attack has missed!")

    def damage(self):
        self.hp -= self.oppStrength

    def dodge(self):
        self.dodgeChance = random.randrange(4)  # increase range to make success more likely
        if self.dodgeChance == 2:
            self.hp -= self.oppStrength
            print("The enemy has failed to dodge.")
            print("You dealt {} damage".format(self.oppStrength))
        elif self.dodgeChance == 1:
            self.hp -= int(round(self.oppStrength / 3))
            print("The enemy braced themselves for impact.")
            print("You dealt {} damage".format(int(round(self.oppStrength / 3))))
        else:
            print("The enemy has dodged your attack.")


class Hero:
    hp = 100
    chance = 0
    strength = 0
    oppStrength = 0
    numPot = 2

    def attack(self):
        self.strength = random.randrange(10, 20)

    def heavy(self):
        chance = random.randrange(3)
        if chance > 1:
            self.strength = 40
        else:
            self.strength = 0

    def damage(self):
        self.hp -= self.oppStrength

    def dodge(self):
        chance = random.randrange(4)  # increase range to make success more likely
        if chance == 2:
            self.hp -= self.oppStrength
            print("You have failed to dodge the enemy's attack.")
            print("You have taken {} damage".format(self.oppStrength))
        elif chance == 1:
            self.hp -= (int(round(self.oppStrength / 3)))
            print("You have braced yourself for impact.")
            print("dodge..You have taken {}".format(int(round(self.oppStrength / 3))))
        else:
            print("You have dodged the incoming attack!")


class HeroActions:
    def attack(self):
        hero.attack()
        enemy.oppStrength = hero.strength
        enemy.damage()
        print("You dealt {} damage".format(hero.strength))

    def dodge(self):
        hero.oppStrength = enemy.strength
        hero.dodge()

    def heavy(self):
        hero.heavy()
        Enemy.oppStrength = hero.strength
        enemy.damage()
        if hero.strength > 0:
            print("You dealt {} damage".format(hero.strength))
        else:
            print('Your heavy attack has missed')

    def potion(self):
        recovery = 100 - hero.hp
        if hero.hp <= 50 and hero.numPot >= 1:
            hero.hp += 50
            hero.numPot -= 1
            print("You drank a potion to recover {} HP!".format(recovery))
        elif hero.hp > 50 and hero.numPot >= 1:
            hero.hp = 100
            hero.numPot -= 1
            print("You drank a potion to recover {} HP!".format(recovery))
        else:
            print("You are out of potions.")


class EnemyActions:
    def attack(self):
        enemy.attack()
        hero.oppStrength = enemy.strength
        hero.damage()
        print("You have taken {} damage".format(enemy.strength))

    def dodge(self):
        enemy.oppStrength = hero.strength
        enemy.dodge()

    def heavy(self):
        enemy.heavy()
        hero.oppStrength = enemy.strength
        hero.damage()
        if enemy.strength > 0:
            print("You have taken {} damage".format(enemy.strength))

    def potion(self):
        recovery = 100 - enemy.hp
        if enemy.hp <= 50 and enemy.numPot >= 1:
            enemy.hp += 50
            enemy.numPot -= 1
            print("The enemy drank a potion to recover {} HP!".format(recovery))
        elif enemy.hp > 50 and enemy.numPot >= 1:
            enemy.hp = 100
            enemy.numPot -= 1
            print("The enemy drank a potion to recover {} HP!".format(recovery))
        else:
            print("The enemy is out of potions.")


enemy = Enemy()
hero = Hero()
HeroActions = HeroActions()
EnemyActions = EnemyActions()


def enemy_hp():
    print("Enemy HP: {}/100".format(enemy.hp))


def hero_hp():
    print("Your HP: {}/100".format(hero.hp))


def user_input():
    action = input()
    return action


def enemy_input():
    num = random.randrange(100)
    return num


def enemy_decision(action, num):
    if num < 50:
        if action != "d" and action != "D":
            EnemyActions.attack()
    elif 50 <= num < 76:
        if action != "d" and action != "D":
            EnemyActions.heavy()
    elif num >= 86:
        if enemy.hp <= 80 and enemy.numPot > 0:
            EnemyActions.potion()
        elif enemy.hp > 80:
            if action != "d" and action != "D":
                EnemyActions.attack()
    return num


def take_action(action, num):
    print(".\n.\n.")
    if action == "a" or action == "A":
        if 76 <= num < 86:
            hero.attack()
            EnemyActions.dodge()
        else:
            HeroActions.attack()
    elif action == "h" or action == "H":
        if 76 <= num < 86:
            hero.heavy()
            if hero.chance > 1:
                EnemyActions.dodge()
            else:
                print("Your heavy attack has missed..")
        else:
            HeroActions.heavy()
    elif action == "d" or action == "D":
        if num < 50 or (num >= 86 and enemy.hp > 80):
            enemy.attack()
            HeroActions.dodge()
        if 50 <= num < 76:
            enemy.heavy()
            if enemy.heavyChance > 1:
                HeroActions.dodge()
            else:
                print("It seems you didn't need to dodge that attack.")
    elif action == "p" or action == "P":
        HeroActions.potion()
    else:
        print("Nothing Happens...")
    return action

def healthbar():
    print("[////////////////////]          [////////////////////]")

def menu():
    print("\nYour HP: {}/100                Enemy HP: {}/100".format(hero.hp, enemy.hp))
    healthbar()
    print("\nWhat would you like to do..?")
    print("(a) = attack            (d) = dodge")
    print("(h) = heavy attack      (p) = potion")


def results():
    if hero.hp <= 0 < enemy.hp:
        print("You have been defeated..\n\nGAME OVER")
    if enemy.hp <= 0 < hero.hp:
        print("Congratulations you have defeated the enemy!!")


while enemy.hp > 0 and hero.hp > 0:
    menu()
    num = enemy_input()
    action = user_input()
    if hero.hp > 0:
        if enemy.hp < 0:
            results()
        else:
            take_action(action, num)
    if enemy.hp > 0:
        if hero.hp < 0:
            results()
        else:
            enemy_decision(action, num)
    print("______________________________________________________")

