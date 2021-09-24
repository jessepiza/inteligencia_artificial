from itertools import permutations
import numpy as np

class CriptoAritmetica:
    letras_iniciales = []
    
    def __init__(self, lista_palabras, resultado):
        self.estado_inicial = lista_palabras
        self.palabras = lista_palabras
        self.resultado = resultado
        self.letras_iniciales = [palabra[0] for palabra in self.palabras+[self.resultado]]
        
    def pintar_estado(self, estado):
        return
    
    def acciones_aplicables(self, estado):
#         count = 0
#         list_letra = ['-' for i in range(10)]
#         for palabra in self.palabras + [self.resultado]:
#             for letra in palabra:
#                 if letra not in list_letra:
#                     list_letra[count] = letra
#                     count += 1
        lista_letras = [letra for palabra in self.palabras + [self.resultado] for letra in palabra ]
        lista_letras = list(set(lista_letras))
            
        digitos = range(10)
        for permutacion in permutations(digitos, len(lista_letras)):
            solucion = dict(zip(lista_letras, permutacion))
            if any(solucion[letra]==0 for letra in self.letras_iniciales[:-1]):
                continue
            palabras_sol = []
            for palabra in self.palabras + [self.resultado]:
                sum_palabra = 0
                for i in reversed(range(len(palabra))):
                    sum_palabra += np.power(10,i)*solucion[palabra[len(palabra)-1-i]]
                palabras_sol.append(sum_palabra)
                
            if np.sum(palabras_sol[:-1]) == palabras_sol[-1]:
                return palabras_sol, solucion
        return None
    
    def transicion(self, estado, indices):
        return
    
    def test_objetivo(self, estado):
        return
    
    def costo(self, estado, accion):
        return 0