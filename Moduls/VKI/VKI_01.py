import requests
import os
import json
import traceback
from xml.etree import ElementTree as ET

import mysql.connector
from pandas import DataFrame

import Tech.mysql_connect as mysql_con


#1 есть активный кредит

def main(json_params = None):
        
        user_id = json_params['user_id']
        client_id = json_params['client_id']
        loan_amount = json_params['loan_amount']
        loan_period = json_params['loan_period']
        payment_frequency = json_params['payment_frequency']
        payment_amount = json_params['payment_amount']
        app_rate = json_params['app_rate']


        vki_01 = 0

        mysql_settings = mysql_con.mysql_con()



        db_connection = sql.connect(user='ext_tolmachev_a', password='Pi*m4?nx1s|ZFH4AV}}f|WHBOJ#OF@~r',
                                      host='37.143.14.122',
                                      database='_dev_lendinvest')
        db_cursor = db_connection.cursor()
        
        sql_script = (' ').join(['select case when count(found_rows()) > 0 then 1 else 0 end as rule_check',
                                'from cc_contracts',
                                "where client_id = {0} and status in ('CREATED' , 'ACTIVE')".format(client_id)
                                ])

        db_cursor.execute(sql_script)

        table_rows = db_cursor.fetchall()

        df = pd.DataFrame(table_rows, columns=db_cursor.column_names)

        db_connection.close()

        vki_01 = df['rule_check'][0]


        return vki_01
