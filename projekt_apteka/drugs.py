import os
import pandas as pd

def pokaz_leki(nazwa_pliku = 'drugs.xlsx'):
    folder_path = os.path.dirname(os.path.abspath(__file__))
    leki = pd.read_excel(os.path.join(folder_path, nazwa_pliku))

    return leki

