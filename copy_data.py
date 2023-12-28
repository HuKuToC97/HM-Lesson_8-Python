import os

from logger import *
from create_data import *
from search_data import *
from additional_functions import *

def copy_contact():
    os.system('cls||clear')

    command = '-1'

    while command != '3':
        print('Вы знаете порядковый номер контакта в списке? \n\
            1) Да\n\
            2) Нет\n\
            3) Выход из копирования\n')

        command = input_data_and_check_correct('Введите номер действия: ', ('1', '2', '3'))

        if command == '3':
            os.system('cls||clear')
            return
        
        if command == '2':
            print('Выберите возможные вариант для продолжения: \n\
            1) Показать всю записную книгу\n\
            2) Вызвать поиск контакта\n\
            3) Выход из копирования\n')

            command = input_data_and_check_correct('Введите номер действия: ', ('1', '2', '3'))

            match (command):
                case '1': 
                    show_info()
                case '2':
                    os.system('cls||clear')
                    search_contact()
                case '3':
                    return
        
        contact_serial_num_for_copy = input_data_and_check_correct('Введите номер контакта для копирования', \
                                                                   count_str_in_file('phonebook.txt'))
    

    print('\nКонтакт скопирован!')
    waiting_for_input_to_continue()
    os.system('cls||clear')
    pass