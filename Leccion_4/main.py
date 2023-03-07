#import pdb
#pdb.set_trace()

def get_maxs(listas):
    """
    Devuelve una lista con los numeros máximos de cada lista
    
    Parámetros:
    -----------
    listas([list]): Lista de listas
    
    Return:
    -------
    Lista con los máximos
    """
    maximos = [max(i) for i in listas]
    return maximos

def es_primo(n):
    """
    Función que nos devuelve True or False dependiendo si el número es primo.
    Para ello hago una comprobación de división, comprobando el resto de la división
    
    Parámetros:
    -----------
    n(int): El numero que comprobamos
    
    Return:
    -------
    True/False: si es primo o no
    """
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def filter_primos(numeros):
    """
    Dado una lista de n números devuelva aquellos que son primos.
    
    Parámetros:
    -----------
    numeros(list(int)): Lista de enteros
    
    Return:
    -------
    Lista con los numeros primos
    """
    return list(filter(es_primo,numeros))

if __name__ == "__main__":
    listas = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
    # Compruebo la parte 1 del ejercicio
    print(get_maxs(listas))
    # Compruebo los numeros primos del ejemplo
    ejemplo = [3,4,8,5,5,22,13]
    print(filter_primos(ejemplo))
    # Compruebo los numeros primos de las listas del punto 1
    print([filter_primos(i) for i in listas])
    
