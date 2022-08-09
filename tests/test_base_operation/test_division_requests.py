import logging

from operation.division import req_division_result
import pytest

#позитивные проверки X - делимое, Y-делитель, Статус код, Результат
@pytest.mark.parametrize('x, y, statusCode, expected_result',
                         [(1, 1, 0, 1),
                          (0, 1, 0, 0),
                          (1, -1, 0, -1),
                          (-1, 1, 0, -1),
                          (-1, -1, 0, 1),
                          (1, 10, 0, 0),
                          (1, -10, 0, -1),
                          (-1, 10, 0, -1),
                          (-1, -10, 0, 0),
                          ])
def test_req_division_result_positive(x, y, statusCode, expected_result):
    logging.info(f'Проверка ДЕЛЕНИЯ на цело {x} на {y}')
    if statusCode == 0:
        logging.info(f"Expected result: {{'statusCode': {statusCode}, 'result': {expected_result}}}")
    else:
        logging.error(f"Expected result: {{'statusCode': {statusCode}, 'statusMessage': {expected_result}}}")
    assert req_division_result(x, y) == (statusCode, expected_result), logging.error('FAILED')
    logging.info('PASSED')
#Проверка деления на 0
def test_req_zero_division():
    logging.info(f'Проверка ДЕЛЕНИЯ на НОЛЬ')
    logging.info("Expected result: {'statusCode': 1, 'result': 'Ошибка вычисления'}")
    assert req_division_result(10,0) == (1, 'Ошибка вычисления'), logging.error('FAILED')
    logging.info('PASSED')
#Не пустой ввод
@pytest.mark.parametrize('x,y,statusCode, expected_result',
                         [(10,None,3,'Одно из значений не является целым числом'),
                          (None,10,3,'Одно из значений не является целым числом'),
                          (None,None,3,'Одно из значений не является целым числом')])
def test_req_empty_division(x,y,statusCode,expected_result):
    logging.info(f'Проверка ДЕЛЕНИЯ на цело {x} на {y}')
    if statusCode == 0:
        logging.info(f"Expected result: {{'statusCode': {statusCode}, 'result': {expected_result}}}")
    else:
        logging.error(f"Expected result: {{'statusCode': {statusCode}, 'statusMessage': {expected_result}}}")
    assert req_division_result(x,y) == (statusCode,expected_result), logging.error('FAILED')
    logging.info('PASSED')
#Проверка диапазона чисел от -2147483648 до 2147483647
#Проверка левой границы -2147483649  -2147483648  -2147483647
@pytest.mark.parametrize('x,y,statusCode,expected_result',[
                         (1,-2147483649,4,'Превышен размер одного из значений'),
                         (-2147483649,1,4,'Превышен размер одного из значений'),
                         (-2147483648,1,0,-2147483648),
                         (1,-2147483648,0,-1),
                         (-2147483647,1,0,-2147483647),
                         (1,-2147483647,0,-1),
                         (2147483647,-1,0,-2147483647),
                         (-1,2147483647,0,-1),
                         ])
def test_req_boundaries_left_division(x,y,statusCode,expected_result):
    logging.info(f'Проверка ДЕЛЕНИЯ на цело больших чисел слева {x} на {y}')
    if statusCode == 0:
        logging.info(f"Expected result: {{'statusCode': {statusCode}, 'result': {expected_result}}}")
    else:
        logging.error(f"Expected result: {{'statusCode': {statusCode}, 'statusMessage': {expected_result}}}")
    assert req_division_result(x,y) == (statusCode,expected_result), logging.error('FAILED')
    logging.info('PASSED')
#проверка правой границы 2147483646   2147483647    2147483648
@pytest.mark.parametrize('x,y,statusCode,expected_result',
                        [
                        (2147483648,1,0,'Превышен размер одного из значений'),
                        (1,2147483648,0,'Превышен размер одного из значений'),
                        (-2147483648,-1,0,'Превышен размер одного из значений'),
                        (-1,-2147483648,0,'Превышен размер одного из значений'),
                        (2147483647,1,0,2147483647),
                        (1,2147483647,0,0),
                        (-2147483647,-1,0,2147483647),
                        (-1,-2147483647,0,0),
                        (2147483646,1,0,2147483646),
                        (1,2147483646,0,0),
                        (-2147483646,-1,0,2147483646),
                        (-1,-2147483646,0,0)
                        ])
def test_req_boundaries_right_division(x,y,statusCode,expected_result):
    logging.info(f'Проверка ДЕЛЕНИЯ на цело больших чисел справа {x} на {y}')
    if statusCode == 0:
        logging.info(f"Expected result: {{'statusCode': {statusCode}, 'result': {expected_result}}}")
    else:
        logging.error(f"Expected result: {{'statusCode': {statusCode}, 'statusMessage': {expected_result}}}")
    assert req_division_result(x,y) == (statusCode,expected_result), logging.error('FAILED')
    logging.info('PASSED')
