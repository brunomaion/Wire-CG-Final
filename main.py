import tkinter as tk
from tkinter import ttk

class Poligono:
    def __init__(self):
        self.vertices = []
        self.closed = False

    def get_vertices(self):
        return self.vertices

    def set_vertices(self, vertices):
        self.vertices = vertices

def clear_points():
    poligono.vertices = []
    poligono.closed = False
    update_canvases()

def on_left_click(event):
    if poligono.closed:
        poligono.vertices = []
        poligono.closed = False
    poligono.vertices.append((event.x, event.y))
    update_canvases()

def on_right_click(event):
    if poligono.vertices:
        poligono.closed = True
        update_canvases()

def update_canvases():
    canvas_input.delete("all")
    canvas_output.delete("all")
    #canvas_input.create_line(width/2, 0, width/2, height, fill="red", dash=(4, 4))
    canvas_input.create_line(0, height/2, width, height/2, fill="red", dash=(4, 4))
    
    
    
    
    if poligono.vertices:
        canvas_input.create_polygon(poligono.vertices, fill='', outline='blue', width=2)
        if poligono.closed:
            centralizar_poligono(poligono)
            canvas_output.create_polygon(poligono.vertices, fill='lightblue', outline='blue', width=2)
    update_vertex_list()

def update_vertex_list():
    vertex_list.set(", ".join([f"({x},{y})" for x, y in poligono.vertices]))

def update_mouse_coordinates(event):
    mouse_coords.set(f"X: {event.x}, Y: {event.y}")


def centralizar_poligono(poligono): #SOMAR X
    vertices = poligono.get_vertices() 
    x_min = min(v[0] for v in vertices)
    x_max = max(v[0] for v in vertices)
    
    x_centro = (x_min + x_max) / 2
    
    vertices = [list(vertex) for vertex in vertices]
    for i, e in enumerate(vertices):
        #print(type(vertices[i][0]))
        #print((vertices[i][0]+2))
        vertices[i][0] = vertices[i][0] + int(x_centro)
    
    vertices = [tuple(vertex) for vertex in vertices]
    poligono.set_vertices(vertices)

root = tk.Tk()
root.title("Polygon Drawer")

# Definir tamanhos fixos
width = 500
height = 500
button_width = 10

# Frame principal
main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH)

# Barra lateral com botões
sidebar_frame = ttk.Frame(main_frame, height=button_width)
sidebar_frame.pack(side=tk.BOTTOM, fill=tk.X)

clear_btn = ttk.Button(sidebar_frame, text="Limpar", command=clear_points)
clear_btn.pack(side=tk.LEFT, pady=10, padx=10)

vertex_list = tk.StringVar()
vertex_list_label = ttk.Label(sidebar_frame, textvariable=vertex_list)
vertex_list_label.pack(side=tk.LEFT, pady=10, padx=10)

mouse_coords = tk.StringVar()
mouse_coordinates_label = ttk.Label(sidebar_frame, textvariable=mouse_coords)
mouse_coordinates_label.pack(side=tk.RIGHT, pady=10, padx=10)

# Plano cartesiano 2D (entrada)
canvas_input = tk.Canvas(main_frame, width=width/2, height=height, bg='white')
canvas_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)
canvas_input.bind("<Button-1>", on_left_click)
canvas_input.bind("<Button-3>", on_right_click)
canvas_input.bind("<Motion>", update_mouse_coordinates)

# Saída do polígono (visualização colorida)
canvas_output = tk.Canvas(main_frame, width=width, height=height, bg='white')
canvas_output.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False)


# Inicializar o objeto polígono
poligono = Poligono()

# Chamando update_canvases() para garantir que a lista de vértices seja exibida corretamente inicialmente
update_canvases()

root.mainloop()
