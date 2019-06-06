import requests
import os
import json
import traceback
from xml.etree import ElementTree as ET

import mysql.connector as sql
import pandas as pd

import Tech.mysql_connect as mysql_con


def make_value(response=None, key1 = None, key2 = None, key3 = None, key4 = None,value_type='str'):
    if value_type == 'str':
        value_s = ''
    else:
        value_s = -1
        
    if key1 is not None and key1 in response.keys():
        value = response[key1]
        if key2 is not None and key2 in value.keys():
            value = value[key2]
            if key3 is not None and key3 in value.keys():
                value = value[key3]
                if key4 is not None and key4 in value.keys():
                    value = value[key4]
        
    if  type(value) is dict:
        value = value_s
    

    #work with missing values
    if value is None:
        if value_type == 'str':
            value = 'missing'
        else:
            value = 9999

    
    return value

def main(response = None ):

    status = 200

    mysql_settings = mysql_con.mysql_con()


    db_connection = sql.connect(user=mysql_settings['user'], password=mysql_settings['password'],
                                  host=mysql_settings['host'],
                                  database=mysql_settings['database'])
    
    db_cursor = db_connection.cursor()
    

    mysql_scoring_result = (

        make_value(response, key1 = 'application_id', key2 = None, key3 = None, key4 = None,value_type='int')
        ,make_value(response, key1 = 'approved_amount', key2 = None, key3 = None, key4 = None,value_type='int')
        ,make_value(response, key1 = 'approved_frequency', key2 = None, key3 = None, key4 = None,value_type='int')
        ,make_value(response, key1 = 'approved_period', key2 = None, key3 = None, key4 = None,value_type='int')
        ,make_value(response, key1 = 'approved_product_id', key2 = None, key3 = None, key4 = None,value_type='int')
        ,make_value(response, key1 = 'approved_rate', key2 = None, key3 = None, key4 = None,value_type='int')
        ,make_value(response, key1 = 'client_id', key2 = None, key3 = None, key4 = None,value_type='int')
        ,make_value(response, key1 = 'cnt_prev', key2 = None, key3 = None, key4 = None,value_type='int')
        ,make_value(response, key1 = 'code', key2 = None, key3 = None, key4 = None,value_type='int')
        ,make_value(response, key1 = 'reason', key2 = None, key3 = None, key4 = None,value_type='str')
        ,make_value(response, key1 = 'result', key2 = None, key3 = None, key4 = None,value_type='str')
        ,make_value(response, key1 = 'status', key2 = None, key3 = None, key4 = None,value_type='str')
        ,make_value(response, key1 = 'user_id', key2 = None, key3 = None, key4 = None,value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'app_data', key3 = 'loan_amount',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'app_data', key3 = 'loan_period',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'app_data', key3 = 'payment_frequency',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'app_data', key3 = 'payment_amount',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'app_data', key3 = 'app_rate',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'app_data', key3 = 'product_id',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'vki_check', key3 = 'bad_amount',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'vki_check', key3 = 'bad_rate',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'vki_check', key3 = 'last_amount',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'vki_check', key3 = 'vki_01',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'vki_check', key3 = 'vki_02',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'vki_check', key3 = 'vki_03',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'vki_check', key3 = 'vki_04',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'vki_check', key3 = 'vki_05',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'vki_check', key3 = 'vki_06',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'vki_check', key3 = 'vki_07',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'vki_check', key3 = 'vki_08',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'nbki_pdl_score_check', key3 = 'score',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'nbki_pdl_score_check', key3 = 'exclusionCode',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'nbki_pdl_score_check', key3 = 'grey',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'nbki_pdl_score_check', key3 = 'pd',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'nbki_pdl_score_check', key3 = 'pd_check_error',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'fin_model_limits', key3 = 'fin_amount',value_type='int')
        ,make_value(response, key4 = None, key1 = 'data', key2 = 'fin_model_limits', key3 = 'fin_rate',value_type='int')
        
        
        
    )


    sql_script = (' ').join(['insert into scoring_main (application_id , approved_amount , approved_frequency , approved_period , approved_product_id , approved_rate,client_id,cnt_prev,code,reason,`result`,status,user_id,app_data_loan_amount,app_data_loan_period,app_data_payment_frequency,app_data_payment_amount,app_data_app_rate,app_data_product_id,vki_check_bad_amount,vki_check_bad_rate,vki_check_last_amount,vki_check_vki_01,vki_check_vki_02,vki_check_vki_03,vki_check_vki_04,vki_check_vki_05,vki_check_vki_06,vki_check_vki_07,vki_check_vki_08,nbki_score,nbki_exclusionCode,nbki_grey,nbki_pd,nbki_pd_check_error,model_fin_amount,model_fin_rate )',
                                "VALUES {0}".format(mysql_scoring_result)
                                ])
    print(sql_script)

    try:
       db_cursor.execute(sql_script)
       db_connection.commit()
    except Exception:
       print('FIN_DB_INSERT' , traceback.format_exc())
       db_connection.rollback()
    

    db_connection.close()
    
    print('sql done!')
    return status
