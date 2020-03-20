#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:29:52 2020

@author: rsi96
"""

from sqlalchemy import create_engine
db_string = "postgresql://wbauer_adb:adb2020@pgsql-196447.vipserv.org:5432/wbauer_adb"
db = create_engine(db_string)
"""
from sqlalchemy import create_engine, MetaData, Table
print(db.table_names())
metadata = MetaData()
category = Table("category", metadata , autoload=True, autoload_with=db)
film = Table("film", metadata , autoload=True, autoload_with=db)
print(repr(category))
print(category.columns.keys())


stmt = 'select * from film_category'
# Execute the statement and fetch the results
results = db.execute(stmt).fetchall()
# Print results
print(results)

from sqlalchemy.sql import select
stmt2 = select([category])
# Print the SQL query string
print(stmt2)
# Execute the statement and fetch with limit the results 
results = db.execute(stmt2).fetchmany(size=10)
print(results)

print(results[3])
#print(first_row[:][3])
print(results[3]['name'])

stmt = select([category])
# Add a where clause to filter the results
stmt = stmt.where(category.c.name == 'Comedy')
# Execute the query to retrieve all the data returned: results
results = db.execute(stmt).fetchall()
# Loop over the results and print the age and name
for result in results:
    print(result.name, result.last_update)
"""
from sqlalchemy import create_engine, MetaData, Table
#print(db.table_names())
metadata = MetaData()
staff = Table("staff", metadata , autoload=True, autoload_with=db)
country = Table("country", metadata , autoload=True, autoload_with=db)
#print(repr(staff))
#print(repr(country))
#print(staff.columns.keys())
#print(country.columns.keys())
#print(' /n /n ')
actor = Table("actor", metadata , autoload=True, autoload_with=db)
language = Table("language", metadata , autoload=True, autoload_with=db)
film = Table("film", metadata , autoload=True, autoload_with=db)
#print(repr(actor))
#print(repr(language))
#print(repr(film))
#print(actor.columns.keys())
#print(language.columns.keys())
#print(film.columns.keys())
"""
staff(address_id)address(city_id)city(country_idcountry
actor(actor_id)film_actor(film_id)film(language_id)language
"""
stmt = 'select count(distinct c.name) from category c join film_category fc on (c.category_id=fc.category_id) join film f on (fc.film_id=f.film_id) join inventory i on (f.film_id=i.film_id) join rental r on (i.inventory_id=r.inventory_id)'
# Execute the statement and fetch the results
results = db.execute(stmt).fetchall()
print(results)

stmt2 = 'select distinct c.name from category c join film_category fc on (c.category_id=fc.category_id) join film f on (fc.film_id=f.film_id) join inventory i on (f.film_id=i.film_id) join rental r on (i.inventory_id=r.inventory_id)'
results = db.execute(stmt2).fetchmany(size=2)
print(results)

stmt3 = 'select f.title, min(f.release_year) as min_year from category c join film_category fc on (c.category_id=fc.category_id) join film f on (fc.film_id=f.film_id) join inventory i on (f.film_id=i.film_id) join rental r on (i.inventory_id=r.inventory_id) group by f.title'
results = db.execute(stmt3).fetchmany(size=2)
print(results)

stmt4 = 'select f.title, max(f.release_year) as max_year from category c join film_category fc on (c.category_id=fc.category_id) join film f on (fc.film_id=f.film_id) join inventory i on (f.film_id=i.film_id) join rental r on (i.inventory_id=r.inventory_id) group by f.title'
results = db.execute(stmt4).fetchall()
print(results)

stmt4 = 'select f.release_year from category c join film_category fc on (c.category_id=fc.category_id) join film f on (fc.film_id=f.film_id) join inventory i on (f.film_id=i.film_id) join rental r on (i.inventory_id=r.inventory_id)'
results = db.execute(stmt4).fetchall()
print(results)
#all films are from 2006


from sqlalchemy.sql import select
from sqlalchemy import or_
actor = Table("actor", metadata , autoload=True, autoload_with=db)
stmt = select([actor])
stmt = stmt.where(or_(actor.c.first_name == 'Olympia', actor.c.first_name == 'Julia', actor.c.first_name == 'Ellen'))
results = db.execute(stmt).fetchall()
# Loop over the results and print the age and name
for result in results:
    print(result)
print(stmt)