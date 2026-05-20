import os.path
import os
import pandas as pd
from customers import klienci
from adres import adresy
def usuwanie_klienta(ID):
    baza_danych_klientow = klienci()
    ID = int(ID)

    tabela_usuniety_klient= baza_danych_klientow[baza_danych_klientow['ID']!= ID ]
    file_path = os.path.dirname(os.path.abspath(__file__))
    sciezka_klienta = os.path.join(file_path, 'customer.csv')

    tabela_usuniety_klient.to_csv(sciezka_klienta,index=False)

    baza_adresow = adresy()
    tabela_bez_adresu = baza_adresow[baza_adresow['ID']!= ID]
    sciezka_adresow = os.path.join(file_path, 'address.csv')
    tabela_bez_adresu.to_csv(sciezka_adresow, index=False)

    sciezka_DATABASE = os.path.join(file_path, 'DATABASE', f'{ID}.txt')
    if os.path.exists(sciezka_DATABASE):
        os.remove(sciezka_DATABASE)

    return f"klient o identyfikatorze ID {ID} zostal usuniety"