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

    response['result'] = 'reject'
    



    cnt_prev = response['cnt_prev']

    grey = response['data']['nbki_pdl_score_check']['grey']
    pd = response['data']['nbki_pdl_score_check']['pd']

    if grey == 1:
        response['result']  = 'approve'

    elif cnt_prev == 0 and pd <= 0.4:
        response['result']  = 'approve'
    elif cnt_prev == 1 and pd <= 0.3:
        response['result']  = 'approve'
    elif cnt_prev == 2 and pd <= 0.25:
        response['result']  = 'approve'
    elif cnt_prev == 3 and pd <= 0.15:
        response['result']  = 'approve'
    elif cnt_prev == 4 and pd <= 0.10:
        response['result']  = 'approve'
    elif cnt_prev > 4 and pd <= 0.10:
        response['result']  = 'approve'

    
    return response
