import requests
import os
import json
import traceback
from xml.etree import ElementTree as ET


#NP_02 - оценка уровня дефолта согласно рекомендациям нбки

def main(nbki_pdl_score_check_result = None):
        
        nbki_pdl_rate = {}

        grey = 0
        pd = 1
        pd_check_error = 0

        score = nbki_pdl_score_check_result['score']
        exclusionCode = nbki_pdl_score_check_result['exclusionCode']

        if exclusionCode != 0:
            pd_check_error = 1
        elif score == 0:
            grey = 1
        else:
            if score < 360:
                pd = 0.92
            elif score < 420:
                pd = 0.82
            elif score < 450:
                pd = 0.72
            elif score < 480:
                pd = 0.61
            elif score < 510:
                pd = 0.49
            elif score < 540:
                pd = 0.37
            elif score < 570:
                pd = 0.28
            elif score < 600:
                pd = 0.20
            elif score < 630:
                pd = 0.13
            elif score < 660:
                pd = 0.08
            elif score < 690:
                pd = 0.05
            elif score < 720:
                pd = 0.03
            elif score < 750:
                pd = 0.02
            elif score < 780:
                pd = 0.01
            else:
                pd = 0


        nbki_pdl_rate['grey'] = grey
        nbki_pdl_rate['pd'] = pd
        nbki_pdl_rate['pd_check_error'] = pd_check_error
        
        return nbki_pdl_rate
