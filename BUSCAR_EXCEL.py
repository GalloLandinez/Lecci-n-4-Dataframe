 #programacion para buscar el excel estando en cualquier parte del pc

import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
archivo_excel = askopenfilename(
    title="GGGGGGGGGG",
    filetypes=[("AAAAAAAA", "*.xlsx *.xls"), 
               ("Todos los archivos", "*.*")])

if archivo_excel:
    df = pd.read_excel(archivo_excel)
    print("Archivo cargado correctamente:")
    print(df.head())
else:
    print("No se seleccionó ningún archivo")