field_size = 3
field = [["-"] * field_size for i in range(field_size)]

PLAYER_NAME = None
player_symbol = None
computer_symbol = None

def show():
    print()
    print("  1 2 3")
    for i, row in enumerate(field, start = 1):
        row_str = f"{i} {' '.join(row)} "
        print(row_str)
    print()

# show()

def player_turn():
    while True:
        coords = input('Введите координаты вашего хода: ').split('')
        print(coords)

        if len(coords) != 2:
            print('Упс! Введите 2 координаты.')
            continue

        x, y = coords

        if not(x.isdigit()) or not(y.isdigit()):
            print('Упс! Координаты - не числа.')
            continue

        x, y = int(x), int(y)

        if 1 <= x <=3 and 1 <= y <=3:
            print('Упс! Координаты вне игрового поля.')
            continue

        if field[x][y] == '-':
            print('Упс! Клетка уже занята.')
            continue

        print(x, y)
        return x, y


def lottery():
    while True:
        player_symbol = input(f'{PLAYER_NAME}, ты будешь играть "крестиками" или "ноликами"? Напечатай X или 0: ')
        if player_symbol in ['x', 'X', 'Х', 'х']:
            player_symbol = 'X'
            computer_symbol = '0'
            print('Хорошо! Ты играешь "крестиками", а я - "ноликами". Приступим.')
            return player_symbol, computer_symbol
        elif player_symbol in ['0', 'O', 'o', 'О', 'о']:
            player_symbol = '0'
            computer_symbol = 'X'
            print('Хорошо! Ты играешь "ноликами", а я - "крестиками". Приступим.')
            return player_symbol, computer_symbol
        else:
            print(f'{PLAYER_NAME}, хорошая попытка, но таким сиволом мы не играем. Давай попробуем сделать выбор еще раз.')


def game():
    print('Добро пожаловать в игру крестики-нолики!')
    PLAYER_NAME = input('Как тебя зовут? ')
    print(f'Приятно познакомиться, {PLAYER_NAME}! Давай я тебе вкратце расскажу правила игры.')
    print('----правила----')
    lottery()
    show()

player_turn()