import os

from ui import *
from logger import *
from date_create import *


def interface():
    with open('phonebook.txt', 'a', encoding='UTF-8'):
        pass
    os.system('cls||clear')
    command = '-1'
    while command != '4':
        print('Возможные варианты взаимодействия: \n\
            1) Добавить контакт\n\
            2) Вывести весь справочник на экран\n\
            3) Поиск контакта в справочнике\n\
            4) Выход из программы\n')
        
        command = input_and_check_correct('Введите номер действия: ', ('1', '2', '3', '4'))
        # command = input('Введите номер действия: ')

        # while command not in ('1', '2', '3', '4'):
        #     print('Некорректные данные')
        #     command = input('Введите номер действия: ')
        
        os.system('cls||clear')

        match (command):
            case '1': 
                add_contact(create_contact())
            case '2':
                show_info()
            case '3':
                search_contact()
            case '4':
                print('Всего хорошего')
    # return

