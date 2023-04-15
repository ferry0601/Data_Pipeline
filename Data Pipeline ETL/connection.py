from sqlalchemy import create_engine
import pandas as pd
import os
import json
import psycopg2


#connection
def config(connection_db):
        f = open('config.json')
        lod = json.load(f)[connection_db]
        return lod



def conn_psql(lod, name_conn):
        try:
            conn = psycopg2.connect(
                  host = lod['host'],
                  database = lod['db'],
                  user = lod['user'],
                  password = lod['password'],
                  port = lod['port']
            )
            print(f'[info] Successed {name_conn}')
            engine = create_engine(f"postgresql+psycopg2://{lod['user']}:{lod['password']}@{lod['host']}:{lod['port']}/{lod['db']}")
            return conn, engine
        except:
            print(f'Not Success {name_conn}')
