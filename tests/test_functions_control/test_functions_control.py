from Application_management.start import calc_start, calc_start_test
from Application_management.stop import calc_stop, calc_stop_test
from Application_management.restart import calc_restart, calc_restart_test
import pytest
import socket
import logging

ip_home = socket.gethostbyname(socket.gethostname())
# Проверка запуска калькулятора
@pytest.mark.parametrize('address, port, expected_result',[
    ('127.0.0.1','17678','Веб-калькулятор запущен на 127.0.0.1:17678'),
    ('127.0.0.1','','Веб-калькулятор запущен на 127.0.0.1:17678'),
    ('','','Веб-калькулятор запущен на 127.0.0.1:17678'),
    (f'{ip_home}','',f'Веб-калькулятор запущен на {ip_home}:17678')
])
def test_calc_start_positive(address, port, expected_result):
    logging.info(f'Проверка ЗАПУСКА калькулятора c адресом: "{address}" и портом: "{port}" ')
    logging.info(f'Expected result: {expected_result}')
    calc_stop()
    assert calc_start_test(address,port) == expected_result, logging.error("FAILED")
    logging.info("PASSED")
#Проверка смены ip сервера
def test_calc_change_ip():
    logging.info('Проверка СМЕНЫ --ip-- калькулятора')
    logging.info(f'Expected result: Веб-калькулятор запущен на {ip_home}:17700')
    calc_stop()
    calc_start()
    assert calc_start_test(f'{ip_home}','17700') == f'Веб-калькулятор запущен на {ip_home}:17700', logging.error("FAILED")
    logging.info("PASSED")
def test_calc_restart():
    logging.info('Проверка ПЕРЕЗАПУСКА калькулятора')
    logging.info(f'Expected result: Веб-калькулятор запущен на 127.0.0.1:17678')
    calc_start()
    assert calc_restart_test() == 'Веб-калькулятор запущен на 127.0.0.1:17678', logging.error("FAILED")
    logging.info("PASSED")
def test_calc_stop():
    logging.info('Проверка ОСТАНОВКИ калькулятора')
    logging.info(f'Expected result: Веб-калькулятор остановлен')
    assert calc_stop_test() == 'Веб-калькулятор остановлен', logging.error("FAILED")
    logging.info("PASSED")
