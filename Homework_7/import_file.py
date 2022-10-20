from os.path import exists


def import_from_file(file_name='person_list.txt'):
    person_list = []
    if (exists(file_name)):
        with open(file_name, 'r', encoding='utf-8') as file:
            for i in file:
                person_list.append(i.strip().split(','))
        return person_list
    else:
        print(f'Не найден файл {file_name}')
