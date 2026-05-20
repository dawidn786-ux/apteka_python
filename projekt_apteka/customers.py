import os
import pandas as pd

def klienci(nazwa_pliku = 'customer.csv'):
    folder_path = os.path.dirname(os.path.abspath(__file__))
    klient = pd.read_csv(os.path.join(folder_path, nazwa_pliku))

    return klient
