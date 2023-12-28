import os

from ui import *
from logger import *
from date_create import *

def input_surname():
    return input('Введите фамилию контакта: ')

def input_name():
    return input('Введите имя контакта: ')

def input_patronymic():
    return input('Введите отчество контакта: ')

def input_phone():
    return input('Введите номер контакта: ')

def input_address():
    return input('Введите адрес контакта: ')


def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()

    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'

