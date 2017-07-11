import random


class Enemy:
    hp = 100
    strength = 0
    oppStrength = 0
    numPot = 2

    def attack(self):
        self.strength = random.randrange(10, 20)

    def heavy(self):
        chance = random.randrange(3)
        if chance > 1:
            self.strength = 50
        else:
            self.strength = 0
            print("The enemy's heavy attack has missed!")

    def damage(self):
        self.hp -= self.oppStrength

    def dodge(self):
        chance = random.randrange(4)  # increase range to make success more likely
        if chance == 2:
            self.hp -= self.oppStrength
            print("The enemy has failed to dodge.")
        elif chance == 1:
            self.hp -= int(round(self.oppStrength / 3))
            print("The enemy braced themselves for impact.")
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
            self.strength = 50
        else:
            self.strength = 0
            print("Your heavy attack has missed!")

    def damage(self):
        self.hp -= self.oppStrength

    def dodge(self):
        chance = random.randrange(4)  # increase range to make success more likely
        if chance == 2:
            self.hp -= self.oppStrength
            print("You have failed to dodge the enemy's attack.")
            print("dodge..You have taken {} damage".format(self.oppStrength))
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
        test = True
        return test

    def dodge(self):
        hero.dodge()
        test = True
        return test

    def heavy(self):
        hero.heavy()
        Enemy.oppStrength = hero.strength
        enemy.damage()
        print("You dealt {} damage".format(hero.strength))
        test = True
        return test

    def potion(self):
        recovery = 100 - hero.hp
        if hero.hp <= 50 and hero.numPot >= 1:
            hero.hp += 50
            hero.numPot -= 1
            print("You drank a potion to recover {} HP!".format(recovery))
        elif hero.hp > 5 and hero.numPot >= 1:
            hero.hp = 100
            hero.numPot -= 1
            print("You drank a potion to recover {} HP!".format(recovery))
        else:
            print("You are out of potions.")
        test = True
        return test


class EnemyActions:
    def attack(self):
        enemy.attack()
        hero.oppStrength = enemy.strength
        hero.damage()
        print("atk act..You have taken {} damage".format(enemy.strength))
        test = True
        return test

    def dodge(self):
        enemy.dodge()
        test = True
        return test

    def heavy(self):
        enemy.heavy()
        hero.oppStrength = enemy.strength
        hero.damage()
        print("hvy act..You have taken {} damage".format(enemy.strength))
        test = True
        return test

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
            print("You are out of potions.")
        test = True
        return test


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
    if num < 50 and (action != "d" or action != "D"):
        EnemyActions.attack()
    if 50 <= num < 76:
        EnemyActions.heavy()
    if 76 <= num < 86:
        if action == "a" or action == "A":
            hero.attack()
            EnemyActions.dodge()
        if action == "d" or action == "D":
            hero.heavy()
            if hero.strength != 0:
                EnemyActions.dodge()
    if num >= 86:
        if enemy.hp <= 80 and enemy.numPot != 0:
            EnemyActions.potion()
        if enemy.hp > 80 and (action != "d" or action != "D"):
            EnemyActions.attack()
    return num


def take_action(action, num):
    print(".\n.\n.")
    test = False
    if action == "a" or action == "A":
        test = HeroActions.attack()
    if action == "h" or action == "H":
        test = HeroActions.heavy()
    if action == "d" or action == "D":
        if num < 50 or (num >= 86 and enemy.hp > 80):
            enemy.attack()
            test = HeroActions.dodge()
        if 50 <= num < 76:
            enemy.heavy()
            if enemy.strength != 0:
                test = HeroActions.dodge()
            if enemy.strength == 0:
                print("It seems you didn't need to dodge that attack.")
                test = True
    if action == "p" or action == "P":
        test = HeroActions.potion()
    if test is False:
        print("Nothing Happens...")
    return action


def menu():
    print("\n")
    enemy_hp()
    hero_hp()
    print("What would you like to do..?\n")
    print("(a) = attack            (d) = dodge")
    print("(h) = heavy attack      (p) = potion")


while enemy.hp > 0 and hero.hp > 0:
    menu()
    num = enemy_input()
    action = user_input()
    print(num, str(action))
    take_action(action, num)
    enemy_decision(action, num)
    print("_____________________________________________")
