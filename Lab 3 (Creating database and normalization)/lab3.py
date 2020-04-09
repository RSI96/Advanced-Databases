#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:28:34 2020

@author: rsi96
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker
"""
data_set = (len('Radosław') + len('Sikora'))% 6
print(data_set)
"""
#data set number 2
"""
#create db
db_string = "postgres://postgres:postgres@localhost:5432/postgres"
engine = create_engine(db_string)

conn = engine.connect()
conn.execute("commit")
conn.execute("create database AB_NYC_2019")
conn.close()
"""

#create declarative base
db_string = "postgres://postgres:postgres@localhost:5432/ab_nyc_2019"
engine = create_engine(db_string)

Base = declarative_base()

class Place(Base):
    __tablename__ = 'places'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    host_id = Column(Integer, ForeignKey("hosts.id"))
    location_id = Column(Integer, ForeignKey("locations.id"))
    parameters_id = Column(Integer, ForeignKey("parameters.id"))
    reviews_id = Column(Integer, ForeignKey("reviews.id"))

    def __repr__(self):
        return "<places(id='{0}', name={1}, host_id={2}, location_id={3}, parameters_id={4}, reviews_id={5})>".format(
            self.id, self.name, self.host_id, self.location_id, self.parameters_id, self.reviews_id)

class Host(Base):
    __tablename__ = 'hosts'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return "<hosts(id='{0}', name={1})>".format(
            self.id, self.name)

class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    neighbourhood_group = Column(String(50))
    neighbourhood = Column(String(50))
    latitude = Column(Float)
    longitude = Column(Float)

    def __repr__(self):
        return "<locations(id='{0}', neighbourhood_group={1}, neighbourhood={2}, latitude={3}, longitude={4})>".format(
            self.id, self.neighbourhood_group, self.neighbourhood, self.latitude, self.longitude)

class Parameter(Base):
    __tablename__ = 'parameters'
    id = Column(Integer, primary_key=True)
    room_type = Column(String(50))
    price = Column(Integer)
    minimum_nights = Column(Integer)
    calculated_host_listings_count = Column(Integer)
    availability_365 = Column(Integer)

    def __repr__(self):
        return "<parameters(id='{0}', room_type={1}, price={2}, minimum_nights={3}, calculated_host_listings_count={4}, availability_365={5})>".format(
            self.id, self.room_type, self.price, self.minimum_nights, self.calculated_host_listings_count, self.availability_365)

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    number_of_reviews = Column(Integer)
    last_review = Column(Date)
    reviews_per_month = Column(Float)

    def __repr__(self):
        return "<reviews(id='{0}', number_of_reviews={1}, last_review={2}, reviews_per_month={3})>".format(
            self.id, self.number_of_reviews, self.last_review, self.reviews_per_month)

#adding multiple tables 
Base.metadata.create_all(engine)