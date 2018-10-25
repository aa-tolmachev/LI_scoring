import Moduls.NBKI_PDL as NP


def resp():
    response = {'status' : 'ok',
                'code' : 200,
                'result' : 'denied',
                'reason' : 'start reason',
                'approved_amount' : 0,
                'approved_period' : 0,
                'approved_frequency' : 0,
                'approved_rate':0,
                'user_id':0,
                'client_id':0,
                'data' :{'app_data':{},
                        'vki_check':{},
                        'nbki_pdl_score_check':{},
                        'final_check':{}
                        }
               }

    return response


def app_data(json_params = None):
    app_data = {'loan_amount':json_params['loan_amount'],
               'loan_period':json_params['loan_period'],
               'payment_frequency':json_params['payment_frequency'],
               'payment_amount':json_params['payment_amount'],
               'app_rate':json_params['app_rate']}

    return app_data

def main(json_params = None):

    response = resp()

    #получаем данные по заявк
    response['data']['app_data'] = app_data(json_params)

    #здесь делаем внутренние проверки


    #если внутренние проверки ок, то получение данных нбки и оценка дефолта в ней должна быть проверка о возможности выдачи
    np_result = NP.NP_MAIN.main(json_params)
    response['data']['nbki_pdl_score_check'] = np_result

    #формируем итог

    return response
