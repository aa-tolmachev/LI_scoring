import requests
import os
import json
import traceback
from xml.etree import ElementTree as ET

import mysql.connector as sql
import pandas as pd


"""
    {
    application_id: <int>,
    decision: <string:approve|reject>,
    // change: {}, // объект пуст если апрувим или отклоняем без изменения заявки
    change: {
    sum: <int|null>, // значение проставляются только в том свойстве, которое надо изменить
    period: <int|null>, // пример: поменять только период - period: 10, sum: null, product_id: null
    product_id: <int|null>, // если будут указаны все поля, то у заявки сначала будет изменен продукт, а потом остальные поля
    }
}
"""


def main(response = None ):

    approved_amount = response['approved_amount']
    approved_rate = response['approved_rate']
    cnt_prev = response['cnt_prev']

    bad_amount = response['data']['vki_check']['bad_amount']
    bad_rate = response['data']['vki_check']['bad_rate']
    last_amount = response['data']['vki_check']['last_amount']



    
    if cnt_prev == 0:
        fin_amount = 1000
    elif cnt_prev == 1:
        fin_amount = 3000
    elif cnt_prev == 2:
        fin_amount = 5500
    elif cnt_prev == 3:
        fin_amount = 6500
    elif cnt_prev == 4: 
        fin_amount = 7500
    elif cnt_prev == 5:
        fin_amount = 8000
    elif cnt_prev == 6: 
        fin_amount = 8500
    elif cnt_prev ==7:
        fin_amount = 9000
    elif cnt_prev == 8:
        fin_amount = 9500
    elif cnt_prev == 9:
        fin_amount = 10000
    else:
        fin_amount = 15000

    response['data']['fin_model_limits']['fin_amount'] = fin_amount

    if bad_amount == 0:
        if fin_amount <= approved_amount:
            approved_amount = fin_amount

    response['approved_amount'] = approved_amount

    if cnt_prev == 0:
        fin_rate = 0.022
    elif cnt_prev == 1:
        fin_rate = 0.019
    elif cnt_prev == 2:
        fin_rate = 0.016
    elif cnt_prev == 3:
        fin_rate = 0.016
    elif cnt_prev == 4: 
        fin_rate = 0.015
    elif cnt_prev == 5:
        fin_rate = 0.015
    elif cnt_prev == 6: 
        fin_rate = 0.014
    elif cnt_prev ==7:
        fin_rate = 0.014
    elif cnt_prev == 8:
        fin_rate = 0.013
    elif cnt_prev == 9:
        fin_rate = 0.013
    else:
        fin_rate = 0.01


    response['data']['fin_model_limits']['fin_rate'] = fin_rate

    if bad_rate == 0:
        if fin_rate >= approved_rate:
            approved_rate = fin_rate

    response['approved_rate'] = approved_rate

    

    
    return response
