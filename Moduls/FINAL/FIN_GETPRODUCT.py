import requests
import os
import json
import traceback
from xml.etree import ElementTree as ET

import mysql.connector as sql
import pandas as pd

import Tech.mysql_connect as mysql_con


#8. своевременное погашение, без просрочки в течение 6-х месяцев - улучшение условий согласно бизнес плану

def main(response = None):
        
        approved_rate = response['approved_rate']
        approved_amount = response['approved_amount']



        approved_rate_min = int(approved_rate * 365 * 100 - 15)
        approved_rate_max = int(approved_rate * 365 * 100 + 15)



        vki_check = 0

        mysql_settings = mysql_con.mysql_con()



        db_connection = sql.connect(user=mysql_settings['user'], password=mysql_settings['password'],
                                      host=mysql_settings['host'],
                                      database=mysql_settings['database'])
        db_cursor = db_connection.cursor()
        
        sql_script = (' ').join(['select min(id) as product_id',
                                'from cc_products',
                                'where active = 1',
                                'and max_credit_limit >= {0}'.format(approved_amount),
                                'and min_credit_limit <= {0}'.format(approved_amount),
                                'and interest_rate >= {0}'.format(approved_rate_min),
                                'and interest_rate <= {0}'.format(approved_rate_max)

                                ])

        db_cursor.execute(sql_script)

        table_rows = db_cursor.fetchall()

        df = pd.DataFrame(table_rows, columns=db_cursor.column_names)

        db_connection.close()

        if df.shape[0] > 0:
            vki_check = df['product_id'][0]
        else:
            vki_check = 0


        return vki_check
