import pymysql
import sys
sys.path.append('..')
from dbconfig import host,user,password,db_name
try:
    connection=pymysql.connect(
        host=host,
        user=user,
        password=password,
        port=3306,
        cursorclass=pymysql.cursors.DictCursor,
        database=db_name,
    )
       
except Exception as ex:
    # finally:
    #     connection.close()
    print("connection refused with: ", ex)
