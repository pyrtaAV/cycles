from logger import logger_config

log = logger_config(__name__)

def user_input():
    try:
        a = int(input())
    except ValueError:
        log.exception('Невозможно преобразовать введенное значение значение')
        return 0
    else:
        return a

a = user_input()
number_list = []

while a != 0:
    print('Повторите ввод')
    number_list.append(a)
    a = user_input()
    
log.info(f'Среднее число списка равно {sum(number_list) / len(number_list)}')