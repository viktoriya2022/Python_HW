def export_to_file(person_list, extension='.txt'):
    if extension == '.txt':
        with open('person_list.txt', 'w', encoding='utf-8') as file:
            for i in person_list:
                for j in range(0, len(i)):
                    if j == len(i)-1:
                        file.write(f'{i[j]}')
                    else:
                        file.write(f'{i[j]},')
                file.write('\n')
        print('Файл сохранен с именем "person_list.txt"')
        print(f'\n{"-" * 35}\n')
    elif extension == '.csv':
        with open('person_list.csv', 'w', encoding='utf-8') as file:
            for i in person_list:
                for j in range(0, len(i)):
                    if j == len(i)-1:
                        file.write(f'{i[j]}')
                    else:
                        file.write(f'{i[j]},')
                file.write('\n')
        print('Файл сохранен с именем "person_list.csv"')
        print(f'\n{"-" * 35}\n')
