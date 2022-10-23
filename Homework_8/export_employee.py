from csv import writer
from json import dumps
import body
import global_variables
import user_dialogs


def export_csv():
    if body.person_list_not_empty(True, global_variables.global_person_list):
        with open('database.csv', 'w', encoding='utf-8') as fout:
            csv_writer = writer(fout)
            for employee in global_variables.global_person_list:
                csv_writer.writerow(employee.values())
            user_dialogs.print_import_export('Экспорт')


def export_json():
    if body.person_list_not_empty(True, global_variables.global_person_list):
        with open('database.json', 'w', encoding='utf-8') as fout:
            for employee in global_variables.global_person_list:
                fout.write(dumps(employee) + '\n')
            user_dialogs.print_import_export('Экспорт')
