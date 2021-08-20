class Nodo:
    
    # Clase para crear los nodos
    
    def __init__(self, estado, madre, accion, costo_camino, codigo):
        self.estado = estado
        self.madre = madre
        self.accion = accion
        self.costo_camino = costo_camino
        self.codigo = codigo
        
def nodo_hijo(problema, madre, accion):
    
    # Función para crear un nuevo nodo
    # Input: problema, que es un objeto de clase ocho_reinas
    #        madre, que es un nodo,
    #        accion, que es una acción que da lugar al estado del nuevo nodo
    # Output: nodo
    
    estado = problema.transicion(madre.estado, accion)
    costo_camino = madre.costo_camino + problema.costo(madre.estado, accion)
    codigo = problema.codigo(estado)
    return Nodo(estado, madre, accion, costo_camino, codigo)


def depth_first_search(problema):
    nodo = Nodo(problema.estado_inicial, None, None, 0, problema.codigo(problema.estado_inicial))
    if problema.test_objetivo(nodo.estado):
        return nodo
    frontera = [nodo]
    explorados = []
    while len(frontera) > 0:
        nodo = frontera.pop()
        explorados.append(nodo.codigo)
        for accion in problema.acciones_aplicables(nodo.estado):
            hijo = nodo_hijo(problema, nodo, accion)
            if problema.test_objetivo(hijo.estado):
                return hijo
            if hijo.codigo not in explorados:
                frontera.append(hijo)
    return None

def breadth_first_search(problema):
    nodo = Nodo(problema.estado_inicial, None, None, 0, problema.codigo(problema.estado_inicial))
    if problema.test_objetivo(nodo.estado):
        return nodo
    frontera = [nodo]
    explorados = []
    while len(frontera) > 0:
        nodo = frontera.pop(0)
        explorados.append(nodo.codigo)
        for accion in problema.acciones_aplicables(nodo.estado):
            hijo = nodo_hijo(problema, nodo, accion)
            if problema.test_objetivo(hijo.estado):
                return hijo
            if hijo.codigo not in explorados:
                frontera.append(hijo)
    return None


def solucion(n):
    if n.madre == None:
        return []
    else:
        return solucion(n.madre) + [n.accion]
    
def backtracking_search(prob, estado):
    if prob.test_objetivo(estado):
        return estado
    for accion in prob.acciones_aplicables(estado):
        hijo = prob.transicion(estado, accion)
        resultado = backtracking_search(prob, hijo)
        if resultado is not None:
            return resultado
    return None


def best_first_search(problema, f = None):
    if f is not None:
        setattr(problema, "costo", f)
    problema.costo = setattr(problema,"costo", f)
    s = problema.estado_inicial
    cod = problema.codigo(s)
    nodo = Nodo(s, None, None, 0, cod)
    frontera = ListaPrioritaria()
    frontera.push(nodo, 0)
    explorados = {}
    explorados[cod] = 0
    while not frontera.is_empty():
        nodo = frontera.pop()
        if problema.test_objetivo(nodo.estado):
            return nodo
        for hijo in expand(problema, nodo):
            s = hijo.estado
            cod = problema.codigo(s)
            c = hijo.costo_camino
            if cod not in explorados.keys() or c < explorados[cod]:
                frontera.push(hijo, c)
                explorados[cod] = c
    return None


