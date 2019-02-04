import requests
import os
import json
import traceback
from xml.etree import ElementTree as ET

import mysql.connector as sql
import pandas as pd

import Tech.mysql_connect as mysql_con


#9. если в течение недели есть 2 отказные заявки то отказ

def main(json_params = None):
        
        user_id = json_params['user_id']
        client_id = json_params['client_id']
        loan_amount = json_params['loan_amount']
        loan_period = json_params['loan_period']
        payment_frequency = json_params['payment_frequency']
        payment_amount = json_params['payment_amount']
        app_rate = json_params['app_rate']


        vki_check = 0

        mysql_settings = mysql_con.mysql_con()



        db_connection = sql.connect(user=mysql_settings['user'], password=mysql_settings['password'],
                                      host=mysql_settings['host'],
                                      database=mysql_settings['database'])
        db_cursor = db_connection.cursor()
        
        sql_script = (' ').join(['select case when count(found_rows()) > 1 then 1 else 0 end as rule_check',
                                'from cc_applications',
                                'where client_id = {0}'.format(client_id),
                                "and  DATEDIFF(created_at, now()) > -7",
                                "and status = 'REJECTED'"
                                ])

        db_cursor.execute(sql_script)

        table_rows = db_cursor.fetchall()

        df = pd.DataFrame(table_rows, columns=db_cursor.column_names)

        db_connection.close()

        vki_check = df['rule_check'][0]


        return vki_check
