import os.path

from projekt_apteka.drugs import pokaz_leki
import pandas as pd
def add_drugs(ID, DRUG, ON_RECEPT, NO_PACAKAGES_AVAILABLE, DATE, NET_PRICE):
    leki = pokaz_leki()

    nowe_leki = pd.DataFrame([{
            'ID': ID,
            'DRUG': DRUG,
            'ON_RECEPT': ON_RECEPT,
            'NO_PACAKAGES_AVAILABLE': NO_PACAKAGES_AVAILABLE,
            'DATE': DATE,
            'NET_PRICE': NET_PRICE,
    }])
    nowa_tabela = pd.concat([leki, nowe_leki], ignore_index=True)
    folder_path = os.path.dirname(os.path.abspath(__file__))
    sciezka = os.path.join(folder_path, 'drugs.xlsx')
    nowa_tabela.to_excel(sciezka, index=False)

    return f"lek {DRUG} zostal dodany do bazy lekow"