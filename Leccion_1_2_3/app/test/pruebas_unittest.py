
import unittest
import sys
import os
# get current directory
path = os.getcwd()
# parent directory
parent = os.path.dirname(path)
# appending a path
sys.path.append(parent)

import finanzas
import pandas as pd

class PruebasUnitarias(unittest.TestCase):
    def test_dato_correcto(self):
        """
        Función que prueba la función dato_correcto
        """
        # Comprobación Uso Normal con dato numérico - Transforma a float
        self.assertEqual(finanzas.dato_correcto(8,1),float(8))
        # Comprobación Uso con String pero numérico - Transforma a float
        self.assertEqual(finanzas.dato_correcto("8",1),float("8"))
        # Comprobación Uso con Float  - Transforma a float
        self.assertEqual(finanzas.dato_correcto(8.2,1),8.2)
        # Comprobación Uso con Bool - Transforma a 0
        self.assertEqual(finanzas.dato_correcto(True,1),0)
        # Comprobación Uso con String letras - Transforma a 0
        self.assertEqual(finanzas.dato_correcto("aaa",1),0)

    def test_leer_archivo(self):
        """
        Función que prueba la función leer_archivo
        """
        # verifica que la función leer_archivo devuelve None si el nombre de archivo no existe
        test_file_name ="aaa.csv"
        self.assertIsNone(finanzas.leer_archivo(test_file_name))
        # verifica que la función leer_archivo devuelve el archivo correcto
        df1 = pd.DataFrame({"ene": [1, 2, 3],"feb": [4, 5, 6],
                "mar": [1, 2, 3], "abr": [1, 2, 3],
                "may": [1, 2, 3],"jun": [1, 2, 3],
                "jul": [1, 2, 3], "ago": [1, 2, 3],
                "sep": [1, 2, 3],"oct": [1, 2, 3],
                "nov": [1, 2, 3], "dic": [1, 2, 3] })
        test_file_name ="test.csv"
        df1.to_csv(test_file_name, sep="\t",index=False)  
        self.assertTrue(finanzas.leer_archivo(test_file_name).equals(df1))
        # verifica que devuelve None si el archivo no tiene 12 columnas
        df3 = pd.DataFrame({"ene": [1, 2, 3],"feb": [4, 5, 6],
                    "mar": [1, 2, 3], "abr": [1, 2, 3],
                    "may": [1, 2, 3],"jun": [1, 2, 3],
                    "jul": [1, 2, 3], "ago": [1, 2, 3],
                    "sep": [1, 2, 3],"oct": [1, 2, 3],
                    "nov": [1, 2, 3] })
        df3.to_csv(test_file_name, sep="\t",index=False)  
        self.assertIsNone(finanzas.leer_archivo(test_file_name)) 
   
    def test_depurar_datos(self):
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
        self.assertTrue(finanzas.depurarDatos(df1).equals(df2))
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
        self.assertTrue( finanzas.depurarDatos(df1).equals(df2))
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
        self.assertTrue( finanzas.depurarDatos(df1).equals(df2))
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
        self.assertTrue( finanzas.depurarDatos(df1).equals(df2))
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
        self.assertTrue( finanzas.depurarDatos(df1).equals(df2))

if __name__=='__main__':
    unittest.main()