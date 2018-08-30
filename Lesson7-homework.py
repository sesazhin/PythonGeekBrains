import random

class Card:

    def __init__(self):
        self.loto_dict = {1: {}, 2: {}, 3: {}}
        self.num_left = 15

        for row in range(1, 4):
            keys = random.sample(range(1, 10), k=5)
            vals = random.sample(range(1, 91), k=5)
            self.loto_dict[row] = {key: value for key, value in zip(keys, vals)}

        print(self.loto_dict)

            #return self.loto_dict

    def print_card(self):
        for row in range(1, 4):

            positions = list(self.loto_dict[row].keys())
            positions.sort()

            for column in range(1, 10):
                if column in positions:
                    print(str(self.loto_dict[row][column]).rjust(2, ' '), end='')
                else:
                    print("zz", end='')
            print("")

    def check_num_exists(self, num):
        for row in range(1, 4):
            if num in self.loto_dict[row].values():
                return 1
            else:
                return 0

    def cross_number(self, num):
        print("Executed 'cross_number' function")
        for row in range(1, 4):
            if num in self.loto_dict[row].values():
                new_vals = [val if val != num else "-" for val in self.loto_dict[row].values()]
                keys = self.loto_dict[row].keys()
                self.loto_dict[row] = {key: value for key, value in zip(keys, new_vals)}
                print("replaced {} with '-' in row {}".format(num,row))

    def decrease_num_left(self):
        self.num_left -= 1

    def get_num_left(self):
        return self.num_left

class player():
    def __init__(self):
        self.card = Card()
        self.lost = 0
        self.win = 0

class User(player):
    pass

class Computer(player):
    pass

class Game():
    total_rounds_num = 90

    def __init__(self):
        self.User_player = User()
        self.Computer_player = Computer()

        self.card_player = self.User_player.card
        self.card_comp = self.Computer_player.card

        self.rounds_num = 1

        #player_result = 1

    def play(self):
        while not self.User_player.win and not self.User_player.lost and not self.Computer_player.win:
            self.game_round()

    def check_player(self,action):
        if action == 1 and self.card_player.check_num_exists(self.bar):
            self.card_player.cross_number(self.bar)
            self.card_player.decrease_num_left()

            if self.card_player.get_num_left() == 0:
                self.User_player.win = 1

            self.card_player.print_card()
            return 1  # ok, continue

        elif action == 2 and not self.card_player.check_num_exists(self.bar):
            return 1  # ok, continue

        else:
            self.User_player.lost = 1
            return 0  # player lost

    def check_comp(self):
        if self.card_comp.check_num_exists(self.bar):
            self.card_comp.cross_number(self.bar)
            self.card_comp.decrease_num_left()

            if self.card_comp.get_num_left() == 0:
                self.Computer_player.win = 1

            #self.card_player.print_card()

    def game_round(self):
        self.gen_bar()
        print("\nНовый бочонок: {} (осталось {})".format(self.bar,Game.total_rounds_num - self.rounds_num))
        print("exists = ", self.card_player.check_num_exists(self.bar))

        print("------ Ваша карточка -----")
        self.card_player.print_card()

        print("--------------------------")

        print("-- Карточка компьютера ---")
        self.card_comp.print_card()
        print("--------------------------")


        action = self.get_action()

        self.check_player(action)
        self.check_comp()
        self.rounds_num -= 1

    def gen_bar(self):
        self.bar = random.randrange(1, 91)

    def get_action(self):

        try:
            action = "0"
            while int(action) not in [1,2]:
                action = input("\nВведите действие, которое Вы хотели бы выполнить:\n1. Эта цифра есть на Вашей карточке? Зачеркнуть?\n2. Этой цифры нет на Вашей карточке? Продолжить?\n")
                    #1 - cross
                    #2 - continue

                if int(action) not in [1, 2]:
                    print("ERROR: Game:get_action()>> incorrect number  input (not 1 or 2)")

            return int(action)

        except ValueError:
            print("Value input is not of type _int_")

game_lotto = Game()
game_lotto.play()