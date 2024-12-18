import time

from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

import navegador
import utils
import load_data

from select_study_group import selectStudyGroup
from select_case_type import selectCaseTypeS
from search_record import searchRecord
from select_sample_type import selectSampleType
from select_case import caseSelect
from data_sample import sampleData

load_dotenv()

samples = load_data.loadSamples()
positions = load_data.loadPositions()

#ABRINDO O NAVEGADOR 
with sync_playwright() as p:
    noraybanks = utils.createBrowser(p)

    navegador.login(noraybanks)

    try:
        for line in samples.index:
            selectStudyGroup(noraybanks)
            selectCaseTypeS(noraybanks, samples, positions, line)
            searchRecord(noraybanks, samples, line)
            caseSelect (noraybanks)
            
            time.sleep(3)

            selectSampleType(noraybanks, samples, positions, line)
            sampleData(noraybanks, line)
            time.sleep(2)
            
            noraybanks.wait_for_selector('#NbctrlPopup1_ButtonOk_jqbtn')
            noraybanks.locator('#NbctrlPopup1_ButtonOk_jqbtn').click()
            
            time.sleep(7)
            
            noraybanks.mouse.wheel(0, 2000)
            noraybanks.wait_for_selector('#wrapper-250')

    except Exception as e:
        print(e)

    finally:
        noraybanks.query_selector('#Header1_NbCurrentProfile1_ButtonLogOut_jqbtn').click()
        time.sleep(20)
        navegador.close()

