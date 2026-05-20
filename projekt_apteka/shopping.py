import os
from datetime import datetime
import pandas as pd
from drugs import pokaz_leki

def kupowanie_leku(ID, NAZWA_LEKU, ILOSC, numer_recepty = "brak"):
    leki = pokaz_leki()
    szukany_lek = leki[leki['DRUG']==NAZWA_LEKU]

    if szukany_lek.empty:
        return f"nie ma takiego leku ({NAZWA_LEKU}) w naszym asortymencie"

    czy_recepta = szukany_lek.iloc[0]['ON_RECEPT']
    dostepna_ilosc = int(szukany_lek.iloc[0]['NO_PACKAGES_AVAILABLE'])

    if dostepna_ilosc < ILOSC:
        return f"nie ma wystarczajacej ilosc towaru"
    if czy_recepta == 'Yes' and numer_recepty == "Brak":
        return f"lek {NAZWA_LEKU} jest na recepte, prosze podac numer recepty"

    file_path = os.path.dirname(os.path.abspath(__file__))
    sciezka = os.path.join(file_path,'DATABASE', f'{ID}.txt')

    if not os.path.exists(sciezka):
        return f"klient o numerze ID {ID} nie istnieje"

    czas = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open (sciezka, 'a', encoding='utf-8') as plik:
        wpis = f" Data: {czas}, Lek: {NAZWA_LEKU}, Ilość: {ILOSC} szt. Recepta: {numer_recepty}\n"
        plik.write(wpis)

    nowa_ilosc = dostepna_ilosc - ILOSC
    leki.loc[leki['DRUG']==NAZWA_LEKU,'NO_PACKAGES_AVAILABLE'] = nowa_ilosc

    sciezka_drug = os.path.join(file_path, 'drugs.xlsx')
    leki.to_excel(sciezka_drug,index= False)
    return f"Klient ID {ID} kupil lek {NAZWA_LEKU} w ilosci {ILOSC}"



