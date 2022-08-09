import json
import requests
import logging
#функция для вывода результата операции в виде: (СТАТУС КОД, РЕЗУЛЬТАТ/ОШИБКА)
def req_state_result():
    url = 'http://127.0.0.1:17678/api/state'
    response = requests.get(url)
    res = response.json()
    statusCode = res.get('statusCode')
    state = res.get('state')
    logging.info(f'Actual result: {res}')
    # Записываем актуальный результат в лог файл
    return statusCode, state

def state_requests():
    url = 'http://127.0.0.1:17678/api/state'
    response = requests.get(url)
    # Записываем актуальный результат в лог файл
    logging.getLogger().info(f'Actual result  : {response.status_code}')
    return response.status_code

def state_response():
    url = 'http://127.0.0.1:17678/api/state'
    response = requests.get(url)
    # Записываем актуальный результат в лог файл
    logging.getLogger().info(f'Actual result  : {response.json()}')
    return response.json()
