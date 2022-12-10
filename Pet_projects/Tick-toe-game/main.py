field = [["-"] * 3 for i in range(3)]
turn_counter = 0


def greet():
    print("----------------------")
    print("   Добро пожаловать   ")
    print("в игру крестики-нолики")
    print("----------------------")
    print("  формат ввода:  x y  ")
    print("x - координата строки ")
    print("y - координата столбца")
    print("----------------------")


def show_field():
    print()
    print("  1 2 3")
    for i, row in enumerate(field, start=1):
        row_str = f"{i} {' '.join(row)} "
        print(row_str)
    print()


def player_turn():
    while True:
        coords = input('Введите координаты: ').split()

        if len(coords) != 2:
            print('Упс! Введите 2 координаты.')
            continue

        x, y = coords

        if not(x.isdigit()) or not(y.isdigit()):
            print('Упс! Координаты - не числа.')
            continue

        x, y = int(x), int(y)
        x -= 1
        y -= 1

        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Упс! Координаты вне игрового поля.')
            continue

        if field[x][y] != '-':
            print('Упс! Клетка уже занята.')
            continue

        return x, y


def check_win():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ['X', 'X', 'X']:
            return 'Выиграл крестик!'
        elif symbols == ['0', '0', '0']:
            return ' Выиграл нолик! '

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ['X', 'X', 'X']:
            return 'Выиграл крестик!'
        elif symbols == ['0', '0', '0']:
            return ' Выиграл нолик! '

    symbols = []
    for i in range(3):
        symbols.append(field[i][i])
    if symbols == ['X', 'X', 'X']:
        return 'Выиграл крестик!'
    elif symbols == ['0', '0', '0']:
        return ' Выиграл нолик! '

    symbols = []
    for i in range(3):
        symbols.append(field[i][2-i])
    if symbols == ['X', 'X', 'X']:
        return 'Выиграл крестик!'
    elif symbols == ['0', '0', '0']:
        return ' Выиграл нолик! '

    return False


greet()

while True:
    turn_counter += 1

    show_field()

    if turn_counter % 2 == 0:
        print("Ходит НОЛИК")
    else:
        print("Ходит КРЕСТИК")

    x, y = player_turn()

    if turn_counter % 2 == 0:
        field[x][y] = "0"
    else:
        field[x][y] = "X"

    if check_win() is not False:
        show_field()
        print("----------------------")
        print(f"-- {check_win()} --")
        print("----------------------")
        break
    elif turn_counter == 9:
        show_field()
        print("----------------------")
        print("------- Ничья! -------")
        print("----------------------")
        break
