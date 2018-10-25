import requests
import os
import json
import traceback
from xml.etree import ElementTree as ET


#грузим необходимые локальные модули
import Moduls.NBKI_PDL.NP_01 as NP_01
import Moduls.NBKI_PDL.NP_02 as NP_02



def main(json_params = None):

    np_result = {}

    #NP_01
    nbki_pdl_score_check_result = NP_01.main(json_params)
    np_result.update(nbki_pdl_score_check_result)

    #NP_02
    nbki_pdl_rate = NP_02.main(nbki_pdl_score_check_result)
    np_result.update(nbki_pdl_rate)

    return np_result


