import global_variables
import export_employee
import import_employee
import user_dialogs


def print_person_list(person_list):
    if person_list_not_empty(True, person_list):
        for i in range(0, len(person_list)):
            print(f'\n{"-" * 16} {i + 1} {"-" * 16}\n')
            for item in range(0, len(person_list[i])):
                print(
                    f'{global_variables.person_list_ids[item]}: {person_list[i][global_variables.person_list_ids[item]]}')
        print(f'\n{"-" * 35}\n')


def person_list_not_empty(print_msg, person_list):
    if person_list != []:
        return True
    else:
        if print_msg:
            user_dialogs.print_empty_list()
    return False


def add_person():
    temp = {}
    if person_list_not_empty(False, global_variables.global_person_list):
        temp[global_variables.person_list_ids[0]] = str(
            int(global_variables.global_person_list[len(global_variables.global_person_list)-1]['id'])+1)
    else:
        temp[global_variables.person_list_ids[0]] = '1'
    for item in range(0, len(global_variables.add_dialog)):
        temp[global_variables.person_list_ids[item+1]
             ] = input(global_variables.add_dialog[item])
    global_variables.global_person_list.append(temp)


def delete_person():
    id_person = user_dialogs.delete_person_dialog('1')
    for item in global_variables.global_person_list:
        if id_person in item['id']:
            del global_variables.global_person_list[global_variables.global_person_list.index(
                item)]
            user_dialogs.delete_person_dialog('2', id_person)
            break
    else:
        user_dialogs.delete_person_dialog('3', id_person)


def change_person():
    id_person = user_dialogs.change_person_dialog('1')
    for item in global_variables.global_person_list:
        if id_person in item['id']:
            for change_id in range(1, len(item)):
                print(
                    f'\nТекущее значение {global_variables.person_list_ids[change_id]}: {item[global_variables.person_list_ids[change_id]]}')
                item[global_variables.person_list_ids[change_id]
                     ] = input('\nВведите новое значение (пропустить - ENTER): ')
            user_dialogs.change_person_dialog('2', id_person)
            break
    else:
        user_dialogs.change_person_dialog('3', id_person)


def do_menu_id(menu_id):
    match menu_id.split():
        case ['1']: export_employee.export_json()
        case ['2']: export_employee.export_csv()
        case ['3']: import_employee.import_json()
        case ['4']: import_employee.import_csv()


def find_person(search_position):
    search_param = user_dialogs.find_person_dialog()
    temp_list = []
    for item in global_variables.global_person_list:
        if (item[search_position] == search_param):
            temp_list.append(item)
    print_person_list(temp_list)
