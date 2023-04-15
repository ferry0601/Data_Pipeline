import os
import connection
import sqlparse
import pandas as pd
import datetime as dt


if __name__ == '__main__':
    print('[info] Starting...')
    #connection data source
    lod = connection.config('commerce')
    conn, engine = connection.conn_psql(lod, 'Data Source')
    cursor = conn.cursor()

    #connection data source
    lod_dwh = connection.config('dwh')
    conn_dwh, engine_dwh = connection.conn_psql(lod_dwh, 'Data WareHouse')
    cursor_dwh = conn_dwh.cursor()


    #create schema dwh
    path_schema_dwh = os.getcwd() +'/query/'
    schema_dwh = sqlparse.format(
        open(path_schema_dwh+'schema_ingest.sql','r').read(), strip_comment=True
    ).strip()


    #getquery
    path_query = os.getcwd() +'/query/'
    query1 = sqlparse.format(
        open(path_query+'query1.sql','r').read(), strip_comment=True
    ).strip()

    query2 = sqlparse.format(
        open(path_query+'query2.sql','r').read(), strip_comment=True
    ).strip()

    query3 = sqlparse.format(
        open(path_query+'query3.sql','r').read(), strip_comment=True
    ).strip()
    
    try:
        #define or getdata
        df1 = pd.read_sql(query1, engine)
        df2 = pd.read_sql(query2, engine)
        df3 = pd.read_sql(query3, engine)

        
        df_merge1 = df1.merge(df2, on='product_id', how='left')
        df_full = df_merge1.merge(df3,on='customer_id', how='left')
        
        # delete missing value
        df_miss=df_full.dropna(axis=1)
        #df_loc=df_miss.loc[10]

        #print getdata
        #print(df_loc)
        #print(df_miss)

        #create schema
        cursor_dwh.execute(schema_dwh)
        conn_dwh.commit()

        #ingest to dwh
        df_miss.to_sql('dim_market', engine_dwh, if_exists='append', index=False)
        print('[info] Ingest data is success...')

        #get csv
        datetime_now = dt.datetime.now().strftime('%Y%m%d')
        file = f'dim_market_{datetime_now}.csv'
        path_output = os.getcwd() +'/output/'
        df_miss.to_csv(f'{path_output}/{file}',index=False)

        #create data mart
        os.system(f'python mapReduce.py output/{file} > \
                  output/data_mart_result.txt') 
        
        #convert txt to csv
        read_file = pd.read_csv(f'{path_output}/data_mart_result.txt')
        read_file.to_csv (f'{path_output}/data_mart_result.csv', index=None)

    except Exception as e:
        print('[INFO] Not Success')
    
