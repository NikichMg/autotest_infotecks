import json
import logging

import requests
#функция для вывода результата операции в виде: (СТАТУС КОД, РЕЗУЛЬТАТ/ОШИБКА)
def req_addition_result(x, y):
    # ссылка на тестируемую опцию
    url = 'http://127.0.0.1:17678/api/addition'
    params = {
        "x": x, # первый параметр
        "y": y  # второй параметр
    }
    # кодируем словарь в формат JSON
    json_param = json.dumps(params)
    # отправка POST-запроса с данными в формате JSON
    response = requests.post(url, data=json_param)
    # кодируем словарь в формат JSON
    res = response.json()
    # получаем данные из готового словаря
    statusCode = res.get('statusCode')
    result = res.get('result')
    statusMessage = res.get('statusMessage')
    #определяем результат или тип ошибки
    if statusCode == 0:
        res = result
        # Записываем актуальный результат в лог файл
        logging.info(f'Actual result: {response.json()}')
    else:
        res = statusMessage
        # Записываем актуальный результат в лог файл
        logging.error(f'Actual result: {response.json()}')
    return statusCode, res

def addition_status_requests(x='',y=''):
    # ссылка на тестируемую опцию
    url = 'http://127.0.0.1:17678/api/addition'
    params = {
        "x": x, # первый параметр
        "y": y  # второй параметр
    }
    # кодируем словарь в формат JSON
    json_param = json.dumps(params)
    # отправка POST-запроса с данными в формате JSON
    response = requests.post(url, data=json_param)
    # Записываем актуальный результат в лог файл
    logging.getLogger().info(f'Actual result  : {response.status_code}')
    return response.status_code

def addition_status_response(x='',y=''):
    # ссылка на тестируемую опцию
    url = 'http://127.0.0.1:17678/api/addition'
    params = {
        "x": x, # первый параметр
        "y": y  # второй параметр
    }
    # кодируем словарь в формат JSON
    json_param = json.dumps(params)
    # отправка POST-запроса с данными в формате JSON
    response = requests.post(url, data=json_param)
    # Записываем актуальный результат в лог файл
    logging.getLogger().info(f'Actual result  : {response.json()}')
    return response.json()
