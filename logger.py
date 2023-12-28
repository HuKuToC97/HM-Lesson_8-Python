import os

from ui import *
from logger import *
from date_create import *

def waiting_for_input_to_continue(messege = 'Нажмите Enter для продолжения...'):
    a = input(messege)

def input_and_check_correct(messege, range_data):
    data_input = input(messege)

    while data_input not in range_data:
        print('Некорректные данные')
        data_input = input(messege)

    return data_input



def add_contact(contact):
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(contact)
    print('\nКонтакт добавлен!')
    waiting_for_input_to_continue()
    os.system('cls||clear')


def show_info():
    print('-----------------')
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        for contact in enumerate(contacts_list, 1):
            print(*contact)
        # print(file.read().rstrip())
    print('-----------------')
    waiting_for_input_to_continue()
    os.system('cls||clear')


def search_by(messege, index_data_in_contact,contacts_list):
    search = input(messege)

    os.system('cls||clear')

    print(f'Результаты поиска по запросу "{search}":')
    print('-----------------')
    for contact_str in contacts_list:
        if index_data_in_contact != 5:
            contact_lst = contact_str.replace('\n',' ').split()
            if search in contact_lst[index_data_in_contact]:
                print(f'{contact_str}\n')
        else:
            if search in contact_str:
                print(f'{contact_str}\n')
    print('-----------------')
    print()
    waiting_for_input_to_continue()


def search_contact():
    var_search = '-1'
    while var_search != '7':
        print('Возможные варианты поиска: \n\
            1) Поиск по фамилии\n\
            2) Поиск по имени\n\
            3) Поиск по отчеству\n\
            4) Поиск по номеру\n\
            5) Поиск по адресу\n\
            6) Поиск совпадений по всей базе\n\
            7) Выход из поиска\n')
        
        var_search = input_and_check_correct('Введите номер действия: ', \
                                             ('1', '2', '3', '4', '5', '6', '7'))
        
        index_data_in_contact = int(var_search)-1
        with open('phonebook.txt', 'r', encoding='UTF-8') as file:
            contacts_list = file.read().rstrip().split('\n\n')
        
        os.system('cls||clear')
        match (var_search):
            case '1': 
                search_by('Введите фамилию или ее часть для поиска контакта: ', index_data_in_contact, contacts_list)
            case '2':
                search_by('Введите имя или его часть для поиска контакта: ',\
                               index_data_in_contact, contacts_list)
            case '3':
                search_by('Введите отчество или его часть для поиска контакта: ',\
                                     index_data_in_contact, contacts_list)
            case '4':
                search_by('Введите номер телефона или его часть для поиска контакта: ',\
                                index_data_in_contact, contacts_list)
            case '5':
                search_by('Введите адрес контакта или его часть для поиска контакта: ',\
                                  index_data_in_contact, contacts_list)
            case '6':
                search_by('Введите данные для поиска контактка: ', \
                          index_data_in_contact, contacts_list)
            case '7':
                print('')
        
        os.system('cls||clear')
