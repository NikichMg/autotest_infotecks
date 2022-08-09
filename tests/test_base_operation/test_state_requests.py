from operation.state import req_state_result
import logging

#Проверка статуса сервера
def test_req_state_serv():
    logging.info('ПРОВЕРКА СОСТОЯНИЯ СЕРВЕРА')
    logging.info(f'Expected result: ОК')
    assert req_state_result() == (0, 'OК'), logging.error('FAILED')
    logging.info('PASSED')
    logging.info(' ')