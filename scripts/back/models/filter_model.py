from sqlalchemy import create_engine
import pandas as pd
import os

def engine_creator():
    bd_name = os.getenv('DB_NAME')
    bd_pass = os.getenv('DB_PASS')
    bd_user = os.getenv('DB_USER')
    bd_host = os.getenv('DB_HOST')
    bd_url = 'postgres://' + bd_user + ':' + bd_pass + '@' + bd_host + '/' + bd_name
    engine = create_engine(bd_url)
    return engine


def table_query(query, engine=engine_creator()):
    df = pd.read_sql_query(query, con=engine)
    return (df)

def table_builder(table, array_filters= []):
    base= "select * from " + str(table)
    if len(array_filters) > 0:
        base = base + " where " + array_filters.pop(0)
        if len(array_filters) >0:
            for el in array_filters:
                base = base + " and " + el
    print(base)
    print("++++++++++++++++++++++++++++++++++++")
    tabla = table_query(base)
    return tabla

#departments, crear el filter builder

# Test de fillter builder so it can be iterated or used the pop pytho

def filter_builder(dict_values ):
    filters = []
    for el in dict_values:
        filters.append(" " + str(el)+ " in " + str(dict_values[el]).replace("[", "(").replace("]",")")+ " " )
    return filters

