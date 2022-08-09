import logging
from operation.add import req_addition_result
import pytest
#позитивные проверки X - слагаемое, Y - слагаемое, Статус код, Результат
@pytest.mark.parametrize('x, y, statusCode, expected_result',
                         [(0, 0, 0, 0),
                          (0, 1, 0, 1),
                          (1, 0, 0, 1),
                          (1, -1, 0, 0),
                          (-1, 1, 0, 0),
                          (-1, -1, 0, -2)
                          ])
def test_req_addition_result_positive(x, y, statusCode, expected_result):
    logging.info(f'Проверка СЛОЖЕНИЯ числа {x} и {y}:')
    if statusCode == 0:
        logging.info(f"Expected result: {{'statusCode': {statusCode}, 'result': {expected_result}}}")
    else:
        logging.error(f"Expected result: {{'statusCode': {statusCode}, 'statusMessage': {expected_result}}}")
    assert req_addition_result(x, y) == (statusCode, expected_result), logging.error('FAILED')
    logging.info('PASSED')
#На пустой ввод
@pytest.mark.parametrize('x,y,statusCode, expected_result',
                         [(10,None,3,'Одно из значений не является целым числом'),
                          (None,10,3,'Одно из значений не является целым числом'),
                          (None,None,3,'Одно из значений не является целым числом')])
def test_req_empty_addition(x,y,statusCode, expected_result):
    logging.info(f'Проверка СЛОЖЕНИЯ {x} и {y}:')
    if statusCode == 0:
        logging.info(f"Expected result: {{'statusCode': {statusCode}, 'result': {expected_result}}}")
    else:
        logging.error(f"Expected result: {{'statusCode': {statusCode}, 'statusMessage': {expected_result}}}")
    assert req_addition_result(x,y) == (statusCode,expected_result), logging.error('FAILED')
    logging.info('PASSED')
#Проверка границ от -2147483648 до 2147483647
#Проверка левой границы:
@pytest.mark.parametrize('x,y,statusCode,expected_result',[
                             (-1,-2147483648,4,'Превышен размер одного из значений'),
                             (-2147483648,-1,4,'Превышен размер одного из значений'),
                             (1,-2147483649,4,'Превышен размер одного из значений'),
                             (-2147483649,1,4,'Превышен размер одного из значений'),
                             (-2147483648,-2147483648,4,'Превышен размер одного из значений'),
                             (1,-2147483648,0,-2147483647),
                             (-2147483648,1,0,-2147483647),
                             (-1,-2147483647,0,-2147483648),
                             (-2147483647,-1,0,-2147483648)
                             ])
def test_req_boundaries_left_addition(x,y,statusCode,expected_result):
    logging.info(f'Проверка СЛОЖЕНИЯ больших чисел слева {x} и {y}:')
    if statusCode == 0:
        logging.info(f"Expected result: {{'statusCode': {statusCode}, 'result': {expected_result}}}")
    else:
        logging.error(f"Expected result: {{'statusCode': {statusCode}, 'statusMessage': {expected_result}}}")
    assert req_addition_result(x,y) == (statusCode,expected_result), logging.error('FAILED')
    logging.info('PASSED')
#Проверка правой границы
@pytest.mark.parametrize('x,y,statusCode,expected_result',[
                             (1,2147483647,4,'Превышен размер одного из значений'),
                             (2147483647,1,4,'Превышен размер одного из значений'),
                             (-1,2147483648,4,'Превышен размер одного из значений'),
                             (2147483648,-1,4,'Превышен размер одного из значений'),
                             (2147483647,2147483647,4,'Превышен размер одного из значений'),
                             (-1,2147483647,0,2147483646),
                             (2147483647,-1,0,2147483646),
                             (1,2147483646,0,2147483647),
                             (2147483646,1,0,2147483647)
                             ])
def test_req_boundaries_right_addition(x,y,statusCode,expected_result):
    logging.info(f'Проверка СЛОЖЕНИЯ больших чисел справа {x} и {y}:')
    if statusCode == 0:
        logging.info(f"Expected result: {{'statusCode': {statusCode}, 'result': {expected_result}}}")
    else:
        logging.error(f"Expected result: {{'statusCode': {statusCode}, 'statusMessage': {expected_result}}}")
    assert req_addition_result(x,y) == (statusCode,expected_result), logging.error('FAILED')
    logging.info('PASSED')