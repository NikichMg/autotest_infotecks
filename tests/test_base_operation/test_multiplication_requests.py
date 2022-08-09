from operation.multiplication import req_multiplication_result
import pytest
import logging

#позитивные проверки X - частное, Y - частное, Статус код, Результат
@pytest.mark.parametrize('x, y, statusCode, expected_result',
                         [(0, 0, 0, 0),
                          (0, 1, 0, 0),
                          (1, 0, 0, 0),
                          (1, -1, 0, -1),
                          (-1, 1, 0, -1),
                          (-1, -1, 0, 1)
                          ])
def test_req_multiplication_result_positive(x, y, statusCode, expected_result):
    logging.info(f'Проверка УМНОЖЕНИЯ {x} на {y}')
    if statusCode == 0:
        logging.info(f"Expected result: {{'statusCode': {statusCode}, 'result': {expected_result}}}")
    else:
        logging.error(f"Expected result: {{'statusCode': {statusCode}, 'statusMessage': {expected_result}}}")
    assert req_multiplication_result(x, y) == (statusCode, expected_result), logging.error('FAILED')
    logging.info('PASSED')
#Не пустой ввод
@pytest.mark.parametrize('x,y,statusCode, expected_result',
                         [(10,None,3,'Одно из значений не является целым числом'),
                          (None,10,3,'Одно из значений не является целым числом'),
                          (None,None,3,'Одно из значений не является целым числом')])
def test_req_empty_multiplication(x,y,statusCode, expected_result):
    logging.info(f'Проверка УМНОЖЕНИЯ {x} на {y}')
    if statusCode == 0:
        logging.info(f"Expected result: {{'statusCode': {statusCode}, 'result': {expected_result}}}")
    else:
        logging.error(f"Expected result: {{'statusCode': {statusCode}, 'statusMessage': {expected_result}}}")
    assert req_multiplication_result(x,y) == (statusCode,expected_result), logging.error('FAILED')
    logging.info('PASSED')
#Проверка границ от -2147483648 до 2147483647
#Проверка левой границы:
@pytest.mark.parametrize('x,y,statusCode, expected_result',
                         [(-2147483649,1,4,'Превышен размер одного из значений'),
                          (1,-2147483649,4,'Превышен размер одного из значений'),
                          (-715827883,3,4,'Превышен размер одного из значений'),
                          (3,-715827883,4,'Превышен размер одного из значений'),
                          (-2147483648,2147483647,4,'Превышен размер одного из значений'),
                          (2147483647,-2147483648,4,'Превышен размер одного из значений'),
                          (-1073741824,2,0,-2147483648),
                          (2,-1073741824,0,-2147483648),
                          (-2147483647,1,0,-2147483647),
                          (1,-2147483647,0,-2147483647)
                          ])
def test_req_boundaries_left_multiplication(x,y,statusCode, expected_result):
    logging.info(f'Проверка УМНОЖЕНИЯ больших чисел слева {x} на {y}')
    if statusCode == 0:
        logging.info(f"Expected result: {{'statusCode': {statusCode}, 'result': {expected_result}}}")
    else:
        logging.error(f"Expected result: {{'statusCode': {statusCode}, 'statusMessage': {expected_result}}}")
    assert req_multiplication_result(x,y) == (statusCode,expected_result), logging.error('FAILED')
    logging.info('PASSED')
#Проверка правой границы:
@pytest.mark.parametrize('x,y,statusCode, expected_result',
                         [(2147483648,1,4,'Превышен размер одного из значений'),
                          (1,2147483648,4,'Превышен размер одного из значений'),
                          (10737418243,2,4,'Превышен размер одного из значений'),
                          (2,1073741824,4,'Превышен размер одного из значений'),
                          (2147483647,2147483647,4,'Превышен размер одного из значений'),
                          (-2147483648,-2147483648,4,'Превышен размер одного из значений'),
                          (2147483647,1,0,2147483647),
                          (1,2147483647,0,2147483647),
                          (1073741823,2,0,2147483646),
                          (2,1073741823,0,2147483646)
                          ])
def test_req_boundaries_right_multiplication(x,y,statusCode, expected_result):
    logging.info(f'Проверка УМНОЖЕНИЯ больших чисел справа {x} на {y}')
    if statusCode == 0:
        logging.info(f"Expected result: {{'statusCode': {statusCode}, 'result': {expected_result}}}")
    else:
        logging.error(f"Expected result: {{'statusCode': {statusCode}, 'statusMessage': {expected_result}}}")
    assert req_multiplication_result(x,y) == (statusCode,expected_result), logging.error('FAILED')
    logging.info('PASSED')