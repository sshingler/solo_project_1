from db.run_sql import run_sql

from models.trek import Trek
from models.destination import Destination

import repositories.destination_repository as destination_repository 

def delete_all():
    sql = "DELETE FROM treks"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM treks WHERE id = %s"
    values = [id]
    run_sql(sql, values) 

def select_all():
    treks = []

    sql = "SELECT * FROM treks"
    results = run_sql(sql)

    for row in results:
        destination = destination_repository.select(row['destination_id'])
        trek = Trek(row['trek_name'], row ['trek_distance'], row ['trek_days'], row ['trek_headline'], row ['trek_completed'], row ['trek_notes'], destination, row ['id'])
        treks.append(trek)
    return treks 

def select(id):
    trek = None
    sql = "SELECT * FROM treks WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        destination = destination_repository.select(result['destination_id'])
        trek = Trek(result['trek_name'], result ['trek_distance'], result ['trek_days'], result ['trek_headline'], result['trek_completed'], result ['trek_notes'], destination, result ['id'])
    return trek 

def save(trek): 
    sql = "INSERT INTO treks (trek_name, trek_distance, trek_days, trek_headline, trek_completed, trek_notes, destination_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [trek.trek_name, trek.trek_distance, trek.trek_days, trek.trek_headline, trek.trek_completed, trek.trek_notes, trek.destination.id]
    results = run_sql(sql, values)
    id = results [0]['id']
    trek.id = id 
    return trek 

def update(trek):
    sql = "UPDATE treks SET (trek_name, trek_distance, trek_days, trek_headline, trek_completed, trek_notes, destination_id ) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [trek.trek_name, trek.trek_distance, trek.trek_days, trek.trek_headline, trek.trek_completed, trek.trek_notes, trek.destination.id, trek.id]
    print(values)
    run_sql(sql, values)
    