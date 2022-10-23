def show_menu():
    print('\n'+"=" * 35)
    print("МЕНЮ:")
    print( "=" * 35+"\n")
    print("1. Вывод списка всех сотрудников.")
    print("2. Поиск сотрудника по фамилии.")
    print("3. Выборка по должности.")
    print("4. Выборка по зарплате.")
    print("5. Добавить сотрудника.")
    print("6. Удалить сотрудника.")
    print("7. Обновить данные сотрудника.")
    print("8. Экспорт / импорт.")
    print("9. Завершение работы."'\n')
    return input("Выберите пункт меню: ")


def print_empty_list():
    print("\033[31m {}" .format(
        '\nДанные не найдены.'+"\033[0m"))


def print_import_export(import_export):
    print("\033[31m {}" .format(
        f'\n{import_export} успешно произведен'+"\033[0m"))


def find_person_dialog():
    search_item = input('\nВведите данные для поиска: ')
    return search_item


def delete_person_dialog(dialog_num, id_person=0):
    match dialog_num.split():
        case['1']:
            person_id = input('\nВведите id сотрудника: ')
            return person_id
        case['2']: print("\033[31m {}" .format(
            f'\nСотрудник с id {id_person} удален'+"\033[0m"))
        case['3']: print("\033[31m {}" .format(
            f'\nСотрудник с id {id_person} не найден'+"\033[0m"))


def change_person_dialog(dialog_num, id_person=0):
    match dialog_num.split():
        case['1']:
            person_id = input('\nВведите id сотрудника для изменения: ')
            return person_id
        case['2']: print("\033[31m {}" .format(
            f'\nИзменения для сотрудника с id {id_person} сохранены'+"\033[0m"))
        case['3']: print("\033[31m {}" .format(
            f'\nСотрудник с id {id_person} не найден'+"\033[0m"))


def show_export_import_menu():
    print("\n" + "=" * 35+"\n")
    print("1. Экспортировать данные в формате json")
    print("2. Экспортировать данные в формате csv")
    print("3. Импортировать данные из формата json")
    print("4. Импортировать данные из формата csv")
    print("5. Выход в основное меню")
    return input("Введите номер необходимого действия: ")
