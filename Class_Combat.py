import random


class Enemy:
    hp = 100
    strength = 0
    oppStrength = 0
    numPot = 2
    dodgeChance = 0
    heavyChance = 0
    bar = "[////////////////////]"

    def healthbar(self):
        if self.hp == 100:
            self.bar = "[////////////////////]"
        elif self.hp >= 95:
            self.bar = "[////////////////////]"
        elif self.hp >= 90:
            self.bar = "[/////////////////// ]"
        elif self.hp >= 85:
            self.bar = "[//////////////////  ]"
        elif self.hp >= 80:
            self.bar = "[/////////////////   ]"
        elif self.hp >= 75:
            self.bar = "[////////////////    ]"
        elif self.hp >= 70:
            self.bar = "[///////////////     ]"
        elif self.hp >= 65:
            self.bar = "[//////////////      ]"
        elif self.hp >= 60:
            self.bar = "[/////////////       ]"
        elif self.hp >= 55:
            self.bar = "[////////////        ]"
        elif self.hp >= 50:
            self.bar = "[///////////         ]"
        elif self.hp >= 45:
            self.bar = "[//////////          ]"
        elif self.hp >= 40:
            self.bar = "[/////////           ]"
        elif self.hp >= 35:
            self.bar = "[////////            ]"
        elif self.hp >= 30:
            self.bar = "[///////             ]"
        elif self.hp >= 25:
            self.bar = "[//////              ]"
        elif self.hp >= 20:
            self.bar = "[/////               ]"
        elif self.hp >= 15:
            self.bar = "[////                ]"
        elif self.hp >= 10:
            self.bar = "[///                 ]"
        elif self.hp <= 5:
            self.bar = "[//                  ]"
        elif self.hp > 0:
            self.bar = "[/                   ]"
        elif self.hp <= 0:
            self.bar = "[                    ]"

    def attack(self):
        self.strength = random.randrange(10, 20)

    def heavy(self):
        self.heavyChance = random.randrange(1000)
        if self.heavyChance > 599:
            self.strength = 45
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
    heavyChance = 0
    dodgeChance = 0
    strength = 0
    oppStrength = 0
    numPot = 2
    bar = "[////////////////////]"

    def healthbar(self):
        if self.hp == 100:
            self.bar = "[////////////////////]"
        elif self.hp >= 95:
            self.bar = "[////////////////////]"
        elif self.hp >= 90:
            self.bar = "[/////////////////// ]"
        elif self.hp >= 85:
            self.bar = "[//////////////////  ]"
        elif self.hp >= 80:
            self.bar = "[/////////////////   ]"
        elif self.hp >= 75:
            self.bar = "[////////////////    ]"
        elif self.hp >= 70:
            self.bar = "[///////////////     ]"
        elif self.hp >= 65:
            self.bar = "[//////////////      ]"
        elif self.hp >= 60:
            self.bar = "[/////////////       ]"
        elif self.hp >= 55:
            self.bar = "[////////////        ]"
        elif self.hp >= 50:
            self.bar = "[///////////         ]"
        elif self.hp >= 45:
            self.bar = "[//////////          ]"
        elif self.hp >= 40:
            self.bar = "[/////////           ]"
        elif self.hp >= 35:
            self.bar = "[////////            ]"
        elif self.hp >= 30:
            self.bar = "[///////             ]"
        elif self.hp >= 25:
            self.bar = "[//////              ]"
        elif self.hp >= 20:
            self.bar = "[/////               ]"
        elif self.hp >= 15:
            self.bar = "[////                ]"
        elif self.hp >= 10:
            self.bar = "[///                 ]"
        elif self.hp <= 5:
            self.bar = "[//                  ]"
        elif self.hp > 0:
            self.bar = "[/                   ]"
        elif self.hp <= 0:
            self.bar = "[                    ]"

    def attack(self):
        self.strength = random.randrange(8, 20)

    def heavy(self):
        self.heavyChance = random.randrange(1000)
        if self.heavyChance > 640:
            self.strength = 45
        else:
            self.strength = 0

    def damage(self):
        self.hp -= self.oppStrength

    def dodge(self):
        self.dodgeChance = random.randrange(4)  # increase range to make success more likely
        if self.dodgeChance == 2:
            self.hp -= self.oppStrength
            print("You have failed to dodge the enemy's attack.")
            print("You have taken {} damage".format(self.oppStrength))
        elif self.dodgeChance == 1:
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
            print("You drank a potion to recover 50 HP!".format(recovery))
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
            print("The enemy drank a potion to recover 50 HP!".format(recovery))
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


def healthbar():
    hero.healthbar()
    enemy.healthbar()


def user_input():
    heroDecision = input()
    return heroDecision


def enemy_input():
    a = 40
    b = 70
    c = 86
    enemyDecision = random.randrange(100)
    if enemyDecision < a:
        if enemy.hp < 30 and enemy.numPot >= 1:
            enemyDecision = "p"
        else:
            enemyDecision = "a"
    elif a <= enemyDecision < b:
        if enemy.hp < 30 and enemy.numPot >= 1:
            enemyDecision = "p"
        else:
            enemyDecision = "h"
    elif b <= enemyDecision < c:
        if enemy.hp < 30 and enemy.numPot >= 1:
            enemyDecision = "p"
        else:
            enemyDecision = "d"
    elif enemyDecision >= c:
        if enemy.hp < 80 and enemy.numPot > 0:
            enemyDecision = "p"
        else:

            enemyDecision = "a"
    return enemyDecision


def enemy_decision(heroDecision, enemyDecision):
    if enemyDecision is "a":
        if heroDecision != "d" and heroDecision != "D":
            EnemyActions.attack()
    elif enemyDecision is "h":
        if heroDecision != "d" and heroDecision != "D":
            EnemyActions.heavy()
    elif enemyDecision is "p":
        if heroDecision is not "a" and heroDecision is not "A" and heroDecision is not "d" and heroDecision is not "D":
            EnemyActions.potion()
    return enemyDecision


def take_action(heroDecision, enemyDecision):
    print(".\n.")
    if heroDecision == "a" or heroDecision == "A":
        if enemyDecision is "d":
            hero.attack()
            EnemyActions.dodge()
        elif enemyDecision is "p":
            if enemy.hp <= 80 and enemy.numPot > 0:
                EnemyActions.potion()
                HeroActions.attack()
        else:
            HeroActions.attack()
    elif heroDecision == "h" or heroDecision == "H":
        if enemyDecision is "d":
            hero.heavy()
            if hero.strength is not 0:
                EnemyActions.dodge()
            else:
                print("Your heavy attack has missed..")
        elif enemyDecision is "p":
            EnemyActions.potion()
            HeroActions.heavy()
        else:
            HeroActions.heavy()
    elif heroDecision == "d" or heroDecision == "D":
        if enemyDecision is "a":
            enemy.attack()
            HeroActions.dodge()
        elif enemyDecision is "h":
            enemy.heavy()
            if enemy.strength is not 0:
                HeroActions.dodge()
            else:
                print("It seems you didn't need to dodge that attack.")
        elif enemyDecision is "d":
            print("You both dodged away from nothing.. ")
    elif heroDecision == "p" or heroDecision == "P":
        HeroActions.potion()
    else:
        print("Nothing Happens...")
    return heroDecision


def menu():
    healthbar()
    print("\nYour HP: {}/100                 Enemy HP: {}/100".format(hero.hp, enemy.hp))
    print("\n{}          {}".format(hero.bar, enemy.bar))
    print("\nWhat would you like to do..?")
    print("(a) = attack            (d) = dodge")
    print("(h) = heavy attack      (p) = potion")


def results():
    if hero.hp <= 0 < enemy.hp:
        print("You have been defeated..\n\nGAME OVER")
        return 0
    elif enemy.hp <= 0 < hero.hp:
        print("Congratulations you have defeated the enemy!!")
        return 1


def main():
    while enemy.hp > 0 and hero.hp > 0:
        menu()
        enemyDecision = enemy_input()
        heroDecision = user_input()
        if hero.hp > 0:
            take_action(heroDecision, enemyDecision)
        if enemy.hp > 0:
            enemy_decision(heroDecision, enemyDecision)
        print("______________________________________________________")
    result = results()
    return result
main()


