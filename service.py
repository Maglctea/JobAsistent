from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from models import *

engine = create_engine('sqlite:///JobAsistent.sqlite', echo=False)

session = sessionmaker(bind=engine)
s: Session = session()


def add_job(name, description, salary, id_type):
    job = Job(name_job=name, description_job=description, salary=salary, id_type=id_type)
    s.add(job)
    s.commit()
    return job


def add_skill(id_job, name):
    if type(name) == str:
        skill = Skill(id_job=id_job, name_skill=name)
        s.add(skill)
    elif type(name) == list:
        for skill in name:
            add_skill(id_job=id_job, name=skill)
    s.commit()


def get_job(name, many=False):
    if name == '*':
        return s.query(Job).all()
    if many:
        return s.query(Job).filter_by(name_job=name).all()
    else:
        return s.query(Job).filter_by(name_job=name).first()


def get_job_type(id_type=None):
    if id_type is None:
        return s.query(JobType).all()
    else:
        return s.query(JobType).get(id_type)