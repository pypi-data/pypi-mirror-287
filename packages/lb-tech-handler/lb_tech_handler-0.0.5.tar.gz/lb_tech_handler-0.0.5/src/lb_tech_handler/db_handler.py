import os

CPU_COUNT = os.cpu_count()

LB_DB_HOST_NAME_OR_IP = os.getenv(key='LB_DB_HOST_NAME_OR_IP',default='db.learnbasics.fun')

LB_DB_USER_NAME = os.getenv(key='LB_DB_USER_NAME')

LB_DB_PASSWORD = os.getenv(key='LB_DB_PASSWORD')

LB_DB_PORT = os.getenv(key='LB_DB_PORT',default='7777')

LB_DB_DATABASE_NAME = os.getenv(key='LB_DB_DATABASE_NAME',default='lb_db')

LB_DB_MIN_CONN = os.getenv(key='LB_DB_MIN_CONN',default=1)

LB_DB_MAX_CONN = os.getenv(key='LB_DB_MAX_CONN',default=CPU_COUNT)

LB_DB_LOG_FILE_PATH = os.getenv(key='LB_DB_LOG_FILE_PATH',default='db.log') 

print(LB_DB_PASSWORD)