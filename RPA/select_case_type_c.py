import time 

def selectCaseType(noraybanks, cases, positions, line):
    # Selecionar tipo de caso
    if not positions.empty:
        number = cases.loc[line, 'TIPOC']
        position = positions[positions['TIPO'] == number]
        print(f"Processando número: {number}")
        print(position)
        
        # Obter o XPath do locador
        xpath = position.iloc[0]['LOCADOR']
        
        # Selecionar a opção no menu suspenso
        print(f"XPath selecionado: {xpath}")
        print(f"Selecionando a opção: {number} com XPath: {xpath}")
        time.sleep(3)
        
        noraybanks.query_selector('#NbCtrlBiobancoNodo1_ddListNodo').click()
        noraybanks.query_selector('#NbCtrlBiobancoNodo1_ddListNodo').select_option(str(xpath))
        time.sleep(5)