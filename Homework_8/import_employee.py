from json import loads
from csv import reader
import global_variables
import user_dialogs


def import_csv():
    global_variables.global_person_list = []
    with open('database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = reader(fin)
        for row in csv_reader:
            if row != []:
                global_variables.global_person_list.append(
                    dict(zip(global_variables.person_list_ids, row)))
        user_dialogs.print_import_export('Импорт')


def import_json():
    global_variables.global_person_list = []
    with open('database.json', 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = loads(line.strip())
            global_variables.global_person_list.append(temp)
    user_dialogs.print_import_export('Импорт')
