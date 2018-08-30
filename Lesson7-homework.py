import random

class Card:

    def __init__(self):
        self.loto_dict = {1: {}, 2: {}, 3: {}}
        self.num_left = 15

        for row in range(1, 4):
            keys = random.sample(range(1, 10), k=5)
            vals = random.sample(range(1, 91), k=5)
            self.loto_dict[row] = {key: value for key, value in zip(keys, vals)}

        #print(self.loto_dict)

            #return self.loto_dict

    # def __str__(self):
    #
    #     str = ""
    #
    #     for row in range(1, 4):
    #
    #         positions = list(self.loto_dict[row].keys())
    #         positions.sort()
    #
    #         for column in range(1, 10):
    #             if column in positions:
    #                 print(str(self.loto_dict[row][column]).rjust(2, ' '), end='  ')
    #             else:
    #                 print("  ", end='')
    #         print("")

    def __str__(self):

        string_to_print = ""

        for row in range(1, 4):
            positions = list(self.loto_dict[row].keys())
            positions.sort()

            for column in range(1, 10):
                if column in positions:
                    string_to_print += str(self.loto_dict[row][column]).rjust(2, ' ') + "  "

                else:
                    string_to_print += "  "

            string_to_print += "\n"

        return string_to_print

    def check_num_exists(self, num):

        flag = 0

        for row in range(1, 4):
            if num in self.loto_dict[row].values():
                #print("number {} found in: {}. row = {}".format(num,self.loto_dict[row].values(),row))
                flag = 1
            #else:
                #print("number {} not found in: {}. row = {}".format(num, self.loto_dict[row].values(),row))

        return flag

    def cross_number(self, num, obj_str):
        #print("Executed 'cross_number' function")

        crossed_numbers = 0

        for row in range(1, 4):
            if num in self.loto_dict[row].values():
                new_vals = [val if val != num else "-" for val in self.loto_dict[row].values()]
                keys = self.loto_dict[row].keys()
                self.loto_dict[row] = {key: value for key, value in zip(keys, new_vals)}
                #print("replaced {} with '-' in row {}, Type of Obj: {}".format(num,row,obj_str))
                crossed_numbers += 1

        return crossed_numbers

    def decrease_num_left(self, num):
        for _ in range(0, num):
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

        self.bar_values = random.sample(range(1, 91), k=90)

        #print(self.bar_values)

        self.bar_values.sort()
        #print(self.bar_values)

        #player_result = 1

    def play(self):
        while not self.User_player.win and not self.User_player.lost and not self.Computer_player.win:
            self.game_round()

        if self.User_player.win:
            #print("Поздравляем, вы победили компьютер!")
            #self.player_wins += 1
            #print("Player won times: ",self.player_wins)
            return 1

        if self.User_player.lost or self.Computer_player.win:
            #print("Вы проиграли компьютеру. Попробуйте ещё раз")
            #self.comp_wins += 1
            #print("Computer won times: ",self.comp_wins)
            return 2

    def check_player(self,action):
        if action == 1 and self.card_player.check_num_exists(self.bar):
            crossed_numbers = self.card_player.cross_number(self.bar,"player")
            self.card_player.decrease_num_left(crossed_numbers)

            if self.card_player.get_num_left() == 0:
                self.User_player.win = 1

            print(self.card_player)
            return 1  # ok, continue

        elif action == 2 and not self.card_player.check_num_exists(self.bar):
            return 1  # ok, continue

        else:
            self.User_player.lost = 1
            return 0  # player lost

    def check_comp(self):
        if self.card_comp.check_num_exists(self.bar):
            crossed_numbers = self.card_comp.cross_number(self.bar,"computer")
            self.card_comp.decrease_num_left(crossed_numbers)

            #print("self.card_comp.get_num_left() = ", self.card_comp.get_num_left())

            if self.card_comp.get_num_left() == 0:
                self.Computer_player.win = 1

    def check_player_test(self):
        if self.card_player.check_num_exists(self.bar):
            crossed_numbers = self.card_player.cross_number(self.bar,"player")
            self.card_player.decrease_num_left(crossed_numbers)
            #print("self.card_player.get_num_left() = ",self.card_player.get_num_left())

            if self.card_player.get_num_left() == 0:
                self.User_player.win = 1

    def game_round(self):
        self.gen_bar()

        # print("\nНовый бочонок: {} (осталось {}, debug = {})".format(self.bar,Game.total_rounds_num - self.rounds_num,self.rounds_num))
        #
        # print("------ Ваша карточка -----")
        # print("<1  2  3  4  5  6  7  8  9>")
        # print(self.card_player)
        #
        # print("--------------------------")
        #
        # print("-- Карточка компьютера ---")
        # print("<1  2  3  4  5  6  7  8  9>")
        # print(self.card_comp)
        # print("--------------------------")
        #
        # print("exists = ", self.card_player.check_num_exists(self.bar))

        #action = self.get_action()
        #self.check_player(action)

        self.check_player_test()
        self.check_comp()
        self.rounds_num += 1

        #print("self.User_player.win = ",self.User_player.win)
        #print("self.Computer_player.win = ",self.Computer_player.win)


    def gen_bar(self):
        self.bar = self.bar_values[self.rounds_num-1]

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

try:
    user_won = 0
    comp_won = 0

    while 1:
        game_lotto = Game()
        result = game_lotto.play()

        if result == 1:
            user_won += 1
            print("Player won times: ", user_won)

        if result == 2:
            comp_won += 1
            print("Computer won times: ", comp_won)

except KeyboardInterrupt:
    exit(1)