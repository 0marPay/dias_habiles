import os
import re
import pandas as pd

def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, text, re.IGNORECASE)
    return emails

def print_lista(lista):
    [print(i,'-',l) for i,l in enumerate(lista)]; print()

def obtener_archivo():
    # Filtrar los archivos que terminan con ".xlsx"
    carpeta = "correos_pepsico"
    archivos = [carpeta + "/" + archivo for archivo in os.listdir(carpeta) if archivo.endswith(".xlsx")]
    print("Archivos:"); print_lista(archivos)

    archivo = int(input("Ingrese su el número correspondiente al ARCHIVO: "))
    archivo = archivos[archivo]
    print("Ha seleccionado el archivo:", archivo); print()
    return archivo

def obtener_datos(archivo):
    # Leer el archivo Excel
    df = pd.read_excel(archivo)
    df = df.fillna('')
    # Agrupar los correos electrónicos por "Planta" y "Tipo de Queja"
    grouped_emails = df.apply(lambda row: extract_emails(" ".join(row[2:])), axis=1)
    df["Correos"] = grouped_emails
    return df[["Planta", "Tipo de Queja", "Correos"]]

def obtener_planta(df):
    plantas = df['Planta'].unique()
    plantas = [p for p in plantas if p != ""]
    print("Plantas:"); print_lista(plantas)
    planta = int(input("Ingrese su el número correspondiente a la PLANTA: "))
    planta = plantas[planta]
    print("Ha seleccionado la PLANTA:", planta); print()
    return planta, df[(df['Planta'] == planta)]

def obtener_tipo_queja(df):
    tipos_quejas = df["Tipo de Queja"].unique()
    tipos_quejas = [tq for tq in tipos_quejas if tq != ""]
    print("Tipo de Queja:"); print_lista(tipos_quejas)
    tipo_queja = int(input("Ingrese su el número correspondiente al TIPO DE QUEJA: "))
    tipo_queja = tipos_quejas[tipo_queja]
    print("Ha seleccionado el TIPO DE QUEJA", tipo_queja); print()
    return tipo_queja, df[(df['Tipo de Queja'] == tipo_queja)]

def imprimir_correos(df, planta, tipo_queja):
    correos = df["Correos"]
    correos = correos.tolist()[0]
    print("Representante:"); print(correos[0])
    del correos[0]
    print("Con copia:") 
    print(', '.join(correos))

archivo = obtener_archivo()
df = obtener_datos(archivo)
planta, df = obtener_planta(df)
tipo_queja, df = obtener_tipo_queja(df)
imprimir_correos(df, planta, tipo_queja)