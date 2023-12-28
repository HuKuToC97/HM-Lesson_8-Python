import os

from additional_functions import *




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


