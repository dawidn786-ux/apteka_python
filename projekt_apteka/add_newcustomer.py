from projekt_apteka.customers import klienci
from adres import adresy
import pandas as pd
import os
import random

def add_customer(NAME, E_MAIL, PHONE, CREATED, UPDATED, STREET, CITY, COUNTRY):
    ID= random.randint(1000,9999)
    klient = klienci()
    nowy_klient = pd.DataFrame([{
        'ID': ID,
        'NAME': NAME,
        'E-MAIL': E_MAIL,
        'PHONE': PHONE,
        'CREATED': CREATED,
        'UPDATED': UPDATED,
    }])

    nowa_tabela = pd.concat([klient, nowy_klient], ignore_index=True)

    adres = adresy()
    nowy_adres = pd.DataFrame([{
    'ID': ID,
    'STREET': STREET,
    'CITY': CITY,
    'COUNTRY': COUNTRY,
    }])

    nowa_tabela = pd.concat([adres, nowy_adres], ignore_index=True)

    file_path = os.path.dirname(os.path.abspath(__file__))

    sciezka_adres = os.path.join(file_path, 'address.csv')
    nowa_tabela.to_csv(sciezka_adres, index=False)

    sciezka_klient = os.path.join(file_path, 'customer.csv')
    nowa_tabela.to_csv(sciezka_klient, index = False)

    sciezka_DATABASE = os.path.join(file_path, 'DATABASE', f"{ID}.txt")
    with open(sciezka_DATABASE,'w') as plik:
        plik.write(f"Historia zakupow klienta ID:{ID}:\n")

    return f"klient {NAME} ID:{ID} zostal dodany do bazy danych"

