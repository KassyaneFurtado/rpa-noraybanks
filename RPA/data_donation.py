import time
import pandas as pd

cases = pd.read_csv("CASES.csv")

def donationData (noraybanks, cases, line):

    noraybanks.locator('#txtReceptionDate').click() 
    time.sleep(2)
    if not pd.isnull(cases.loc[line, 'DATADECOLETA']):
        DATADECOLETA = str(cases.loc[line, 'DATADECOLETA'])
        noraybanks.fill('#txtReceptionDate', DATADECOLETA)
        noraybanks.locator('#DdListConsentMuestras').select_option('1')
        noraybanks.locator('#DDListTipoCons').click()
        noraybanks.locator('#DDListTipoCons').select_option('1')
        time.sleep(10)
        # noraybanks.wait_for_selector('#DdListConsentFirmado')
        # noraybanks.locador('#DdListConsentFirmado').click() 
        # noraybanks.locator('#DdListConsentFirmado').select_option('1')
        # time.sleep(5)
        # noraybanks.locador('#TxtFechaConsentFirma').click()
        # noraybanks.fill('#TxtFechaConsentFirma', DATADECOLETA)
        noraybanks.wait_for_selector('#BtnInsert_jqbtn').click()
        time.sleep(10)
        noraybanks.wait_for_selector('#NbctrlPopup1_ButtonOk_jqbtn').click()
        noraybanks.mouse.wheel(0, 500) 