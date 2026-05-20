import os
import pandas as pd

def adresy(nazwa_pliku = 'address.csv'):
    folder_path = os.path.dirname(os.path.abspath(__file__))
    adres = pd.read_csv(os.path.join(folder_path, 'address.csv'))

    return adres
