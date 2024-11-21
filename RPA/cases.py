import time

import os
from dotenv import load_dotenv

from playwright.sync_api import sync_playwright

import pandas as pd
import utils
import navegador
import load_data

from select_case_type_c import selectCaseType
from data_case import caseData
from data_donation import donationData

load_dotenv()

login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
samples = load_data.loadSamples()
positions = load_data.loadPositions()
cases = load_data.loadCases()


with sync_playwright() as p:
    noraybanks = utils.createBrowser(p)

    navegador.login(noraybanks)

    try:
        for line in cases.index:
            noraybanks.wait_for_selector('#wrapper-250 > ul > li.opt1 > a')
            noraybanks.locator('#wrapper-250 > ul > li.opt1 > a').click()
            time.sleep(5)
            noraybanks.wait_for_selector('#wrapper-250 > ul > li.opt1 > ul > li.opt100 > a > span')
            noraybanks.locator('#wrapper-250 > ul > li.opt1 > ul > li.opt100 > a > span').click() 
            time.sleep(5)
            noraybanks.locator('#NbCtrlBiobancoNodo1_ddListBiobanco').select_option('1')
            time.sleep(5)
            selectCaseType(noraybanks, cases, positions, line)
            caseData(noraybanks, cases, line)
            donationData(noraybanks, cases, line)
            
            #SE HOUVER AMOSTRAS COM O MESMO PRONTUÁRIO DO CASO NA PLANILHA SAMPLE PUXAR AS FUNÇÕES DE LANÇAMENTO DE AMOSTRAS
     
     
    finally:
        noraybanks.query_selector('#Header1_NbCurrentProfile1_ButtonLogOut_jqbtn').click()
        time.sleep(20)
        navegador.close()

