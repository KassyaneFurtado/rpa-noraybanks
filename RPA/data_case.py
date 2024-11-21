import time
import pandas as pd

cases = pd.read_csv("CASES.csv")

def caseData(noraybanks, cases, line):
        #DIGITAR PRONTUÁRIO
        if not pd.isnull(cases.loc[line, "PRONTUARIO"]):
                noraybanks.wait_for_selector('#TxtCodDonante')
                noraybanks.locator('#TxtCodDonante').click()
                prontuario = str(int(cases.loc[line, "PRONTUARIO"]))
                noraybanks.fill('#TxtCodDonante', prontuario)

        noraybanks.locator('#DDListEspecie').select_option('2')     
        noraybanks.locator('#checkBoxDatosFiliacion').click()
        noraybanks.locator('#BtnAceptar_jqbtn').click()
        noraybanks.locator('#NbctrlPopup1_ButtonOk_jqbtn').click()
        time.sleep(10)
        #SELECIONAR CENTRO DE ESTUDO
        noraybanks.locator('#DDListCentro').select_option('2')
        time.sleep(10)
        #PREENCHER DADOS PESSOAIS DO DOADOR
        
        NOME1 = str(cases.loc[line, "NOME1"])
        noraybanks.locator('#txtNombre').click()
        noraybanks.fill('#txtNombre' , NOME1)

        NOME2 = str(cases.loc[line, "NOME2"])
        noraybanks.locator('#txtApe1').click()
        noraybanks.fill('#txtApe1', NOME2)

        NOME3 = str(cases.loc[line, "NOME3"])
        noraybanks.locator('#txtApe2').click()
        noraybanks.fill('#txtApe2', NOME3)

        DATANASCIMENTO = str(cases.loc[line, "DATANASCIMENTO"])
        noraybanks.locator('#TxtFechaNac').click()
        noraybanks.fill('#TxtFechaNac', DATANASCIMENTO)
        noraybanks.locator('#divFormularioFiliacion > div').click()

        noraybanks.locator('#TxtHistoria').click()
        noraybanks.fill('#TxtHistoria', prontuario)

        noraybanks.locator('#DDSexo').click()
        if cases.loc[line, 'SEXO'] == 1:
                noraybanks.locator('#DDSexo').select_option('1')
        else:
                noraybanks.locator('#DDSexo').select_option('2')
        noraybanks.locator('#divFormularioFiliacion > div').click()

        noraybanks.locator('#ImgNewDon').click()
        time.sleep(5)
        noraybanks.locator('#NbctrlPopup1_ButtonYes_jqbtn').click()
        time.sleep(5)
        noraybanks.locator('#NbctrlPopup1_ButtonOk_jqbtn').click()
        time.sleep(5)