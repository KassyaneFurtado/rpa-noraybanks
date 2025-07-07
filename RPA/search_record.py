import pandas as pd

def searchRecord(noraybanks, samples, line):
    # Buscar amostra por prontuário
    if not pd.isnull(samples.loc[line, "PRONTUARIO"]):
        noraybanks.wait_for_selector('#nbConsulta1_TxtCodigoUnico')
        noraybanks.locator('#nbConsulta1_TxtCodigoUnico').click()
        prontuario = str(int(samples.loc[line, "PRONTUARIO"]))
        print(prontuario)
        noraybanks.fill('#nbConsulta1_TxtCodigoUnico', prontuario)
        noraybanks.wait_for_selector('#btnFiltro_jqbtn')
        noraybanks.locator('#btnFiltro_jqbtn').click()

    else:
        noraybanks.wait_for_selector('#nbConsulta1_TxtCodigoApp').click()
        codigonb = str(samples.loc[line, "NB"])
        print(codigonb)
        noraybanks.wait_for_selector('#btnFiltro_jqbtn')
        noraybanks.locator('#btnFiltro_jqbtn').click()

