import subprocess

def calc_help():
    # Выполняем команду "-help" и возвращаем её вывод
    return subprocess.check_output('./webcalculator --help').decode('cp1251')