from flask import Flask
from flask import request
import requests
from flask import make_response
import os
import json
import traceback



from xml.etree import ElementTree as ET


from Moduls import main


application = Flask(__name__)  # Change assignment here

#test
@application.route("/")  
def hello():
    return "Hello World!"

@application.route('/score/v1', methods=['GET', 'POST'])  
def score_v1():
    response = {'status' : 'ok',
                'code' : 200,
                'data' :{}
               }
    try:
        getData = request.get_data()
        json_params = json.loads(getData) 
        
        #json_params = {'user_id':16,
        #              'client_id':1,
        #              'application_id':40,
        #              'loan_amount':3000,
        #              'loan_period':14,
        #              'payment_frequency':1,
        #              'payment_amount':3550,
        #              'app_rate':0.022}



        

        result = main.main(json_params)
        response['data'] = result
        #принтим на всякий случай
        print(response)

        #ответ согласно ответу Димы
        response = response['data']['data']['for_kk']


        
        
    except:
        traceback.print_exc()
        response['status'] = 'error'
        response['code'] = 501


    response = json.dumps(response)
    print(response)
    return str(response)
        


if __name__ == "__main__":
    #heroku
    port = int(os.getenv('PORT', 5000))
    application.run(debug=False, port=port, host='0.0.0.0')
    #local
    #application.run()