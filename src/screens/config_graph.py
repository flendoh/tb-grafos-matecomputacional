import dearpygui.dearpygui as dpg
from .preview_graph import PreviewGraph
import random
class ConfigGraph:
    def __init__(self):
        self.size_array = None
        self.matrix_group = None
        self.preview_window = PreviewGraph()
        self.start_node = None
        self.end_node = None

    def create_matrix(self, sender=None, app_data=None, user_data=None):
        size = dpg.get_value(self.size_array)
        self.input_ids = []

        if self.matrix_group is not None:
            children = dpg.get_item_children(self.matrix_group, 1)
            for child in children:
                dpg.delete_item(child)
        else:
            self.matrix_group = dpg.add_group(horizontal=False, parent=user_data)
        
        for i in range(size):
            with dpg.group(horizontal=True, parent=self.matrix_group):
                for j in range(size):
                    input_id = dpg.add_input_int(label=f"({i},{j})", width=70,callback=self.update_preview)
                    self.input_ids.append(input_id)

    def update_preview(self):
        self.preview_window.update(self.get_matrix(), dpg.get_value(self.start_node), dpg.get_value(self.end_node))

    def clear_matrix(self):
        for input_id in self.input_ids:
            dpg.set_value(input_id, 0)

    def fill_matrix(self):
        self.clear_matrix()
        size = dpg.get_value(self.size_array)
        t = ((size**2)-size)/2
        current_fill = 0
        while(current_fill<t):
            input_id = random.choice(self.input_ids) #seleccionamos aleatoriamente un elemento de los inputs
            label = dpg.get_item_label(input_id).replace("(", "").replace(")", "")
            node = label.split(',')

            inverse_label = f"({node[1]},{node[0]})"

            inverse_id = next((current for current in self.input_ids if dpg.get_item_label(current) == inverse_label), None)

            #verificamos que no sea reflexia y sea antisimetrica
            if node[0]!=node[1] and dpg.get_value(input_id) == 0 and dpg.get_value(inverse_id) == 0:
                random_value = random.randint(0, 10)
                dpg.set_value(input_id, random_value)
                current_fill+=1


        self.update_preview()
    
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
        with dpg.window(label="Configuración", width=500, height=200) as main_window:
            dpg.add_text("Config Matriz")
            self.size_array = dpg.add_input_int(label="Tamaño", width=100, default_value=8, callback=self.create_matrix)
            dpg.add_text("Matriz")
            dpg.add_button(label="Rellenar Matriz Aleatoriamente", callback=self.fill_matrix)

        self.create_matrix(user_data=main_window)
        self.preview_window.create(matrix=self.get_matrix())

        dpg.add_text("Encontrar el camino mínimo entre dos nodos (Dijkstra)", parent=main_window)
        
        self.start_node = dpg.add_input_int(label="Nodo Inicio", width=100, parent=main_window, callback=self.update_preview)
        self.end_node = dpg.add_input_int(label="Nodo Final", width=100, parent=main_window, callback=self.update_preview)