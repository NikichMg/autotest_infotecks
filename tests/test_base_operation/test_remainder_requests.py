from operation.remainder import req_remainder_result
import logging
import pytest


#позитивные проверки X - делимое, Y-делитель, Статус код, Результат
@pytest.mark.parametrize('x, y, statusCode, expected_result',
                         [(10, 10, 0, 0),
                          (0, 10, 0, 0),
                          (11, -1, 0, 0),
                          (-11, 2, 0, 1),
                          (-11, -3, 0, -2),
                          (1, -4, 0, -3),
                          (-1, -5, 0, -1),
                          (-4, 6, 0, 2)
                          ])
def test_req_remainder_result_positive(x, y, statusCode, expected_result):
    logging.info(f'Проверка остатка от ДЕЛЕНИЯ {x} на {y}')
    if statusCode == 0:
        logging.info(f"Expected result: {{'statusCode': {statusCode}, 'result': {expected_result}}}")
    else:
        logging.error(f"Expected result: {{'statusCode': {statusCode}, 'statusMessage': {expected_result}}}")
    assert req_remainder_result(x, y) == (statusCode, expected_result), logging.error('FAILED')
    logging.info('PASSED')
#Проверка деления на 0
def test_req_zero_remainder():
    logging.info(f'Проверка остатка от ДЕЛЕНИЯ на НОЛЬ')
    logging.info("Expected result: {'statusCode': 1, 'result': 'Ошибка вычисления'}")
    assert req_remainder_result(10,0) == (1, 'Ошибка вычисления'), logging.error('FAILED')
    logging.info('PASSED')
#Нa пустой ввод
@pytest.mark.parametrize('x,y,statusCode, expected_result',
                         [(10,None,3,'Одно из значений не является целым числом'),
                          (None,10,3,'Одно из значений не является целым числом'),
                          (None,None,3,'Одно из значений не является целым числом')])
def test_req_empty_remainder(x,y,statusCode,expected_result):
    logging.info(f'Проверка остатка от ДЕЛЕНИЯ {x} на {y}')
    if statusCode == 0:
        logging.info(f"Expected result: {{'statusCode': {statusCode}, 'result': {expected_result}}}")
    else:
        logging.error(f"Expected result: {{'statusCode': {statusCode}, 'statusMessage': {expected_result}}}")
    assert req_remainder_result(x,y) == (statusCode,expected_result), logging.error('FAILED')
    logging.info('PASSED')
#Проверка диапазона чисел от -2147483648 до 2147483647
#Проверка левой границы -2147483649  -2147483648  -2147483647
@pytest.mark.parametrize('x,y,statusCode,expected_result',[
                         (1,-2147483649,4,'Превышен размер одного из значений'),
                         (-2147483649,1,4,'Превышен размер одного из значений'),
                         (-2147483648,1,0,0),
                         (1,-2147483648,0,-2147483647),
                         (-2147483647,1,0,0),
                         (1,-2147483647,0,-2147483646),
                         (2147483647,-1,0,0),
                         (-1,2147483647,0,2147483646),
                         ])
def test_req_boundaries_left_remainder(x,y,statusCode,expected_result):
    logging.info(f'Проверка остатка от ДЕЛЕНИЯ больших чисел слева {x} на {y}')
    if statusCode == 0:
        logging.info(f"Expected result: {{'statusCode': {statusCode}, 'result': {expected_result}}}")
    else:
        logging.error(f"Expected result: {{'statusCode': {statusCode}, 'statusMessage': {expected_result}}}")
    assert req_remainder_result(x,y) == (statusCode,expected_result), logging.error('FAILED')
    logging.info('PASSED')
#проверка правой границы 2147483646   2147483647    2147483648
@pytest.mark.parametrize('x,y,statusCode,expected_result',
                        [
                        (2147483648,1,4,'Превышен размер одного из значений'),
                        (1,2147483648,4,'Превышен размер одного из значений'),
                        (2147483647,1,0,0),
                        (1,2147483647,0,1),
                        (2147483647,-1,0,0),
                        (-1,2147483647,0,2147483646),
                        (-2147483648,2147483647,0,2147483646),
                        (2147483646,1,0,0),
                        (1,2147483646,0,1),
                        (2147483646,-1,0,0),
                        (-1,2147483646,0,2147483645)
                        ])
def test_req_boundaries_right_remainder(x,y,statusCode,expected_result):
    logging.info(f'Проверка остатка от ДЕЛЕНИЯ больших чисел справа {x} на {y}')
    if statusCode == 0:
        logging.info(f"Expected result: {{'statusCode': {statusCode}, 'result': {expected_result}}}")
    else:
        logging.error(f"Expected result: {{'statusCode': {statusCode}, 'statusMessage': {expected_result}}}")
    assert req_remainder_result(x,y) == (statusCode,expected_result), logging.error('FAILED')
    logging.info('PASSED')