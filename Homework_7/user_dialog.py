from os.path import exists
from get_person import create_fake_person
from import_file import import_from_file
from get_person import create_fake_person
from export_file import export_to_file

info_list = ['Имя', 'Отчество', 'Фамилия', 'Год рождения', 'Возраст',
             'Адрес', 'Телефон', 'e-mail', 'Место работы', 'Должность']


def is_person_list_file_exist():
    if (not exists("person_list.txt")):
        if input('Не найден файл справочника. Сгенерировать справочник? (Y - да)') == 'Y':
            generate_person()


def print_person(person_list):
    for i in range(0, len(person_list)):
        print(f'\n{"-" * 16} {i + 1} {"-" * 16}\n')
        for item in range(0, len(person_list[i])):
            print(f'{info_list[item]}: {person_list[i][item]}')
    print(f'\n{"-" * 35}\n')


def generate_person():
    list_person = []
    person_count = int(
        input('Введите количество личностей для генерации:'))
    for i in range(person_count):
        list_person.append(create_fake_person())
    export_to_file(list_person)
    print_person(list_person)
    return list_person


def get_main_menu():
    print('Главное меню:')
    print('0 - сгенеририровать новый справочник')
    print('1 - отобразить весь справочник')
    print('2 - поиск по справочнику')
    print('3 - сохранить справочник')
    print('4 - выход')
    action = input('Введите номер:')
    return action


def get_export_menu():
    print('В какой формат сохранить справочник?')
    print('0 - ".txt"')
    print('1 - ".csv"')
    action = input('Введите номер:')
    return action


def find_person():
    person_list = import_from_file()
    find_info = input('Введите значение для поиска:')
    for i in person_list:
        for j in i:
            if find_info in j:
                print_person([i])
