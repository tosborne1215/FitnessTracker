#!/usr/bin/python3


from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Numeric, Date
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///data/fitness.sqlite')
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    runtimes = relationship("RunTime", back_populates="user",
                            cascade="all, delete, delete-orphan")
    weights = relationship("Weight", back_populates="user",
                           cascade="all, delete, delete-orphan")

    def __repr__(self):
        return "<User(name='%s'>" % self.name


class RunTime(Base):
    __tablename__ = 'runtimes'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="runtimes")
    distance = Column(Numeric, nullable=True)
    time = Column(Numeric, nullable=True)

    def __repr__(self):
        return "<User(name='%s'>" % self.name


class Weight(Base):
    __tablename__ = 'weights'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="weights")
    weight = Column(Numeric)
    occurence = Column(Date, nullable=True)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()
session.commit()
