#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:28:11 2020

@author: rsi96
"""

data_set = (len('Radosław') + len('Sikora'))% 6
print(data_set)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

"""
#create db
db_string = "postgres://postgres:postgres@localhost:5432/postgres"
engine = create_engine(db_string)

conn = engine.connect()
conn.execute("commit")
conn.execute("create database test")
conn.close()
"""

#create declarative base
db_string = "postgres://postgres:postgres@localhost:5432/test"
engine = create_engine(db_string)

Base = declarative_base()

from sqlalchemy import Column, Integer, String, Date

#create tables
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))
    born_date = Column(Date)

    def __repr__(self):
        return "<authors(id='{0}', name={1}, surname={2}, born_date={3})>".format(
            self.id, self.name, self.surnamey, self.born_date)
        
from sqlalchemy import ForeignKey

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    id_author = Column(Integer, ForeignKey('authors.id'))
    original_title = Column(String, nullable = False)
    publication_date = Column(Integer, nullable = False)
    original_language = Column(String(), nullable = False)

#adding multiple tables 
Base.metadata.create_all(engine)

#adding one table
#Book.__table__.create(engine)

from sqlalchemy.orm import sessionmaker

#create sessions
Session = sessionmaker(bind=engine)
session = Session() #begin

author1 = Author(name = 'William', surname = 'Shakespeare', born_date = '26.04.1564')
author2 = Author(name = 'Albert', surname = 'Camus', born_date = '7.11.1913')

#one per line
session.add(author1)
session.add(author2)

session.commit() #end

Session = sessionmaker(bind=engine)
session = Session() #begin

book1 = Book(id_author = 1 ,original_title = 'Hamlet', publication_date= 1603, original_language = 'english')
book2 = Book(id_author = 1, original_title = 'King Lear', publication_date= 1606, original_language = 'english')
book3 = Book(id_author = 2, original_title = 'La Peste', publication_date= 1947, original_language = 'french')

#multiple
records_list = [book1, book2, book3]
session.add_all(records_list)

session.commit() #end

