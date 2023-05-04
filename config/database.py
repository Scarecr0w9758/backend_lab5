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
    # print('success connected')
    # print(connection)

    # try:
    #     #cursor=connection.cursor()
    #     #create table
    #     # with connection.cursor() as cursor:
    #     #     create_table_query="CREATE TABLE `users`(id int AUTO_INCREMENT,\
    #     #                         name varchar(32),\
    #     #                         password varchar(32),\
    #     #                         email varchar(32), PRIMARY KEY (id));"
    #     #     cursor.execute(create_table_query)
    #     #     print("created table executed right")
    #  #insert
    #     with connection.cursor() as cursor:
    #         tmp_name='vlad'
    #         tmp_password='123'
    #         tmp_email='be@killed.ru'
    #         insert_query= f"INSERT INTO `users` (name,password,email) VALUES  ('{tmp_name}','{tmp_password}','{tmp_email}');"
    #         cursor.execute(insert_query)
    #         connection.commit()
    #         print("insert successfully")

    
    #     # with connection.cursor() as cursor:
    #     #     select_all_rows="SELECT * FROM `USERS`"
    #     #     cursor.execute(select_all_rows)
    #     #     rows=cursor.fetchall()
    #     #     for row in rows:
    #     #         print('row: ', row)
    #     #     print('#'*20)  


   
       
except Exception as ex:
    # finally:
    #     connection.close()
    print("connection refused with: ", ex)
