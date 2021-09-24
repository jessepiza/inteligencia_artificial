from copy import deepcopy
from itertools import product
import numpy as np

class CriptoAritmetica():
    def __init__(self, lista_palabras):
        self.palabras = lista_palabras
        self.lista_letras = [letra for palabra in self.palabras for letra in palabra ]
        self.lista_letras = list(set(self.lista_letras))
        self.estado_inicial = {letra:None for letra in self.lista_letras}
        self.letras_iniciales = [palabra[0] for palabra in self.palabras]
        
    def pintar_estado(self, estado):
        return
        
    def transicion(self, estado, accion):
        estado_copy = deepcopy(estado)
        estado_copy[accion[0]] = accion[1]
        return estado_copy
    
    def acciones_aplicables(self, estado):
        digitos_disponibles = [d for d in range(10) if d not in estado.values()]
        letras_disponibles = [d for d in self.lista_letras if estado[d] == None]
        acciones = list(product(digitos_disponibles, letras_disponibles))
        print(acciones)
        acciones = acciones.remove((0, 'm'))
        return acciones
    
    def test_objetivo(self, estado):
        palabras_sol = []
        for palabra in self.palabras:
            for letra in palabra:
                palabra = palabra.replace(letra, str(estado[letra]))
            try:
                num_palabra = int(palabra)
                palabras_sol.append(num_palabra)
            except:
                return False
        return np.sum(palabras_sol[:-1]) == palabras_sol[-1]   
        
    def codigo(self, estado):
        return estado
    
    def costo(self, estado, accion):
        return 0
        