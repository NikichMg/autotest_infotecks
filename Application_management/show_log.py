import subprocess

def calc_show_log():
    # Выполняем команду "show_log" и возвращаем её вывод
    return subprocess.check_output('./webcalculator show_log').decode('cp1251')
