
# Функция используеься для ож
def waiting_for_input_to_continue(messege = 'Нажмите Enter для продолжения...'):
    a = input(messege)


def input_data_and_check_correct(messege, range_data):
    data_input = input(messege)

    while data_input not in range_data:
        print('Некорректные данные')
        data_input = input(messege)

    return data_input

