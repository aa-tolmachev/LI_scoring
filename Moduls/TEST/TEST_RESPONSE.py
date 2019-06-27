import requests
import os
import json
import traceback




def main(json_params = None ,response = None):

    is_test_response = 0

    user_id = int(json_params['user_id'])
    client_id = int(json_params['client_id'])
    application_id = int(json_params['application_id'])
    loan_amount = int(json_params['loan_amount'])
    loan_period = int(json_params['loan_period'])
    payment_frequency = int(json_params['payment_frequency'])
    payment_amount = int(json_params['payment_amount'])
    app_rate = int(json_params['app_rate'])
 

    is_test_sum = user_id + client_id + application_id + loan_amount + loan_period + payment_frequency + payment_amount + app_rate

    if is_test_sum == 0:
        is_test_response = 1

        response['result'] = 'approve'

    else:
        is_test_response = 0


    return is_test_response , response
