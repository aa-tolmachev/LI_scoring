import requests
import os
import json
import traceback
from xml.etree import ElementTree as ET


#грузим необходимые локальные модули
import Moduls.VKI.VKI_01 as VKI_01




def main(json_params = None):

    vki_result = {}

    #NP_01
    vki_01_res = VKI_01.main(json_params)
    vki_result['vki_01'] = vki_01_res



    return vki_result


