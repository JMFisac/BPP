#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 00:09:56 2023

@author: jaime munoz fisac
"""
import pandas as pd
import matplotlib.pyplot as plt

filename = "finanzas2020.csv"

class ColumnsNumberError(Exception):
    """
    Clase de excepción personalizada para
    el error de número de columnas
    """
    def __init__(self,columns_number):
        self.columns_number=columns_number
        
def dato_correcto(dato, mes):
    """
    Función que convierte un dato, float, int o string de un numero a float y
    maneja el error si no es numérico

       Parámetros:
            dato(?): dato a tranformar
            mes(str): Mes

       Return:
            dato(float) - Dato transformado a float si es posible, si no 0
    """
    try:
        if type(dato) == float  or type(dato) == int or type(dato) == str:
            return float(dato) 
        raise ValueError
    except ValueError: 
        print( f"El dato {dato} en el mes {mes} no es numérico, se sustituirá por 0.")
        return 0
    

def leer_archivo(archivo):
    """
    Función que lee un archivo CSV y 
    devuelve un dataframe de pandas
       
       Parámetros:
            archivo(str): "nombre_archivo.csv"

       Return:
            df(Dataframe): dataframe con el csv descargado
    """
    try:
       df = pd.read_csv(archivo, sep='\t')
       if len(df.columns) != 12:
            raise ColumnsNumberError(len(df.columns))
       
    except FileNotFoundError:
        # Error cuando no existe el fichero
        print("El archivo no existe.")
        return None

    except ColumnsNumberError as e:
        # Error cuando no tiene 12 columnas
        columns_number = e.args[0]
        print(f'El archivo no tiene 12 columnas, tiene {columns_number}.')
        return None
    
    except Exception as e:
        # Error si df es None y lanzará la excepción la comprobar df.columns
        print(f'El archivo no se descargó correctamente')
        return None

    else:
        return df
        
def depurarDatos(df):
    """
    Función que depura los datos del dataframe
    y los convierte a float

       Parámetros:
            df(Dataframe): Dataframe a depurar

       Return:
            df(Dataframe): Dataframe depurado
    """
    for mes in df.columns:
        try:
            if df[mes].isnull().all():
                raise ValueError(f"Todos los valores del mes {mes} son nulos.")
            if df[mes].isnull().any():
                raise ValueError(f"Hay valores Nulos en el mes {mes}.")
        except ValueError as e:
            df[mes] = df[mes].fillna(0)
            print(e)
        except Exception as e:
            print(e)
        finally:
            df[mes] = df[mes].apply(dato_correcto,mes=mes)
    return df
        
if __name__ == "__main__":    
    
    df = leer_archivo(filename)
    if not df is None:
        df = depurarDatos(df)
        
        gasto_mensual = df.apply(lambda x: x[x < 0].sum(), axis=0)
        mes_gasto_max = gasto_mensual.idxmin()
        print(f"Mes en el que se ha gastado más: {mes_gasto_max}.")
        
        balance_mensual = df.sum(axis=0) 
        mes_ahorro_max = balance_mensual.idxmax()
        print(f"Mes en el que se ha ahorrado más: {mes_ahorro_max}.")
        
        media_gastos_año = gasto_mensual.mean()
        print(f"La media de gastos anual es: {media_gastos_año}.")
        
        gastos_totales = gasto_mensual.sum()
        print(f"Los gastos totales del año son: {gastos_totales}.")
        
        ingresos_mesuales = df.apply(lambda x: x[x > 0].sum(), axis=0)
        plt.plot(ingresos_mesuales)
        plt.title("Gastos mensuales")
        plt.xlabel("Mes")
        plt.xticks(rotation=45)
        plt.ylabel("Gasto (€)")
        plt.savefig('grafica.png')
        plt.show()



