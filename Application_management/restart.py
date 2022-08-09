import logging
import subprocess

def calc_restart():
    # Выполняем команду "restart" и возвращаем её вывод
    result = subprocess.check_output('./webcalculator.exe restart').decode('cp1251').splitlines()
    # Выбираем нужный результат из списка
    if len(result)==1:
        return result[0]
    return result[3]

def calc_restart_test():
    # Выполняем команду "restart" и возвращаем её вывод
    result = subprocess.check_output('./webcalculator.exe restart').decode('cp1251').splitlines()
    if len(result)==1:
        # Записываем актуальный результат в лог файл
        logging.info(f'Actual result: {result[0]}')
        return result[0]
    # Записываем актуальный результат в лог файл
    logging.info(f'Actual result: {result[3]}')
    return result[3]


