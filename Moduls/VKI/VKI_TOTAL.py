import requests
import os
import json
import traceback
from xml.etree import ElementTree as ET

import mysql.connector as sql
import pandas as pd

import Tech.mysql_connect as mysql_con

import Moduls.VKI.VKI_LASTAMOUNT as VKI_LA
import Moduls.VKI.VKI_APP_PRODUCT as VKI_AP



def main(response = None , json_params=None):

    result = 'reject'
    approved_amount = 0
    approved_period = 0
    approved_frequency = 0
    approved_rate = 0
    cnt_prev = 0
    app_product = 0

    vki_result = response['data']['vki_check']
    app_data = response['data']['app_data']

    result_cnt_prev = vki_result['vki_08']
    cnt_prev = result_cnt_prev

    #отказ
    result_info = vki_result['vki_01'] + vki_result['vki_05']  + vki_result['vki_09'] 
    if result_info == 0:
        result = 'approve'

    #ставку изменяем
    result_rate = vki_result['vki_02']*0.002 + vki_result['vki_03']*0.004 + vki_result['vki_04']*0.004
    current_rate = app_data['app_rate']
    approved_rate = current_rate + result_rate

    response['data']['vki_check']['bad_rate'] = 1 if result_rate > 0 else 0


    #лимит изменяем
    last_amount = VKI_LA.main(json_params)

    result_amount_change = vki_result['vki_04'] * 0.5 + vki_result['vki_07'] * 0.5
    result_amount_not_change = vki_result['vki_06']

    if result_amount_not_change:
        approved_amount = last_amount
    elif result_amount_change > 0:
        approved_amount = last_amount * (1 - result_amount_change)
    elif cnt_prev == 0:
        approved_amount = response['data']['app_data']['loan_amount']
    else:
        approved_amount = response['data']['app_data']['loan_amount']

    response['data']['vki_check']['last_amount'] = last_amount
    response['data']['vki_check']['bad_amount'] = 1 if result_amount_change > 0 else 0

    #период изменяем
    approved_period = response['data']['app_data']['loan_period']
    #частоту изменяем
    approved_frequency = response['data']['app_data']['payment_frequency']

    #получаем продукт
    app_product = VKI_AP.main(json_params)
    response['data']['app_data']['product_id'] = app_product


    #обновляем данные
    response['result'] = result
    response['approved_amount'] = approved_amount
    response['approved_period'] = approved_period
    response['approved_frequency'] = approved_frequency
    response['approved_rate'] = approved_rate
    response['cnt_prev'] = cnt_prev

    return response
