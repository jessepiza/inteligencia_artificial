from copy import deepcopy
import matplotlib.pyplot as plt
from itertools import product, permutations
import numpy as np
from PIL import Image, ImageDraw, ImageFont

class CriptoAritmetica():
    '''
    Problema de las ocho reinas, el cual consiste en poner ocho reinas en un tablero de ajerdez de tal manera que ninguna pueda atacar a las demás.
    Estado inicial: Ninguna letra ha sido reemplazada por algún dígito.
    Posibles acciones: Reemplazar todas las veces que aparezca un dígito que no haya aparecido en el problema.
    Función de transiciones: Reemplazar una acción que permita establecer un nuevo dígito a una letra.
    Prueba de satisfacción del objetivo: Permite determinar si el juego se termina cuando todas las letras tienen un dígito asociado, cumple con las condiciones  aritméticas (la operación correctamente verificada) y la condición adicional de que dos letras no pueden tener el mismo valor numérico (comprendido entre 0 y 9).
    Función de costo:sin importar el resultado el costo siempre es 0, dado que todas las soluciones son igual de válidas.
    '''
    
    def __init__(self, lista_palabras):
        self.palabras = lista_palabras
        self.lista_letras = [letra for palabra in self.palabras for letra in palabra ]
        self.lista_letras = list(set(self.lista_letras))
        self.estado_inicial = {letra:None for letra in self.lista_letras}
        self.letras_iniciales = list(set(palabra[0] for palabra in self.palabras))
        
    def pintar_estado(self, estado):
        # Dibuja el problema inicial, el estado del que se habla (ya sea la solución o no) y devuelve el resultado de la operación.
        # Input: Estado - diccionario con el estado de las letras del problema.
        fig, axes = plt.subplots(figsize=(5,len(self.palabras)))
        white = np.ones((100, 100), dtype=np.float)
        list_len = [len(palabra) for palabra in self.palabras]
        
        plt.text(0.2, 1.5, 'Problema inicial', fontsize = 20, color = 'blue')
        plt.text(1.5, 1.5, 'Estado', fontsize = 20, color = 'blue')
        plt.text(2.5, 1.5, 'Resultado', fontsize = 20, color = 'blue')
        plt.text(0, 1.3, '----------------------------------------------------------------------------------------------------------------------------', fontsize = 20, color = 'blue')
        
        for i in range(len(self.palabras)):
            if i == len(self.palabras) - 2:
                plt.text(0.2, (len(self.palabras)-i)/len(self.palabras), f"+      {self.palabras[i]}", fontsize = 20)
                plt.text(0.2, 3/2*1/len(self.palabras), '----------------', fontsize = 20)
            else:
                plt.text(0.4, (len(self.palabras)-i)/len(self.palabras), self.palabras[i], fontsize = 20)
                
        q = 0
        for est in estado:
            plt.text(1.4, (len(estado)-q)/len(estado), '|', fontsize = 20, color = 'blue')
            plt.text(1.5, (len(estado)-q)/len(estado), est, fontsize = 20)
            plt.text(1.6, (len(estado)-q)/len(estado), '|', fontsize = 20, color = 'blue')
            plt.text(1.8, (len(estado)-q)/len(estado), '|', fontsize = 20, color = 'blue')
            if estado[est] == None:
                plt.text(1.7, (len(estado)-q)/len(estado), '-', fontsize = 20)
            else:
                plt.text(1.7, (len(estado)-q)/len(estado), str(estado[est]), fontsize = 20)
            q += 1
            
        if self.test_objetivo(estado):
            for i in range(len(self.palabras_sol)):
                if i == len(self.palabras_sol) - 2:
                    plt.text(2.5, (len(self.palabras_sol)-i)/len(self.palabras_sol), f"+      {self.palabras_sol[i]}", fontsize = 20)
                    plt.text(2.5, 3/2*1/len(self.palabras_sol), '----------------', fontsize = 20)
                else:
                    plt.text(2.7, (len(self.palabras_sol)-i)/len(self.palabras_sol), str(self.palabras_sol[i]), fontsize = 20)
        else:
            plt.text(2.5, 1, "El estado no es", fontsize = 20)
            plt.text(2.3, 0.7, "una solución al problema.", fontsize = 20)
        
        axes.axis('off')
        
        return axes
    
    def pintar_camino(self, camino):
        # Dada una solución (camino) pinta el estado final de este.
        # Input: camino - Lista de duplas con los letras y los valores correspondientes a las letras del problema.
        dict_camino = dict(camino)
        self.pintar_estado(dict_camino)
        plt.show()
        
    def transicion(self, estado, accion):
        # Dada una acción se cambia el estado del problema.
        # Input: acción - Dupla con la letra y el valor que se desea cambiar en el diccionario.
        # Output: Estado que es un diccionario.
        estado_copy = deepcopy(estado)
        estado_copy[accion[0]] = accion[1]
        return estado_copy
    
    def acciones_aplicables(self, estado):
        # Devuelve una lista de tuplas que representan
        # la acción permitida, de acuerdo a la codificación
        # presentada en al formalización del problema más arriba.
        # Input: Estado - diccionario con el estado de las letras del problema.
        # Output: acciones - Lista de tuplas.
        digitos_disponibles = [d for d in range(10) if d not in estado.values()]
        letras_disponibles = [d for d in self.lista_letras if estado[d] == None]
        acciones = list(product(letras_disponibles, digitos_disponibles))
        for letra in self.letras_iniciales:
            if (letra, 0) in acciones:
                acciones.remove((letra, 0)) 
        return acciones
    
    def test_objetivo(self, estado):
        # Devuelve True/False dependiendo si el estado
        # resuelve el problema
        # Input: estado - diccionario de las letras con sus respectivos valores.
        # Output: True/False
        
        self.palabras_sol = []
        for palabra in self.palabras:
            for letra in palabra:
                palabra = palabra.replace(letra, str(estado[letra]))
            try:
                num_palabra = int(palabra)
                self.palabras_sol.append(num_palabra)
            except:
                return False
        return np.sum(self.palabras_sol[:-1]) == self.palabras_sol[-1] 
    
    def sol_algoritmo(self):
        # Resuelve el problema criptoaritmético tomando todas las posibles permutaciones
        # que tienen los digitos del 0 al 9 con las letras del problema.
        # Output: solucion si existe, else None.
        digitos = range(10)
        for permutacion in permutations(digitos, len(self.lista_letras)):
            solucion = dict(zip(self.lista_letras, permutacion))
            if any(solucion[letra]==0 for letra in self.letras_iniciales):
                continue
            if self.test_objetivo(solucion):
                return solucion
        return None
        
    def codigo(self, estado):
        str_codigo = ""
        for i in estado: 
            if estado[i] != None:
                str_codigo += f"{i}-{estado[i]} "
        return str_codigo
    
    def costo(self, estado, accion):
        return 0
        