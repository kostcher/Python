import random


class Player:
    def __init__(self, card):
        self.card = card
        self.total_removed = 0

    def search_and_delete_ceil(self, search_ceil):
        for i, row in enumerate(self.card):
            for j, card_ceil in enumerate(row):
                if card_ceil == search_ceil:
                    self.card[i][j] = 'X'
                    self.total_removed += 1
                    return True

        return False


class Loto:
    def __init__(self):
        self.player = Player(self.create_card())
        self.computer_player = Player(self.create_card())
        self.kegs = list(range(1, 91))

    @staticmethod
    def create_card():
        card = []
        row = []

        for index, number in enumerate(random.sample(range(1, 91), 15), 1):
            row.append(number)

            if len(row) == 5:
                row = sorted(row)

                while len(row) < 9:
                    row.insert(random.randint(0, len(row)), '_')

                card.append(row)
                row = []

        return card

    @staticmethod
    def print_card(player):
        for row in player.card:
            for number in row:
                print('{:<4}'.format(number), end='')
            print('\n')

    def get_keg(self):
        return self.kegs.pop(random.randrange(len(self.kegs)))

    def game(self):
        while self.kegs:
            current_keg = self.get_keg()
            print('Новый бочонок: %s (осталось) %s' % (current_keg, len(self.kegs)))
            print('---------- Ваша карточка ---------')
            self.print_card(self.player)
            print('------- Карточка компьютера ------')
            self.print_card(self.computer_player)

            while True:
                action = input('Зачеркнуть цифру? (y/n)')

                if action != 'y' and action != 'n':
                    print('Неизвестное действие')
                else:
                    break

            is_number_exists = self.player.search_and_delete_ceil(current_keg)

            if action == 'y' and is_number_exists is False:
                print('Вы проиграли, числа %s нет на вашей карточке' % current_keg)
                exit()
            elif action == 'n' and is_number_exists is True:
                print('Вы проиграли, число %s есть на вашей карточке' % current_keg)
                exit()

            self.computer_player.search_and_delete_ceil(current_keg)

            if self.player.total_removed == 15:
                print('Вы выйграли!')
                exit()
            elif self.computer_player.total_removed == 15:
                print('Выйграл компьютер!')
                exit()
            elif self.player.total_removed == 15\
                    and self.computer_player.total_removed == 15:
                print('Ничья!')
                exit()

            print('\n')


loto = Loto()
loto.game()
