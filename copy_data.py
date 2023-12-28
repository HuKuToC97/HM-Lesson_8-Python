import os

from logger import *
from create_data import *
from search_data import *
from additional_functions import *

def remember_contact():
    os.system('cls||clear')
    print('Выберите возможные вариант для продолжения: \n\
    1) Показать всю записную книгу\n\
    2) Вызвать поиск контакта\n\
    3) Вернуться в предыдущее меню\n')

    command = input_data_and_check_correct('Введите номер действия: ', ('1', '2', '3'))

    match (command):
        case '1': 
            show_info()
        case '2':
            os.system('cls||clear')
            search_contact()
        case '3':
            os.system('cls||clear')
            return

def copy_data_in_new_file():
    pass



def check_for_copy(file_path,num_str):
    command = '-1'
    while command != 3:
        print('Вы хотите скопировать следующий контакт:')
        print('-----------------')
        with open(file_path, 'r', encoding='UTF-8') as file:
            lines = file.readlines()
            print(lines[(num_str-1)*3] + \
                  lines[(num_str-1)*3+1].rstrip())
        print('-----------------')
        print('\n\
            1) Да\n\
            2) Выбрать другой контакт\n\
            3) Выход из меню выбора контакта\n')
        
        command = input_data_and_check_correct('Введите номер действия: ', ('1', '2', '3'))

        match (command):
            case '1': 
                return True
            case '2':
                return False
            case '3':
                return None










def copy_contact():
    os.system('cls||clear')

    command = '-1'

    while command != '3':
        print('Для копирования необходим порядковый номер контакта из записной книжки.\n'\
            'Вы знаете порядковый номер контакта? \n\
            1) Да\n\
            2) Нет\n\
            3) Выход из меню копирования\n')

        command = input_data_and_check_correct('Введите номер действия: ', ('1', '2', '3'))

        if command == '1':
            result_check = False

            while result_check != True:
            
            
                os.system('cls||clear')

                contact_serial_num_for_copy = int(input_data_and_check_correct('Введите порядковый номер контакта для копирования: ', \
                                                                    tuple(map(str, tuple(range(1, int(count_str_in_file('phonebook.txt')/3) + 1))))))
                print()


                result_check = check_for_copy('phonebook.txt', contact_serial_num_for_copy)

                if result_check:
                    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
                        lines = file.readlines()
                        with open('contact_copy.txt', 'a', encoding='UTF-8') as output:
                            output.write(lines[(contact_serial_num_for_copy-1)*3] + \
                            lines[(contact_serial_num_for_copy-1)*3+1]+'\n')     
                        print('\nКонтакт скопирован в конец файла "contact_copy.txt"!')
                        waiting_for_input_to_continue()
                        os.system('cls||clear')
                        break
                elif result_check == False:
                    pass
                else:
                    os.system('cls||clear')
                    break
        
        if command == '2':
            remember_contact()

        if command == '3':
            os.system('cls||clear')
            return

    return