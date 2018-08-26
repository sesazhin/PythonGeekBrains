class Person:
    def __init__(self,name,health,damage,armor):
        self._name = name
        self._health = health
        self._damage = damage
        self._armor = armor

    # def get_health(self):
    #     return self._health

    # def getname(self):
    #     return self._name

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def damage(self):
        return self._damage

    @property
    def armor(self):
        return self._armor

    def print_init_params(self):
        print("#################################################")
        print(str(self.name) + ": Initial Health = " + str(self.health))
        print(str(self.name) + ": Damage = " + str(self.damage))
        print(str(self.name) + ": Armor = " + str(self.armor))

class Enemy(Person):
    def _calculate_damage(self, who_attack_damage, who_defend_armor):
        return who_attack_damage / who_defend_armor

    def attack(self, who_attack, who_defend):
         damage_dealt = self._calculate_damage(self,who_attack._damage, who_defend._armor)
         who_defend._health -= damage_dealt
         print('{} (Враг) нанес {} урона {}, у того осталось {} жизней.'.format(who_attack._name, who_defend._name, round(damage_dealt,2), round(who_defend._health,2)))

    def print_name_fraction(self):
        return self._name + " - Враг"

class Player(Person):
    def _calculate_damage(self, who_attack_damage, who_defend_armor):
        return who_attack_damage / who_defend_armor

    def attack(self, who_attack, who_defend):
         damage_dealt = self._calculate_damage(self,who_attack._damage, who_defend._armor)
         who_defend._health -= damage_dealt
         print('{} (Игрок) нанес {} урона {}, у того осталось {} жизней.'.format(who_attack._name, who_defend._name, round(damage_dealt,2), round(who_defend._health,2)))

    def print_name_fraction(self):
        return self._name + " - Игрок"

class game:
    def __init__(self):
        self._Enemy = Enemy("Сергей",100,50,1.4)
        self._Player = Player("Владимир",120,60,1.6)

    def start_game(self):
        print(self._Enemy.print_name_fraction())
        print(self._Player.print_name_fraction())

        self._Enemy.print_init_params()
        self._Player.print_init_params()

        last_attacker = "player"
        if last_attacker == "player":
            print("Игру начинает враг!")

        else:
            print("Игру начинает игрок!")

        while self._Player.health > 0 and self._Enemy.health > 0:
            if last_attacker == "player":
                Enemy.attack(Enemy, self._Enemy, self._Player)
                last_attacker = "enemy"
            else:
                Player.attack(Player, self._Player, self._Enemy)
                last_attacker = "player"

        if self._Player.health > 0:
            print('Игрок победил!')
        else:
            print('Враг победил!')

game().start_game()
