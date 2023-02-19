from db.run_sql import run_sql

from models.destination import Destination 
from models.trek import Trek 

import repositories.trek_repository as trek_repository 

def delete_all():
    sql = "DELETE FROM destinations"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM destinations WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    destinations = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        destination = Destination(row['destination_name'], row ['country'], row ['continent'], row ['id'])
        destinations.append(destination)
    return destinations 

def select(id):
    destination = None
    sql = "SELECT * FROM destinations WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        destination = Destination(result['destination_name'], result ['country'], result ['continent'], result ['id'])
    return destination 

def save(destination):
    sql = "INSERT INTO destinations (destination_name, country, continent) VALUES (%s, %s, %s) RETURNING *"
    values = [destination.destination_name, destination.country, destination.continent]
    results = run_sql(sql, values)
    id = results [0]['id']
    destination.id = id
    return destination 
