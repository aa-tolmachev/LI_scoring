import requests
import os
import json
import traceback
from xml.etree import ElementTree as ET


#грузим необходимые локальные модули
import Moduls.VKI.VKI_01 as VKI_01
import Moduls.VKI.VKI_02 as VKI_02
import Moduls.VKI.VKI_03 as VKI_03
import Moduls.VKI.VKI_04 as VKI_04
import Moduls.VKI.VKI_05 as VKI_05
import Moduls.VKI.VKI_06 as VKI_06
import Moduls.VKI.VKI_07 as VKI_07
import Moduls.VKI.VKI_08 as VKI_08


def main(json_params = None):

    vki_result = {}

    #VKI_01
    vki_01_res = VKI_01.main(json_params)
    vki_result['vki_01'] = vki_01_res

    #VKI_02
    vki_02_res = VKI_02.main(json_params)
    vki_result['vki_02'] = vki_02_res

    #VKI_03
    vki_03_res = VKI_03.main(json_params)
    vki_result['vki_03'] = vki_03_res

    #VKI_04
    vki_04_res = VKI_04.main(json_params)
    vki_result['vki_04'] = vki_04_res

    #VKI_05
    vki_05_res = VKI_05.main(json_params)
    vki_result['vki_05'] = vki_05_res

    #VKI_06
    vki_06_res = VKI_06.main(json_params)
    vki_result['vki_06'] = vki_06_res

    #VKI_07
    vki_07_res = VKI_07.main(json_params)
    vki_result['vki_07'] = vki_07_res

    #VKI_08
    vki_08_res = VKI_08.main(json_params)
    vki_result['vki_08'] = vki_08_res

    return vki_result


