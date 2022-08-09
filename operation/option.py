import json
import requests
import logging

def req_option_requests():
    url = 'http://127.0.0.1:17678/api/get'
    response = requests.options(url)
    # Записываем актуальный результат в лог файл
    logging.getLogger().info(f'Actual result  : {response.status_code}')
    return response.status_code
