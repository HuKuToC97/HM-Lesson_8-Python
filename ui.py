import os

from logger import *
from create_data import *
from search_data import *
from copy_data import *
from additional_functions import *


def interface():
    create_txt_file('phonebook')
    os.system('cls||clear')
    command = '-1'
    while command != '5':
        print('Возможные варианты взаимодействия: \n\
            1) Добавить контакт\n\
            2) Вывести весь справочник на экран\n\
            3) Поиск контакта в справочнике\n\
            4) Копирование контакта из справочника в новый файл\n\
            5) Выход из программы\n'
            '\nВнимание!\nПри работе с данной версией программы следует учитывать регистры при написании текста.\n'
            'Например "иван" не равно "Иван".\n')
        
        command = input_data_and_check_correct('Введите номер действия: ', ('1', '2', '3', '4','5'))
        
        os.system('cls||clear')

        match (command):
            case '1': 
                add_contact(create_contact())
            case '2':
                show_info()
            case '3':
                search_contact()
            case '4':
                copy_contact()
            case '5':
                print('Спасибо, что выбрали нашу программу.\nДо свидания!')

