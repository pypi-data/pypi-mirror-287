import os
import traceback
from psycopg2 import pool
import psycopg2
import pandas as pd 
from lb_tech_handler.common_methods import timed_execution

from dotenv import load_dotenv

load_dotenv()

CPU_COUNT = os.cpu_count()

LB_DB_HOST_NAME_OR_IP = os.getenv(key='LB_DB_HOST_NAME_OR_IP',default='db.learnbasics.fun')

LB_DB_USER_NAME = os.getenv(key='LB_DB_USER_NAME')

LB_DB_PASSWORD = os.getenv(key='LB_DB_PASSWORD')

LB_DB_PORT = os.getenv(key='LB_DB_PORT',default=7777)

LB_DB_APPLICATION_NAME = os.getenv(key='LB_DB_APPLICATION_NAME',default='LB_DB_UNNAMED_APPLICATION')

LB_DB_DATABASE_NAME = os.getenv(key='LB_DB_DATABASE_NAME',default='lb_db')

LB_DB_MIN_CONN = os.getenv(key='LB_DB_MIN_CONN',default=1)

LB_DB_MAX_CONN = os.getenv(key='LB_DB_MAX_CONN',default=CPU_COUNT)

LB_DB_LOG_FILE_PATH = os.getenv(key='LB_DB_LOG_FILE_PATH',default='db.log') 

print("PORT",LB_DB_PORT)

db_pool = pool.SimpleConnectionPool(
    minconn = LB_DB_MIN_CONN,
    maxconn = LB_DB_MAX_CONN,
    database = LB_DB_DATABASE_NAME,
    user = LB_DB_USER_NAME,
    password = LB_DB_PASSWORD,
    host = LB_DB_HOST_NAME_OR_IP,
    port = LB_DB_PORT,
    application_name = LB_DB_APPLICATION_NAME
)

def get_dataframe_from_query(query: str,args={}) -> pd.DataFrame:

    temp_conn = db_pool.getconn()

    # conn = psycopg2.connect(
    # database=db , user=username, password= password, host=host , port= port
    # )

    """returns the query as pandas dataframe from database
    Args:
    --------
        query (str): query
    
    Returns:
    ---------
        data: pandas dataframe from query
    """
    table = pd.read_sql(query, con=temp_conn,params=args)
    
    db_pool.putconn(temp_conn)
    
    return table



def excute_query(query:str,vars={}):

    try:
        conn:psycopg2.extensions.connection = db_pool.getconn()

        cursor = conn.cursor()   
        cursor.execute(query=query,vars=vars)
        conn.commit()
        
        db_pool.putconn(conn=conn)
    except Exception as e:
        db_pool.putconn(conn=conn,close=True)
        raise Exception(e)


def excute_query_and_return_result(query:str,vars={}):
    try:

        conn:psycopg2.extensions.connection = db_pool.getconn()
        
        cursor = conn.cursor()   

        cursor.execute(query=query,vars=vars)

        conn.commit()

        data =  cursor.fetchall()

        db_pool.putconn(conn=conn)

        return data
    except Exception as e:

        db_pool.putconn(conn=conn,close=True)

        raise Exception(e)

def excute_transaction(list_of_queries:list[dict]):

    try:
        conn:psycopg2.extensions.connection = db_pool.getconn()

        cursor = conn.cursor()

        for query in list_of_queries:
            cursor.execute(query=query['query'],vars=query['vars'])
        
        conn.commit()
        
        
        db_pool.putconn(conn=conn)

    except Exception as e:
        conn.rollback()

        db_pool.putconn(conn=conn,close=True)  
        
        raise Exception(e)
    
def get_connection_from_pool():
    return db_pool.getconn()

def put_connection_in_pool(conn):
    db_pool.putconn(conn=conn)

@timed_execution
def is_free_connection_in_pool():

    return LB_DB_MAX_CONN - len(db_pool._used) > 0

if __name__ == "__main__":
    # df = get_dataframe_from_query(query="select * from learnyst.ly_course_Detail")
    print(is_free_connection_in_pool())
    # print(df)