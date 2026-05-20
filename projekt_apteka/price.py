from globals import vat
import os
import pandas as pd
from drugs import pokaz_leki

def cena_brutto(NAZWA_LEKU, ILOSC ):
    lek = pokaz_leki()
    szukany_lek = lek[lek['DRUG']==NAZWA_LEKU]
    szukana_cena = float(szukany_lek.iloc[0]['NET_PRICE'])

    brutto_szutka = szukana_cena + (szukana_cena*vat)
    laczna_cena = brutto_szutka * ILOSC
    return round(laczna_cena,2)

