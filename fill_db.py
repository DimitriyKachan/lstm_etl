import psycopg2
import json
import requests
import pandas as pd


apikey = json.load(open('alphavantage_key.json'))["key"]
df = pd.read_csv('tickers/tickers_for_db.csv')
df['ticker_id'] = df.index


conn = psycopg2.connect(
    host='localhost',
    database='stocks',
    port=5432,
    username='postgres'
)


def insert_tickers(conn, df1):
    with conn.cursor() as cursor:
        conn.autocommit = True
        tuples = [tuple(x) for x in df1.to_numpy()]
        cols = ','.join(df1.columns)
        query = "INSERT INTO %s(%s) VALUES(%%s,%%s)" % ('public."Tickers"',
                                                        cols)
        cursor.executemany(query, tuples)
