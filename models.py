from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


engine = create_engine('sqlite:///JobAsistent.sqlite', echo=False)
Base = declarative_base()


class Skill(Base):
    __tablename__ = 'skill'

    id_skill = Column(Integer, primary_key=True)
    id_job = Column(Integer, ForeignKey('job.id_job'))
    name_skill = Column(String(25))

    def __str__(self):
        return self.name_skill


class Job(Base):
    __tablename__ = 'job'

    id_job = Column(Integer, primary_key=True)
    name_job = Column(String(100))
    id_type = Column(Integer, ForeignKey('job_type.id_type'))
    description_job = Column(String(500), nullable=True)
    salary = Column(Integer, nullable=True)

    skills = relationship('Skill', backref="job")

    def __str__(self):
        return self.name_job

class JobType(Base):
    __tablename__ = 'job_type'

    id_type = Column(Integer, primary_key=True)
    name_type = Column(String(15))

    def __str__(self):
        return self.name_type


Base.metadata.create_all(engine)
