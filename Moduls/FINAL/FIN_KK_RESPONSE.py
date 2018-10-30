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

    for_kk = {}
    for_kk['application_id'] = response['application_id']
    for_kk['decision'] = response['result']
    for_kk['change'] = {}

    if for_kk['decision'] == 'approve':
        if response['approved_amount'] != response['data']['app_data']['loan_amount']:
            for_kk['change']['sum'] = response['approved_amount']
        if response['approved_period'] != response['data']['app_data']['loan_period']:
            for_kk['change']['period'] = response['approved_period']
        if response['approved_product_id'] != response['data']['app_data']['product_id']:
            for_kk['change']['product_id'] = response['approved_product_id']



    
    return for_kk
