from views import *
TEXT_MENU = '--------- Меню ---------\n1). Добавить вакансию.\n2). Найти работу.\n3). Список всех вакансий\noff - Завершить работу\n>>> '

request = input(TEXT_MENU)
while request != 'off':
    if request == '1':
        add_job()
    elif request == '2':
        get_job()
    elif request == '3':
        get_all_jobs()
    else:
        print('Неизвестный параметр')
    request = input(TEXT_MENU)