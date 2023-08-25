# Программа должна выводить данные
def write(text):
    with open("data.txt", "a", encoding="utf-8") as f:
        f.writelines(text)
        f.writelines("\n")
        print("Успешно")

def read_all():
    # if "data.txt".exists():
    with open("data.txt", "r", encoding="utf-8") as f:
        # f.readlines()
        for line in f:
            print(line[:-1])

def get_by_name(name):
    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f:
            if name in line:
                print(line[:-1])

def del_by_name(name):
    a = []
    with open("data.txt", "r+", encoding="utf-8") as f:
        for line in f:
            if name in line:
                continue
            else:
                a.append(line)

    with open("data.txt", "w", encoding="utf-8") as f:
        f.writelines(a)

def edit_by_name(name):
    a = []
    with open("data.txt", "r+", encoding="utf-8") as f:
        for line in f:
            if name in line:
                print(f'Исходная строка: {line[:-1]}')
                t = input("Введите на что изменить. Пример:(фамилия имя отчество номер телефона) ")
                
                print('Подтвердите замену (1 - Да, 0 - Нет)')
                print(f'Исходная запись: \t {line[:-1]}')
                print(f'Новая запись: \t\t {t}')

                if (input("(1 - Да, 0 - Нет): ")) == '1': a.append(str(t +'\n'))
                else: a.append(line)

            else:
                a.append(line)

    with open("data.txt", "w", encoding="utf-8") as f:
        f.writelines(a)

                   

def choose(choice):
    if choice == '1': return write(input("Введите ваши данные пример:(фамилия имя отчество номер телефона) "))
    elif choice == "2": return read_all()
    elif choice == "3": return get_by_name(input("Введите имя, фамилию, отчество "))
    elif choice == "4": return del_by_name(input("Введите имя, фамилию, отчество для удаления "))
    elif choice == "5": return edit_by_name(input("Введите имя, фамилию, отчество для редактирования "))
    if choice == "0": exit()


'''
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
Пользователь также может ввести фамилию, и Вы должны реализовать функционал для изменения и удаления данных
'''

