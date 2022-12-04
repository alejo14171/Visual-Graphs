from graphics import *
import numpy as np
import tkinter

# Initial arrays where data is going to be stored
matriz_adyacencias = np.zeros([0, 0])
lista_nodos = []
lista_arcos = []
arcos_aux = []
cantidad_nodos = -1
cantidad_arcos = 0
radius = 15

win = GraphWin('Visual Graphs', 800, 600)
button_nodes = Rectangle(Point(695, 5), Point(795, 55))
button_edges = Rectangle(Point(695, 60), Point(795, 110))
button_path = Rectangle(Point(695, 115), Point(795, 165))
button_erase_nodes = Rectangle(Point(695, 170), Point(795, 220))
button_eulerian= Rectangle(Point(695, 225), Point(795, 275))
button_conexo = Rectangle(Point(695, 280), Point(795, 330))
button_bipartito = Rectangle(Point(695, 335), Point(795, 385))
button_colorear = Rectangle(Point(695, 390), Point(795, 440))

text_nodes = Text(Point(745, 30), 'Nodes')
text_nodes.draw(win)
text_edges = Text(Point(745, 85), 'Arists')
text_path = Text(Point(745, 140), 'Path')
text_erase = Text(Point(745, 195), 'Erase Nodes')
text_eulerian = Text(Point(745, 250), 'Eulerian Path')
text_conexo = Text(Point(745, 305), 'Connected')
text_bipartito = Text(Point(745, 360), 'Bipartite')
text_colorear = Text(Point(745, 415), 'Coloring')

button_eulerian.draw(win)
button_erase_nodes.draw(win)
text_eulerian.draw(win)
text_erase.draw(win)
text_path.draw(win)
text_edges.draw(win)
button_nodes.draw(win)
button_edges.draw(win)
button_path.draw(win)
button_conexo.draw(win)
text_conexo.draw(win)
button_bipartito.draw(win)
text_bipartito.draw(win)
button_colorear.draw(win)
text_colorear.draw(win)

area = Rectangle(Point(5,5), Point(690,595))
area.setFill('gray')
area.draw(win)

# Crear una manera de dibujar eso más bonito
#    - Pintar nodos seleccionados de color verde
#    - Ponerle a cada nodo su respectivo label (por ahora su número)
#    - Mejores botones, al presionarlo que se vea verde en serio
#    - Un texto que diga si está en modo creador de nodos o modo creador de arcos
# Mejorar eso del sleep
# Matriz adyacencias
# Función para recorrer desde un nodo a otro
# Función para recorrer todo el grafo a partir de un nodo


class Nodo():
    global matriz_adyacencias, lista_nodos

    def __init__(self, point, label, figura, color = 'black'):
        self.position = point
        self.label = label
        self.figure = [figura[0], figura[1]]
        self.color = color
    
    # def actualizar_matriz_adyacencias(self):


class Arco():
    def __init__(self, points, label, figure):
        self.position = [points[0], points[1]]
        self.label = [label[0], label[1]]
        self.figure = [figure[0], figure[1]]


def verify_eulerian():
    global matriz_adyacencias
    for f in matriz_adyacencias:
        print(np.sum(f))
        if np.sum(f)%2 != 0:
            return True

def verify_conexo():
    global matriz_adyacencias
    copy_ma = matriz_adyacencias.copy()

    for i in range(copy_ma.shape[0]):
        copy_ma[i, i] = 0

    for fila in copy_ma:
        if np.sum(fila) == 0:
            return False
    return True




def verificar_nodo_seleccionado(point, primer=0):
    if primer == 1: t = 'Select a SECOND node'
    if primer == 2: t = 'Arist created, for creating another arist select another node'
    if primer == 3: t = 'Node erased!'


    for nodo in lista_nodos:
        position = nodo.position
        label = nodo.label
        d = ( (position.x - point.x)**2 + (position.y - point.y)**2 )**0.5
        if d <= radius:
            text_aux = Text(Point(350, 550), t)
            return True, text_aux, label
    
    text_aux = Text(Point(350, 30), 'There is no selected node!, select one node')
    return False, text_aux, label

def retornar_nodo_seleccionado(point):
    t = 'Node erased!'

    for nodo in lista_nodos:
        position = nodo.position
        label = nodo.label
        d = ( (position.x - point.x)**2 + (position.y - point.y)**2 )**0.5
        if d <= radius:
            text_aux = Text(Point(350, 550), t)
            return True, text_aux, nodo

    text_aux = Text(Point(350, 30), 'There is no selected node!, select one node')
    return False, text_aux, nodo

def get_arcos(nodo):
    global lista_arcos
    arcos_vecinos = []
    indexes_arcos_a_eliminar = []
    for i in range(len(lista_arcos)):
        print(lista_arcos[i].label[0][1], nodo.label.split('n')[1], lista_arcos[i].label[1][1], nodo.label.split('n')[1])
        if lista_arcos[i].label[0][1] == nodo.label.split('n')[1] or lista_arcos[i].label[1][1] == nodo.label.split('n')[1]:
            arcos_vecinos.append(lista_arcos[i])
            indexes_arcos_a_eliminar.append(i)

    # for i in range(len(indexes_arcos_a_eliminar)):
    #     lista_arcos.pop(i)
    
    return arcos_vecinos


def nodes_creator(flag):
    '''Crea nodos hasta que da nuevamente en el botón de crear nodos'''
    global cantidad_nodos, lista_nodos, matriz_adyacencias

    while True:
        if flag == 'Enter':
            button_nodes.setWidth(3)
            button_nodes.setOutline('green')
            flag = 'Operating'

        elif flag == 'Operating':
            point = win.getMouse()
            if 690<point.x<790 and 0<point.y<55:
                button_nodes.setWidth(1)
                button_nodes.setOutline('black')
                break

            if not (point.x>690):
                c = Circle(point, radius)
                c.setFill('black')
                c.draw(win)
                texto_nodo = Text(Point(point.x, point.y), 'n'+str(cantidad_nodos+1))
                nodo = Nodo(point, 'n'+str(cantidad_nodos+1), [c, texto_nodo])
                nodo.figure[1].setFill('white')
                nodo.figure[1].draw(win)
                cantidad_nodos += 1
                lista_nodos.append(nodo)

                if matriz_adyacencias.size == 0: matriz_adyacencias = np.zeros([1, 1])
                else:
                    A = [[0] for x in range(cantidad_nodos)] #columna añadida require un +1
                    A = np.transpose(A)
                    # print('\n A:', A, '\n')
                    B = [[0] for x in range(cantidad_nodos+1)]
                    # B = np.array(A)
                    # print('\n B:', B, '\n')
                    matriz_adyacencias = np.concatenate([matriz_adyacencias, A], axis=0)
                    matriz_adyacencias = np.concatenate([matriz_adyacencias, B], axis=1)
                    print(matriz_adyacencias)

# pygame
# networkx
def edges_creator(flag):
    '''Crea nodos hasta que da nuevamente en el botón de crear nodos'''
    while True:

        global cantidad_arcos, lista_arcos, matriz_adyacencias

        if flag == 'Enter':
            button_edges.setWidth(3)
            button_edges.setOutline('green')
            flag = 'Operating'

        elif flag == 'Operating':

            text_aux = Text(Point(350, 30), 'Select a node')
            text_aux.draw(win)
            flag_primer_nodo = False
            flag_segundo_nodo = False

            # If click on edges button
            point = win.getMouse()
            if 690<point.x<790 and 60<point.y<110:
                button_edges.setWidth(1)
                button_edges.setOutline('black')
                text_aux.undraw()
                break

            while flag_primer_nodo == False:
                point_first_node = point
                flag_primer_nodo, text_aux_1, label_nodo1 = verificar_nodo_seleccionado(point_first_node, 1)
                label_nodo1 = label_nodo1.split('n')
                if flag_primer_nodo == False: 
                    text_aux.undraw()
                    text_aux_1.draw(win)
                    point = win.getMouse()
                    text_aux_1.undraw()
                else:
                    text_aux.undraw()
                    text_aux_1.draw(win)

            text_aux_2 = Text(Point(350, 550), '')
            # While click outside the second node
            while flag_segundo_nodo == False:
                point_second_node = win.getMouse()
                text_aux_1.undraw()
                text_aux_2.undraw()
                flag_segundo_nodo, text_aux_2, label_nodo2 = verificar_nodo_seleccionado(point_second_node, 2)
                label_nodo2 = label_nodo2.split('n')
                if flag_segundo_nodo == False:
                    text_aux_2.draw(win)
                else:
                    text_aux_2.draw(win)

                    
            
            l = Line(point_first_node, point_second_node)
            l.draw(win)
            x1 = point_first_node.x
            x2 = point_second_node.x
            y1 = point_first_node.y
            y2 = point_second_node.y

            point_text = Point(abs(x2+x1)/2, abs(y2+y1)/2)
            
            arcos_aux.append((int(label_nodo1[1]), int(label_nodo2[1])))
            # print(arcos_aux)
            texto_arco = Text(point_text, label_nodo1[1] + '-' + label_nodo2[1])
            texto_arco.draw(win)

            arco = Arco([point_first_node, point_second_node], [label_nodo1, label_nodo2], [l, texto_arco])
            print(int(label_nodo1[1]), int(label_nodo2[1]))

            matriz_adyacencias[int(label_nodo1[1]), int(label_nodo2[1])] = 1
            matriz_adyacencias[int(label_nodo2[1]), int(label_nodo1[1])] = 1

            print(matriz_adyacencias)
            lista_arcos.append(arco)

            time.sleep(0.5)
            text_aux_2.undraw()

def draw_path(i, f):
    circle = Circle(lista_nodos[i].position, radius)
    circle.setFill('green')
    circle.draw(win)
    time.sleep(0.5)
    circle.undraw()
    circle = Circle(lista_nodos[f].position, radius)
    circle.setFill('green')
    circle.draw(win)
    time.sleep(0.5)
    circle.undraw()


def make_path(initial_node, final_node):
    global matriz_adyacencias
    ma_copy = matriz_adyacencias.copy()

    flag = True
    visited_nodes = [initial_node]

    while flag == True:
        if initial_node == final_node:
            return 1
        if ma_copy[initial_node, final_node] == 1:
            draw_path(initial_node, final_node)
            return 1

        else:
            aux = False
            for i in range(len(ma_copy[initial_node])):
                if ma_copy[initial_node, i] == 1 and aux == False:
                    draw_path(initial_node, i)
                    ma_copy[initial_node, i] = 0
                    initial_node = i
                    aux == True

def make_path_eulerian(initial_node):
    global matriz_adyacencias
    ma_copy = matriz_adyacencias.copy()

    flag = True
    visited_nodes = []
    aux_fila = ma_copy[initial_node]
    i = 0
    for el in aux_fila:
        if el == 1:
            actual_node = i
        i+=1

    while flag == True:
        if initial_node == actual_node:
            return 1
        if ma_copy[initial_node, initial_node] == 1:
            draw_path(initial_node, actual_node)
            return 1

        else:
            aux = False
            for i in range(len(ma_copy[initial_node])):
                if ma_copy[initial_node, i] == 1 and aux == False:
                    draw_path(initial_node, i)
                    ma_copy[initial_node, i] = 0
                    ma_copy[i, initial_node] = 0
                    initial_node = i
                    aux == True


def draw_eulerian(i, f):
    circle = Circle(lista_nodos[i].position, 10)
    circle.setFill('green')
    circle.draw(win)
    time.sleep(0.5)
    circle.undraw()
    circle = Circle(lista_nodos[f].position, 10)
    circle.setFill('green')
    circle.draw(win)
    time.sleep(0.5)
    circle.undraw()


def eulerian_path(initial_node, final_node):
    global matriz_adyacencias
    ma_copy = matriz_adyacencias.copy()

    flag = True
    visited_nodes = [initial_node]

    while flag == True:
        if initial_node == final_node:
            return 1
        if ma_copy[initial_node, final_node] == 1:
            draw_eulerian(initial_node, final_node)
            return 1

        else:
            aux = False
            for i in range(len(ma_copy[initial_node])):
                if ma_copy[initial_node, i] == 1 and aux == False:
                    draw_path(initial_node, i)
                    ma_copy[initial_node, i] = 0
                    initial_node = i
                    aux == True
                
                    



def path_creator(flag):
    '''Crea nodos hasta que da nuevamente en el botón de crear nodos'''
    while True:

        global cantidad_arcos, lista_arcos

        if flag == 'Enter':
            button_path.setWidth(3)
            button_path.setOutline('green')
            flag = 'Operating'

        elif flag == 'Operating':
            text_aux = Text(Point(350, 30), 'Select a node')
            text_aux.draw(win)
            flag_primer_nodo = False
            flag_segundo_nodo = False

            # If click on path button
            point = win.getMouse()
            if 690<point.x<790 and 115<point.y<165:
                button_edges.setOutline('black')
                text_aux.undraw()
                break

            while flag_primer_nodo == False:
                point_first_node = point
                flag_primer_nodo, text_aux_1, label_nodo1 = verificar_nodo_seleccionado(point_first_node, 1)
                if flag_primer_nodo == False: 
                    text_aux.undraw()
                    text_aux_1.draw(win)
                    point = win.getMouse()
                    text_aux_1.undraw()
                else:
                    text_aux.undraw()
                    text_aux_1.draw(win)

            text_aux_2 = Text(Point(350, 550), '')
            # While click outside the second node
            while flag_segundo_nodo == False:
                point_second_node = win.getMouse()
                text_aux_1.undraw()
                text_aux_2.undraw()
                flag_segundo_nodo, text_aux_2, label_nodo2 = verificar_nodo_seleccionado(point_second_node, 2)
                
                if text_aux_2 == 'Node created! For creating another one select a node.':
                    text_aux_2.draw(win)
            
            make_path(int(label_nodo1[1]), int(label_nodo2[1]))
            text_aux_2 = Text(Point(350, 30), 'Here is your path!')
            text_aux_2.draw(win)
            time.sleep(2)
            text_aux_2.undraw()
            button_path.setWidth(1)
            button_path.setOutline('black')
            break



def path_creator_eulerian(flag):
    '''Crea nodos hasta que da nuevamente en el botón de crear nodos'''
    while True:

        global cantidad_arcos, lista_arcos

        if flag == 'Enter':
            button_eulerian.setWidth(3)
            button_eulerian.setOutline('green')
            flag = 'Operating'

        elif flag == 'Operating':
            text_aux = Text(Point(350, 30), 'Select a node')
            text_aux.draw(win)
            flag_primer_nodo = False
            flag_segundo_nodo = False

            # If click on path button
            make_path_eulerian(0)
            text_aux_2 = Text(Point(350, 30), 'Here is your path!')
            text_aux_2.draw(win)
            time.sleep(2)
            text_aux_2.undraw()
            button_eulerian.setWidth(1)
            button_eulerian.setOutline('black')
            break
            
            
def erase_nodes(flag):
    global matriz_adyacencias, cantidad_nodos
    while True:

        global cantidad_arcos, lista_arcos, matriz_adyacencias

        if flag == 'Enter':
            button_erase_nodes.setWidth(3)
            button_erase_nodes.setOutline('green')
            flag = 'Operating'

        elif flag == 'Operating':
            text_aux = Text(Point(350, 30), 'Select a node')
            text_aux.draw(win)
            flag_primer_nodo = False

            
            while flag_primer_nodo == False:
            # If click on erase button
                point = win.getMouse()
                if 695<point.x<795 and 60<point.y<220:
                    button_erase_nodes.setWidth(1)
                    button_erase_nodes.setOutline('black')
                    text_aux.undraw()
                    return 1

                point_first_node = point
                flag_primer_nodo, text_aux_1, nodo = retornar_nodo_seleccionado(point_first_node)
                if flag_primer_nodo == False: 
                    text_aux.undraw()
                    text_aux_1.draw(win)
                    point = win.getMouse()
                    text_aux_1.undraw()
                else:
                    text_aux.undraw()
                    text_aux_1.draw(win)
                    nodo.figure[0].undraw()
                    nodo.figure[1].undraw()
                    # Dentro de get_arcos borra los arcos de la lista de arcos
                    arcos_nodo = get_arcos(nodo)
                    for arco in arcos_nodo:
                        arco.figure[0].undraw()
                        arco.figure[1].undraw()
                    time.sleep(2)
                    text_aux_1.undraw()
            text_aux.undraw()

            # Cuadrar la matriz de adyacencias
            matriz_adyacencias = np.delete(matriz_adyacencias, int(nodo.label[1]), axis=0)
            matriz_adyacencias = np.delete(matriz_adyacencias, int(nodo.label[1]), axis=1)

            lista_nodos.remove(nodo)
            cantidad_nodos-=1
            i = 0
            for nodo in lista_nodos:
                nodo.label = 'n'+ str(i)
                nodo.figure[1].setText(nodo.label)
                i+=1


            print('MA modificada\n', matriz_adyacencias)
            
    return 1

def estan_conectados(nodo1: Nodo, nodo2: Nodo):
    global matriz_adyacencias

    n1 = nodo1.label[1]
    n2 = nodo2.label[1]

    if matriz_adyacencias[int(n1), int(n2)] == 1:
        return True
    else: 
        return False



def verify_bipartito():
    global matriz_adyacencias, lista_nodos
    conjuntoA = []
    conjuntoB = []
    it = 0
    flag_ini_B = True
    for nodo in lista_nodos:
        flagA = True
        if it == 0: conjuntoA.append(nodo)

        else:
            for nodo_a in conjuntoA:
                if estan_conectados(nodo, nodo_a) and flagA:
                    if it > 0 and flag_ini_B: 
                        conjuntoB.append(nodo)
                        flag_ini_B = False
                    
                    flagA = False
                    for nodo_b in conjuntoB:
                        if estan_conectados(nodo, nodo_b):
                            return False

                    conjuntoB.append(nodo)

            if flagA == True:
                conjuntoA.append(nodo)

        it += 1
    return True

def verify_colorear():
    lista_colores = ['green', 'yellow', 'red', 'pink', 'orange', 'brown', 'purple']
    cant_colores = len(lista_colores)
    suma = 0
    
    for fila in matriz_adyacencias:
        aux = np.sum(fila)
        suma += aux

    if suma>(cant_colores-1)*cant_colores:
        return False

    colorear_grafo(lista_colores)
    return True


def colorear_grafo(colores):
    # ir nodo por nodo mirando si ya están pintados, si no están pintados, los pintamos con el mínimo color posible. Ese mínimo color posible se va a escoger según los vecinos del nodo

    for nodo in lista_nodos:
        vecinos = vecinos_nodo(nodo)

        colores_vecinos = []
        print('colores de los vecinos del', nodo.label)
        for vecino in vecinos:
            color_vecino = vecino.color
            colores_vecinos.append(color_vecino)
            print(vecino.label, color_vecino)
            
        # nodo.color está en la lista de los colores de los vecinos
        
        ind_color = 0
        colores_disponibles = colores.copy()
        # print( 'colores vecinos')
        for color in colores_vecinos:
            if color in colores_disponibles:
                colores_disponibles.remove(color)

        nodo.color = colores_disponibles[0]
        nodo.figure[0].setFill(nodo.color)
        time.sleep(0.1)
    



def vecinos_nodo(nodo: Nodo):
    vecinos_del_nodo = []
    label_nodo = nodo.label
    pos_nodo = int(label_nodo.split('n')[1])
    i = 0
    for el in matriz_adyacencias[pos_nodo]:
        if el == 1:
            vecinos_del_nodo.append(lista_nodos[i])
        i+=1

    
    return vecinos_del_nodo


            

    




while True:
    point = win.getMouse() # Pause to view result
    if 690<point.x<790 and 0<point.y<50:
        nodes_creator('Enter')

    if 690<point.x<790 and 55<point.y<105:
        if  len(lista_nodos) != 0:
            edges_creator('Enter')
        else:
            text_adv = Text(Point(400, 150), 'First, create nodes!')
            text_adv.draw(win)
            time.sleep(0.5)
            text_adv.undraw()

    if 690<point.x<790 and 115<point.y<165:
        if  len(lista_nodos) != 0 and len(lista_arcos) != 0:
            path_creator('Enter')
        else:
            text_adv = Text(Point(400, 20), 'First, create a graph!')
            text_adv.draw(win)
            time.sleep(2)
            text_adv.undraw()
    # Erase
    if 690<point.x<790 and 170<point.y<220:
        if  len(lista_nodos) != 0:
            erase_nodes('Enter')
        else:
            text_adv = Text(Point(400, 150), 'First, create a graph!')
            text_adv.draw(win)
            time.sleep(1)
            text_adv.undraw()
        

    if 690<point.x<790 and 225<point.y<275:
        start_eulerian=False
        if  verify_eulerian():
            text_adv = Text(Point(400, 40), 'There is NO eulerian path for this graph')
            text_adv.setOutline('red')
            text_adv.draw(win)
            time.sleep(2)
            text_adv.undraw()
            
        else:
            text_adv = Text(Point(400, 40), 'There exist an eulerian path for this graph')
            text_adv.setOutline('black')
            text_adv.draw(win)
            time.sleep(1)
            text_adv.undraw()
            path_creator_eulerian('Enter')
# Conexo
    if 690<point.x<790 and 280<point.y<330:
        button_conexo.setWidth(3)
        button_conexo.setOutline('green')
        if  verify_conexo():
            text_adv = Text(Point(400, 40), 'Graph is connected')
            text_adv.setOutline('black')
            text_adv.draw(win)
            time.sleep(2)
            text_adv.undraw()
            button_conexo.setWidth(1)
            button_conexo.setOutline('black')
            
        else:
            text_adv = Text(Point(400, 40), 'Disconnected graph!')
            text_adv.setOutline('black')
            text_adv.draw(win)
            time.sleep(2)
            text_adv.undraw()
            button_conexo.setWidth(1)
            button_conexo.setOutline('black')

    if 690<point.x<795 and 335<point.y<385:
            button_bipartito.setWidth(3)
            button_bipartito.setOutline('green')
            if  verify_bipartito():
                text_adv = Text(Point(400, 40), 'Graph IS bipartite')
                text_adv.setOutline('black')
                text_adv.draw(win)
                time.sleep(2)
                text_adv.undraw()
                button_bipartito.setWidth(1)
                button_bipartito.setOutline('black')
                
            else:
                text_adv = Text(Point(400, 40), 'Graph is NOT bipartite!')
                text_adv.setOutline('black')
                text_adv.draw(win)
                time.sleep(2)
                text_adv.undraw()
                button_bipartito.setWidth(1)
                button_bipartito.setOutline('black')            
                
            

    if 690<point.x<795 and 390<point.y<440:
            button_colorear.setWidth(3)
            button_colorear.setOutline('green')
            if  verify_colorear():
                text_adv = Text(Point(400, 40), 'Here is your colored graph')
                text_adv.setOutline('black')
                text_adv.draw(win)
                time.sleep(2)
                text_adv.undraw()
                button_colorear.setWidth(1)
                button_colorear.setOutline('black')
                win.getMouse()
                for nodo in lista_nodos:
                    nodo.figure[0].setFill('black')
                
            else:
                text_adv = Text(Point(400, 40), 'There are no many colors for that graph!')
                text_adv.setOutline('black')
                text_adv.draw(win)
                time.sleep(2)
                text_adv.undraw()
                button_colorear.setWidth(1)
                button_colorear.setOutline('black')     
                
            

