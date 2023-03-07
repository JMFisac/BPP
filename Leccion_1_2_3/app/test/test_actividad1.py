
import pytest
import app.finanzas
import pandas as pd
import numpy as np

def test_dato_correcto():
    """
    Función que prueba la función dato_correcto
    """
    # Comprobación Uso Normal con dato numérico - Transforma a float
    assert app.finanzas.dato_correcto(8,1) == float(8)
    # Comprobación Uso con String pero numérico - Transforma a float
    assert app.finanzas.dato_correcto("8",1) == float("8")
    # Comprobación Uso con Float  - Transforma a float
    assert app.finanzas.dato_correcto(8.2,1) == 8.2
    # Comprobación Uso con Bool - Transforma a 0
    assert app.finanzas.dato_correcto(True,1) == 0
    # Comprobación Uso con String letras - Transforma a 0
    assert app.finanzas.dato_correcto("aaa",1) == 0

def test_leer_archivo():
    """
    Función que prueba la función leer_archivo
    """
    # verifica que la función leer_archivo devuelve None si el nombre de archivo no existe
    test_file_name ="aaa.csv"
    assert app.finanzas.leer_archivo(test_file_name) is None
    # verifica que la función leer_archivo devuelve el archivo correcto
    df1 = pd.DataFrame({"ene": [1, 2, 3],"feb": [4, 5, 6],
                "mar": [1, 2, 3], "abr": [1, 2, 3],
                "may": [1, 2, 3],"jun": [1, 2, 3],
                "jul": [1, 2, 3], "ago": [1, 2, 3],
                "sep": [1, 2, 3],"oct": [1, 2, 3],
                "nov": [1, 2, 3], "dic": [1, 2, 3] })
    test_file_name ="test.csv"
    df1.to_csv(test_file_name, sep="\t",index=False)  
    assert df1.equals(app.finanzas.leer_archivo(test_file_name))
    # verifica que devuelve None si el archivo no tiene 12 columnas
    df3 = pd.DataFrame({"ene": [1, 2, 3],"feb": [4, 5, 6],
                "mar": [1, 2, 3], "abr": [1, 2, 3],
                "may": [1, 2, 3],"jun": [1, 2, 3],
                "jul": [1, 2, 3], "ago": [1, 2, 3],
                "sep": [1, 2, 3],"oct": [1, 2, 3],
                "nov": [1, 2, 3] })
    df3.to_csv(test_file_name, sep="\t",index=False)  
    assert app.finanzas.leer_archivo(test_file_name) is None 
   
def test_depurar_datos():
    """
    Función que prueba la función depurar_datos
    """
    # verifica que la función leer_archivo devuelve el archivo tranformado en float si no tiene errores
    df1 = pd.DataFrame({"ene": [1, 1, 1],"feb": [4, 5, 6],
                "mar": [1, 2, 3], "abr": [1, 2, 3],
                "may": [1, 2, 3],"jun": [1, 2, 3],
                "jul": [1, 2, 3], "ago": [1, 2, 3],
                "sep": [1, 2, 3],"oct": [1, 2, 3],
                "nov": [1, 2, 3], "dic": [1, 2, 3] })
    df2 = df1.astype(float)
    assert app.finanzas.depurarDatos(df1).equals(df2)
    # verifica que la función leer_archivo tranforma los posibles None a 0
    df1 = pd.DataFrame({"ene": [None, None, None],"feb": [4, 5, 6],
                "mar": [1, 2, 3], "abr": [1, 2, 3],
                "may": [1, 2, 3],"jun": [1, 2, 3],
                "jul": [1, 2, 3], "ago": [1, 2, 3],
                "sep": [1, 2, 3],"oct": [1, 2, 3],
                "nov": [1, 2, 3], "dic": [1, 2, 3] })
    df2 = pd.DataFrame({"ene": [0, 0, 0],"feb": [4, 5, 6],
                "mar": [1, 2, 3], "abr": [1, 2, 3],
                "may": [1, 2, 3],"jun": [1, 2, 3],
                "jul": [1, 2, 3], "ago": [1, 2, 3],
                "sep": [1, 2, 3],"oct": [1, 2, 3],
                "nov": [1, 2, 3], "dic": [1, 2, 3] }).astype(float)
    assert app.finanzas.depurarDatos(df1).equals(df2)
    # verifica que la función leer_archivo tranforma los posibles None a 0
    df1 = pd.DataFrame({"ene": [None, 3, 3],"feb": [4, 5, 6],
                "mar": [1, 2, 3], "abr": [1, 2, 3],
                "may": [1, 2, 3],"jun": [1, 2, 3],
                "jul": [1, 2, 3], "ago": [1, 2, 3],
                "sep": [1, 2, 3],"oct": [1, 2, 3],
                "nov": [1, 2, 3], "dic": [1, 2, 3] })
    df2 = pd.DataFrame({"ene": [0, 3, 3],"feb": [4, 5, 6],
                "mar": [1, 2, 3], "abr": [1, 2, 3],
                "may": [1, 2, 3],"jun": [1, 2, 3],
                "jul": [1, 2, 3], "ago": [1, 2, 3],
                "sep": [1, 2, 3],"oct": [1, 2, 3],
                "nov": [1, 2, 3], "dic": [1, 2, 3] }).astype(float)
    assert app.finanzas.depurarDatos(df1).equals(df2)
    # verifica que la función leer_archivo tranforma los posibles string pero numéricos en su valor float
    df1 = pd.DataFrame({"ene": ["8", 3, 3],"feb": [4, 5, 6],
                "mar": [1, 2, 3], "abr": [1, 2, 3],
                "may": [1, 2, 3],"jun": [1, 2, 3],
                "jul": [1, 2, 3], "ago": [1, 2, 3],
                "sep": [1, 2, 3],"oct": [1, 2, 3],
                "nov": [1, 2, 3], "dic": [1, 2, 3] })
    df2 = pd.DataFrame({"ene": [8, 3, 3],"feb": [4, 5, 6],
                "mar": [1, 2, 3], "abr": [1, 2, 3],
                "may": [1, 2, 3],"jun": [1, 2, 3],
                "jul": [1, 2, 3], "ago": [1, 2, 3],
                "sep": [1, 2, 3],"oct": [1, 2, 3],
                "nov": [1, 2, 3], "dic": [1, 2, 3] }).astype(float)
    assert app.finanzas.depurarDatos(df1).equals(df2)
    # verifica que la función leer_archivo tranforma los posibles string no numéricos a 0
    df1 = pd.DataFrame({"ene": ["UPS", 3, 3],"feb": [4, 5, 6],
                "mar": [1, 2, 3], "abr": [1, 2, 3],
                "may": [1, 2, 3],"jun": [1, 2, 3],
                "jul": [1, 2, 3], "ago": [1, 2, 3],
                "sep": [1, 2, 3],"oct": [1, 2, 3],
                "nov": [1, 2, 3], "dic": [1, 2, 3] })
    df2 = pd.DataFrame({"ene": [0, 3, 3],"feb": [4, 5, 6],
                "mar": [1, 2, 3], "abr": [1, 2, 3],
                "may": [1, 2, 3],"jun": [1, 2, 3],
                "jul": [1, 2, 3], "ago": [1, 2, 3],
                "sep": [1, 2, 3],"oct": [1, 2, 3],
                "nov": [1, 2, 3], "dic": [1, 2, 3] }).astype(float)
    assert app.finanzas.depurarDatos(df1).equals(df2)
   
    
