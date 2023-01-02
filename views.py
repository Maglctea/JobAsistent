import service
from models import *


def add_job():
    name = input('Введите название работы:\n>>> ')
    description = input('Введите описание работы:\n>>> ')
    salary = int(input('Введите размер зарплаты:\n>>> '))
    skills = input('Введите ключевые навыки в одну строку через пробел:\n>>> ').strip().split()

    print('Выберите тип работы:')
    for job_type in service.get_job_type():
        print(f'{job_type.id_type}). {job_type.name_type}')
    job_type = int(input('>>> '))

    job = service.add_job(name=name, description=description, salary=salary, id_type=job_type)

    if skills:
        service.add_skill(id_job=job.id_job, name=skills)
    print('Вакансия добавлена')
    input('Для продолжения введите Enter')


def get_job():
    name = input('Введите название работы:\n>>> ')
    jobs = service.get_job(name, True)

    if jobs:
        for job in jobs:
            skills = []
            for skill in job.skills:
                skills.append(skill.name_skill)

            print(f'{"-" * 20}'
                  f'\n-Наименование: {job.name_job};'
                  f'\n-Тип работы: {service.get_job_type(job.id_type)};'
                  f'\n-Описание: {job.description_job};'
                  f'\n-Требуемые навыки: {", ".join(skills)};'
                  f'\n-Зарплата: {job.salary} руб.')
    else:
        print('Вакансий не найдено')
    input('Для продолжения введите Enter')


def get_all_jobs():
    jobs = service.get_job('*', True)
    if jobs:
        for job in jobs:
            print(f'ID: {job.id_job} Наименование: {job.name_job}')
    else:
        print('Вакансий не найдено')

    input('Для продолжения введите Enter')
