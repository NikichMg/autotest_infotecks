import logging
import subprocess

def calc_start(address='',port=''):
    # Проверяем, что оба аргумента пусты(==False)
    if not address and not port:
        # Выполняем команду "start", декодируем и создаем список
        result = subprocess.check_output(f'./webcalculator start').decode('cp1251').splitlines()
        # Выбираем актуальный результат
        if len(result) == 1:
            return result[0]
        return result[1]
    if not port:
        # Выполняем команду "start" только с адрессом
        result = subprocess.check_output(f'./webcalculator start {address}').decode('cp1251').splitlines()
        # Выбираем актуальный результат
        if len(result) == 1:
            return result[0]
        return result[1]
    # Выполняем команду "start" cо всеми входными параметрами и возвращаем её вывод
    result = subprocess.check_output(f'./webcalculator start {address} {port}').decode('cp1251').splitlines()
    if len(result) == 1:
        # Выбираем актуальный результат
        return result[0]
    return result[1]

def calc_start_test(address='',port=''):
    # Проверяем, что оба аргумента пусты(==False)
    if not address and not port:
        # Выполняем команду "start", декодируем и создаем список
        result = subprocess.check_output(f'./webcalculator start').decode('cp1251').splitlines()
        if len(result) == 1:
            # Записываем актуальный результат в лог файл
            logging.info(f'Actual result: {result[0]}')
            return result[0]
        # Записываем актуальный результат в лог файл
        logging.info(f'Actual result: {result[1]}')
        return result[1]
    if not port:
        # Выполняем команду "start" только с адрессом
        result = subprocess.check_output(f'./webcalculator start {address}').decode('cp1251').splitlines()
        if len(result) == 1:
            logging.info(f'Actual result: {result[0]}')
            return result[0]
        # Записываем актуальный результат в лог файл
        logging.info(f'Actual result: {result[1]}')
        return result[1]
    # Выполняем команду "start" cо всеми входными параметрами и возвращаем её вывод
    result = subprocess.check_output(f'./webcalculator start {address} {port}').decode('cp1251').splitlines()
    if len(result) == 1:
        # Записываем актуальный результат в лог файл
        logging.info(f'Actual result: {result[0]}')
        return result[0]
    # Записываем актуальный результат в лог файл
    logging.info(f'Actual result: {result[1]}')
    return result[1]