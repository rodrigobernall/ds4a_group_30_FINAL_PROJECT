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

def agg_builder_percent(table= "personas", agg_val="p6020", agg_val2= "dpto"):
    base= """with temp as (SELECT dpto, p6020, count(*) AS percentage 
            FROM   personas 
            group by 1,2)
            
            select t.dpto, t.p6020, float4(t.percentage)/cuenta as percentage
            from temp t
            left join (select dpto, count(*) as cuenta from personas group by 1) t2
            on t.dpto =t2.dpto
            """.replace("personas", table).replace("p6020", agg_val).replace("dpto", agg_val2)
    tabla = table_query(base)
    return tabla


def agg_builder_count(table="personas", agg_val="p6020", agg_val2="dpto", filter = "1=1"):
    base = """SELECT dpto, p6020, count(*) AS total 
            FROM   personas where filter_a
            group by 1,2
            """.replace("personas", table).replace("p6020", agg_val).replace("dpto", agg_val2).replace("filter_a", filter)
    tabla = table_query(base)
    return tabla

def group_rows(table="personas", agg_val="p6020", agg_val2="dpto", filter = "1=1"):
    base = """SELECT dpto, p6020
            FROM   personas where filter_a
            group by 1,2
            """.replace("personas", table).replace("p6020", agg_val).replace("dpto", agg_val2).replace("filter_a", filter)
    tabla = table_query(base)
    return tabla

def total_expansion(table="area_personas", agg_val="p6020", agg_val2="p6040", filter = "1=1"):
    base = """SELECT dpto, p6020,
                round(sum(fex_c_2011)) as total
            FROM   personas where filter_a
            group by 1,2
            """.replace("personas", table).replace("p6020", agg_val).replace("dpto", agg_val2).replace("filter_a", filter)
    tabla = table_query(base)
    return tabla


#departments, crear el filter builder

# Test de fillter builder so it can be iterated or used the pop pytho

def filter_builder(dict_values ):
    filters = []
    for el in dict_values:
        filters.append(" " + str(el)+ " in " + str(dict_values[el]).replace("[", "(").replace("]",")")+ " " )
    return filters

