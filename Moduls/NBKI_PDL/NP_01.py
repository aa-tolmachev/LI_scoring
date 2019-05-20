import requests
import os
import json
import traceback
from xml.etree import ElementTree as ET


#NP_01 - запрос отчета pdl скора из НБКИ

def main(json_params = None):
        
        user_id = json_params['user_id']
        client_id = json_params['client_id']
        loan_amount = json_params['loan_amount']
        loan_period = json_params['loan_period']
        payment_frequency = json_params['payment_frequency']
        payment_amount = json_params['payment_amount']
        app_rate = json_params['app_rate']


        nbki_pdl_score_check_result = {}

        url = 'http://test.lendinvest.ru/service/score/{0}?inq_loan_amount={1}&inq_loan_period={2}&payment_frequency={3}&payment_amount={4}&force=true'.format(user_id,loan_amount,loan_period,payment_frequency,payment_amount)
        print('NP 01 - {0}'.format(url))
        r = requests.get(url)
        root = ET.fromstring(r.content)

        #пробегаемся по xml к примеру


        #получаем персональные данные
        for child in root[0][0][0]:
            #print (child.tag ,child.attrib, child.text)
            if child.tag == 'PersonReq':
                nbki_pdl_score_check_result['last_name'] = child.find('name1').text
                nbki_pdl_score_check_result['first_name'] = child.find('first').text
                nbki_pdl_score_check_result['birth_date'] = child.find('birthDt').text


        #получаем данные по паспартам
        for child in root[0][1][0]:
            if child.tag == 'IdReply':
                nbki_pdl_score_check_result['idType'] = child.find('idType').text
                nbki_pdl_score_check_result['seriesNumber']  = child.find('seriesNumber').text
                nbki_pdl_score_check_result['idNum']  = child.find('idNum').text

        #смотрим данные по скорингу
        score = 0
        exclusionCode = 0

        if root.find('productScore') is not None:

            for score_info in root.findall('productScore'):
                if score_info.find('scoreID').text == 'PDL':
                    if score_info.find('exclusionCode') is not None:
                        exclusionCode = score_info.find('exclusionCode').text
                    if score_info.find('score') is not None:
                        score = score_info.find('score').text

        nbki_pdl_score_check_result['score'] = int(score) 
        nbki_pdl_score_check_result['exclusionCode'] =  exclusionCode

        return nbki_pdl_score_check_result
