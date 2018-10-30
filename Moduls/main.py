import Moduls.NBKI_PDL as NP
import Moduls.VKI as VKI
import Moduls.FINAL as FIN

def resp():
    response = {'status' : 'ok',
                'code' : 200,
                'result' : 'reject',
                'reason' : 'start reason',
                'approved_amount' : 0,
                'approved_period' : 0,
                'approved_frequency' : 0,
                'approved_rate':0,
                'approved_product_id':0,
                'cnt_prev':0,
                'user_id':0,
                'client_id':0,
                'application_id':0,

                
                'data' :{'app_data':{},
                        'vki_check':{},
                        'nbki_pdl_score_check':{},
                        'fin_model_limits' : {},
                        'for_kk' : {}

                        }
               }
    return response
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

    #прописываем параметры
    response['user_id'] = json_params['user_id']
    response['application_id'] = json_params['application_id']
    response['client_id'] = json_params['client_id']


    #здесь делаем внутренние проверки
    vki_result = VKI.VKI_MAIN.main(json_params)
    response['data']['vki_check'] = vki_result

    #если можно кредитовать проверяем нбки -
    response = VKI.VKI_TOTAL.main(response , json_params)

    if response['result'] == 'reject':
        response['reason'] = 'vki check'
        response['data']['for_kk'] = FIN.FIN_KK_RESPONSE.main(response)
    else:



        #если внутренние проверки ок, то получение данных нбки и оценка дефолта в ней должна быть проверка о возможности выдачи
        np_result = NP.NP_MAIN.main(json_params)
        response['data']['nbki_pdl_score_check'] = np_result

        #согласно пд смотрим можно или нельзя кредитовать
        response = FIN.FIN_NBKI_PDL.main(response)

        if response['result'] == 'reject':
            response['reason'] = 'NBKI PDL PD'
            response['data']['for_kk'] = FIN.FIN_KK_RESPONSE.main(response)

        else:


            #согласно фин модели формируем новые условия
            response = FIN.FIN_MODEL.main(response)

            #согласно новым условиям выбираем подходящий продукт
            approved_product_id = FIN.FIN_GETPRODUCT.main(response)
            response['approved_product_id'] = approved_product_id

            if response['approved_product_id'] == 0:
                response['result'] = 'reject' 
                response['reason'] = 'NO PRODUCT'
                response['data']['for_kk'] = FIN.FIN_KK_RESPONSE.main(response)
            else:
                #формируем ответ для кк
                response['reason'] = 'ALL GOOD'
                response['data']['for_kk'] = FIN.FIN_KK_RESPONSE.main(response)
    
    return response
