from user_dialog import is_person_list_file_exist
from user_dialog import get_main_menu
from user_dialog import get_export_menu
from export_file import export_to_file
from import_file import import_from_file
from user_dialog import generate_person
from user_dialog import print_person
from user_dialog import find_person

is_person_list_file_exist()
main_menu = '-1'
while main_menu != '4':
    main_menu = get_main_menu()
    if main_menu == '0':
        generate_person()
    elif main_menu == '1':
        person_list = import_from_file()
        print_person(person_list)
    elif main_menu == '2':
        find_person()
    elif main_menu == '3':
        export_menu = get_export_menu()
        if export_menu == '0':
            person_list = import_from_file()
            export_to_file(person_list)
        elif export_menu == '1':
            export_to_file(import_from_file(), '.csv')
