import subprocess

def calc_h():
    #Выполняем команду "-h" и возвращаем её вывод
    return subprocess.check_output('./webcalculator -h').decode('cp1251')