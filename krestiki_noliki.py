# Игра «Крестики-нолики».


def map_print(map_array):  # функция вывода на экран текущего состояния карты
    count = 0
    row = 0
    print("\n")
    print("", 0, 1, 2, sep="    ")
    for i in map_array:
        if count % 3 == 0:
            print(str(row), " ", map_array[i], end="    ")
        else:
            print(map_array[i], end="    ")
        count += 1
        if count % 3 == 0:
            print("\n")
            row += 1

    print("\n")


def status_print(player):
    print(f"{player}, Ваш ход")


def check_coordinates(check_coord, check_map):
    _mar1 = False
    _mar2 = False
    # проверка на допустимый диапазон координат
    correct_coordinates = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]
    for c in correct_coordinates:
        if c == check_coord:
            _mar1 = True
    # проверка не занято ли это поле
    if _mar1:
        if check_map[check_coord] == "-":
            _mar2 = True
    return _mar1 and _mar2

def victory_check_x(map_check):
    map_win = {
        "1": ["00", "01", "02"],
        "2": ["10", "11", "12"],
        "3": ["20", "21", "22"],
        "4": ["00", "10", "20"],
        "5": ["01", "11", "21"],
        "6": ["02", "12", "22"],
        "7": ["00", "11", "22"],
        "8": ["02", "11", "20"],
    }
    x_list = []
    for x, x_values in map_check.items():
        if x_values == "X":
            x_list.append(x)
    for key, values in map_win.items():
        for x in x_list:
            if x in values:
                values.remove(x)
                if values == []:
                    return True


def victory_check_o(map_check):
    map_win = {
        "1": ["00", "01", "02"],
        "2": ["10", "11", "12"],
        "3": ["20", "21", "22"],
        "4": ["00", "10", "20"],
        "5": ["01", "11", "21"],
        "6": ["02", "12", "22"],
        "7": ["00", "11", "22"],
        "8": ["02", "11", "20"],
    }
    o_list = []
    for o, o_values in map_check.items():
        if o_values == "O":
            o_list.append(o)
    for key, values in map_win.items():
        for o in o_list:
            if o in values:
                values.remove(o)
                if values == []:
                    return True


# ---------------------------------------------------------------------------------------------------
# Вывод приветствия и правил игры
print("************************************************************************************************\n"
      "* Добро пожаловать в игру Крестики-нолики.                                                     *\n"
      "*                                                                                              *\n"
      "* Правила:                                                                                     *\n"
      "* Игроки по очереди ставят на свободные клетки поля 3×3 знаки                                  *\n"
      "* (один всегда крестики, другой всегда нолики). Первый, выстроивший                            *\n"
      "* в ряд 3 своих фигуры по вертикали, горизонтали или большой диагонали,                        *\n"
      "* выигрывает. Если игроки заполнили все 9 ячеек и оказалось, что ни в                          *\n"
      "* одной вертикали, горизонтали или большой диагонали нет трёх одинаковых                       *\n"
      "* знаков, партия считается закончившейся вничью. Первый ход делает игрок, ставящий крестики.   *\n"
      "*                                                                                              *\n"
      "* Обычно по завершении партии выигравшая сторона зачёркивает чертой свои три знака             *\n"
      "* (нолика или крестика), составляющих сплошной ряд.                                            *\n"
      "************************************************************************************************\n")

# присваиваем имена игрокам
cross_player = input("Кто будет играть крестиками? (введите имя): ")
zero_player = input("Хорошо, тогда введите имя второго игрока, он будет играть ноликами: ")

# Определяем исходные данные:
map_kn = {           # - словарь с состояниями
    "00": "-", "01": "-", "02": "-",
    "10": "-", "11": "-", "12": "-",
    "20": "-", "21": "-", "22": "-"
}
active_player = cross_player  # - активный игрок
active_symbol = "X"     # - активный символ
game_step = 1
draw = True # - по умолчанию будет ничья


map_print(map_kn) # выводим на экран поле для игры в крестики-нолики - функция
status_print(active_player) # выводим на экран имя активного игрока и просим сделать ход


while game_step <= 9: # в игре максимум 9 ходов
    # просим активного игрока ввести координаты крестика (нолика)
    active_coordinate = input("Введите координату в формате xy (например, 00 - для верхнего левого положения: ")
    if not check_coordinates(active_coordinate, map_kn):    # если ввод данных некорректный, то выводим сообщение
        print("Некорректный ввод. Попробуйте еще раз.")
    # если ввод данных верный, то продолжаем
    else:
        if active_player == cross_player:
            active_symbol = "X"
        else:
            active_symbol = "O"
        map_kn[active_coordinate] = active_symbol        # вносим изменение в словарь
        map_print(map_kn)  # выводим на экран актуальное поле для игры в крестики-нолики
        if victory_check_x(map_kn):  # проверяем на наличие выигрышной комбинации у крестиков
            draw = False
            print(
                f"\n ПОЗДРАВЛЯЕМ {active_player}, ВЫ ВЫИГРАЛИ!!!")  # если есть выигрышная комбинация, то выводим на экран поздравления с именем победителя
            break # игра окончена, выводится на экран сообщение и благодарность за игру
        if victory_check_o(map_kn):  # проверяем на наличие выигрышной комбинации
            draw = False
            print(
                f"\n ПОЗДРАВЛЯЕМ {active_player}, ВЫ ВЫИГРАЛИ!!!")  # если есть выигрышная комбинация, то выводим на экран поздравления с именем победителя
            break # игра окончена, выводится на экран сообщение и благодарность за игру
        # меняем активного игрока
        if active_player == cross_player:
            active_player = zero_player
        else:
            active_player = cross_player
        if game_step < 9:
            print(f"{active_player}, ваш ход.")
        # если комбинация невыигрышная, то переходим к следующему шагу
        game_step += 1

if draw:
    print("Это была упорная битва - НИЧЬЯ")
print("\n Классно поиграли. Спасибо")









