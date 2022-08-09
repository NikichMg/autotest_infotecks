import logging
import subprocess

def calc_stop():
    # Выполняем команду "output" и возвращаем её вывод
    result = subprocess.check_output(f'./webcalculator stop').decode('cp1251').splitlines()
    return result[1]

def calc_stop_test():
    # Выполняем команду "output" и возвращаем её вывод
    result = subprocess.check_output(f'./webcalculator stop').decode('cp1251').splitlines()
    # Записываем актуальный результат в лог файл
    logging.info(f'Actual result: {result[1]}')
    return result[1]
