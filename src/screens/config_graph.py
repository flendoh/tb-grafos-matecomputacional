import dearpygui.dearpygui as dpg
from .preview_graph import PreviewGraph
import random
import time
class ConfigGraph:
    def __init__(self):
        self.size_array = None
        self.matrix_group = None
        self.preview_window = PreviewGraph()
        self.start_node = None
        self.end_node = None
        self.node_size = None
        self.graph_seed = None

    def create_matrix(self, sender=None, app_data=None, user_data=None):
        size = dpg.get_value(self.size_array)
        self.input_ids = []

        if self.matrix_group is not None:
            children = dpg.get_item_children(self.matrix_group, 1)
            for child in children:
                dpg.delete_item(child)
        else:
            self.matrix_group = dpg.add_group(horizontal=False, parent=user_data)
        
        with dpg.table(header_row=False, parent=self.matrix_group, resizable=False):
            for i in range(size):
                dpg.add_table_column()  # agrega columnas para la tabla
        
            for i in range(size):
                with dpg.table_row():  # crea una fila en la tabla
                    for j in range(size):
                        input_id = dpg.add_input_int(label=f"({i},{j})", width=30,callback=self.update_preview, step=0)
                        self.input_ids.append(input_id)

    def update_preview(self):
        self.preview_window.update(self.get_matrix(), dpg.get_value(self.start_node), dpg.get_value(self.end_node), dpg.get_value(self.node_size), dpg.get_value(self.graph_seed))

    def clear_matrix(self):
        for input_id in self.input_ids:
            dpg.set_value(input_id, 0)

    def fill_matrix(self):
        self.clear_matrix()
        size = dpg.get_value(self.size_array)
        max_range = ((size**2)-size)/2
        current_fill = 0
        t = random.randint(1, int(max_range))
        while(current_fill<t):
            input_id = random.choice(self.input_ids) #seleccionamos aleatoriamente un elemento de los inputs
            label = dpg.get_item_label(input_id).replace("(", "").replace(")", "")
            node = label.split(',')

            inverse_label = f"({node[1]},{node[0]})"

            reverse_input_id = next((current for current in self.input_ids if dpg.get_item_label(current) == inverse_label), None)

            #verificamos que no sea reflexia y sea simetrica
            if node[0]!=node[1] and dpg.get_value(input_id) == 0 and dpg.get_value(reverse_input_id) == 0:
                random_value = random.randint(1, 10)
                dpg.set_value(input_id, random_value)
                dpg.set_value(reverse_input_id, random_value)
                current_fill+=1

                #self.update_preview()
                #time.sleep(0.01)  # 0.01 segundos de delay

        self.update_preview()
    
    def gen_random_matrix(self):
        min_range = 8
        max_range = 16

        random_size = random.randint(min_range, max_range)
        dpg.set_value(self.size_array, random_size)
        self.create_matrix()
        self.fill_matrix()
    
    def get_matrix(self):
        size = dpg.get_value(self.size_array)
        matrix = []
        for i in range(size):
            row = []
            for j in range(size):
                index = i * size + j
                value = dpg.get_value(self.input_ids[index])
                row.append(value)
            matrix.append(row)
        return matrix

    def create(self):
        with dpg.window(label="Configuración", width=500, height=500) as main_window:
            #CONFIGURACION MATRIZ
            dpg.add_button(label="Generar una matriz simetrica aleatoria de tamaño n [8<=n<=16]", callback=self.gen_random_matrix)
            dpg.add_text("Matriz")
            self.size_array = dpg.add_input_int(label="Tamaño", width=100, default_value=8, callback=self.create_matrix)
            dpg.add_text("Elementos")

            #MATRIZ
            self.create_matrix(user_data=main_window)
            self.preview_window.create(matrix=self.get_matrix())

            #CAMINO CORTO
            dpg.add_text("Encontrar el camino mínimo entre dos nodos (Dijkstra)")
            self.start_node = dpg.add_input_int(label="Nodo Inicio", width=100, callback=self.update_preview)
            #dpg.add_same_line()
            self.end_node = dpg.add_input_int(label="Nodo Final", width=100, callback=self.update_preview, )

            #CONFIGRUACION DISEÑO DEL GRAFO
            dpg.add_text("Diseño del Grafo")

            self.node_size = dpg.add_input_int(label="Tamaño del Nodo", default_value=500, width=100, callback=self.update_preview, step=150)
            self.graph_seed = dpg.add_input_int(label="Seed", default_value=random.randint(1, 999), width=100, callback=self.update_preview)
