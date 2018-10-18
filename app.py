from flask import Flask
from flask import request
import requests
from flask import make_response
import os
import json
import traceback


from xml.etree import ElementTree as ET


#

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
        #todo - clean # when ready to prod
        #getData = str(request.get_data())
        #json_params = json.loads(getData)
        
        #у димы запросить какой формат вызова меня
        #беру юзер айди и направляю запрос на скоринг
        user_id = 14

        url = 'http://test.lendinvest.ru/service/score/'+str(user_id)
        r = requests.get(url)
        root = ET.fromstring(r.content)

        #todo это пример, переделать под реальный запрос
        #пробегаемся по xml к примеру
        for child in root[0][0][0]:
            #print (child.tag ,child.attrib, child.text)
            if child.tag == 'PersonReq':
                last_name = child.find('name1').text
                response['data']['last_name'] = last_name
                #for child_2 in child:
                    #print (child_2.tag ,child_2.attrib, child_2.text)
        
        
    except:
        response['status'] = 'error'
        response['code'] = 501
        
    return str(response)
        


if __name__ == "__main__":
    #heroku
    port = int(os.getenv('PORT', 5000))
    application.run(debug=False, port=port, host='0.0.0.0')
    #local
    #application.run()