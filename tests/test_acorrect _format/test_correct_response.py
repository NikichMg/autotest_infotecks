from operation.add import addition_status_response
from operation.division import division_status_response
from operation.multiplication import multiplication_status_response
from operation.remainder import remainder_status_response
from operation.state import state_response
import logging


def test_addition_status_requests():
    logging.info('ТЕСТ НА КОРРЕКТНОСТЬ ФОРМЫ ОТВЕТА ОТ СЛОЖЕНИЯ 1 и 2:')
    logging.info("Expected result: {'statusCode': 0, 'result': 3}")
    assert addition_status_response(1,2) == {'statusCode': 0, 'result': 3}, logging.error('FAILED')
    logging.info('PASSED')


def test_division_status_requests():
    logging.info('ТЕСТ НА КОРРЕКТНОСТЬ ФОРМЫ ОТВЕТА ОТ ДЕЛЕНИЯ НА ЦЕЛО 4 и 2:')
    logging.info("Expected result: {'statusCode': 0, 'result': 2}")
    assert division_status_response(4,2) == {'statusCode': 0, 'result': 2}, logging.error('FAILED')
    logging.info('PASSED')

def test_multiplication_status_requests():
    logging.info('ТЕСТ НА КОРРЕКТНОСТЬ ФОРМЫ ОТВЕТА ОТ УМНОЖЕНИЯ 1 и 2:')
    logging.info("Expected result: {'statusCode': 0, 'result': 2}")
    assert multiplication_status_response(1,2) == {'statusCode': 0, 'result': 2}, logging.error('FAILED')
    logging.info('PASSED')

def test_remainder_status_requests():
    logging.info('ТЕСТ НА КОРРЕКТНОСТЬ ФОРМЫ ОТВЕТА ОТ ОСТАТКА ДЕДЕНИЯ 5 и 2')
    logging.info("Expected result: {'statusCode': 0, 'result': 1}")
    assert remainder_status_response(5,2) == {'statusCode': 0, 'result': 1}, logging.error('FAILED')
    logging.info('PASSED')

def test_state_requests():
    logging.info('ТЕСТ НА КОРРЕКТНОСТЬ ФОРМЫ ОТВЕТА О СОСТОЯНИИ СЕРВЕРА:')
    logging.info("Expected result: {'statusCode': 0, 'state': 'OК'}")
    assert state_response() == {'statusCode': 0, 'state': 'OК'}, logging.error('FAILED')
    logging.info('PASSED')
    logging.info(' ')