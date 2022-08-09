from Application_management.start import calc_start
from operation.add import addition_status_requests
from operation.division import division_status_requests
from operation.multiplication import multiplication_status_requests
from operation.option import req_option_requests
from operation.remainder import remainder_status_requests
from operation.state import state_requests
import logging

# Запускаем сервер на стандартном ip
calc_start()

def test_addition_status_requests():
    logging.info('!!!ТЕСТЫ НА КОРРЕКТНОСТЬ ФОРМЫ ЗАПРОСА/ОТВЕТА!!!')
    logging.info('ТЕСТ НА КОРРЕКТНОСТЬ ФОРМЫ ЗАПРОСА ОТ СЛОЖЕНИЯ 1 и 2:')
    logging.info('Expected result: 200')
    assert addition_status_requests(1,2) == 200, logging.error('FAILED')
    logging.info('PASSED')

def test_division_status_requests():
    logging.info('ТЕСТ НА КОРРЕКТНОСТЬ ФОРМЫ ЗАПРОСА ОТ ДЕЛЕНИЯ 1 на 2:')
    logging.info('Expected result: 200')
    assert division_status_requests(1,2) == 200, logging.error('FAILED')
    logging.info('PASSED')

def test_multiplication_status_requests():
    logging.info('ТЕСТ НА КОРРЕКТНОСТЬ ФОРМЫ ЗАПРОСА ОТ УМНОЖЕНИЯ 1 и 2:')
    logging.info('Expected result: 200')
    assert multiplication_status_requests(1,2) == 200, logging.error('FAILED')
    logging.info('PASSED')

def test_option_requests():
    logging.info('ТЕСТ НА КОРРЕКТНОСТЬ ФОРМЫ ЗАПРОСА ЗАДАЧИ "OPTION":')
    logging.info('Expected result: 200')
    assert req_option_requests() == 200, logging.error('FAILED')
    logging.info('PASSED')

def test_remainder_status_requests():
    logging.info('ТЕСТ НА КОРРЕКТНОСТЬ ФОРМЫ ЗАПРОСА ОТ ОСТАТКА ОТ ДЕЛЕНИЯ 1 на 2:')
    logging.info('Expected result: 200')
    assert remainder_status_requests(1,2) == 200, logging.error('FAILED')
    logging.info('PASSED')

def test_state_requests():
    logging.info('ТЕСТ НА КОРРЕКТНОСТЬ ФОРМЫ ЗАПРОСА О СОСТОЯНИИ СЕРВЕРА:')
    logging.info('Expected result: 200')
    assert state_requests() == 200, logging.error('FAILED')
    logging.info('PASSED')
    logging.info(' ')



