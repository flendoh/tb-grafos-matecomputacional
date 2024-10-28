import dearpygui.dearpygui as dpg
import networkx as nx
import matplotlib.pyplot as plt
from screens.solution_table import SolutionTable
import os
import uuid

class PreviewGraph:
    def __init__(self):
        self.solution_table = SolutionTable()
        self.matrix = None
        self.graph = nx.DiGraph()
        self.parent = None
        self.image = None
        self.text_info = None
        self.shortest_path = None
        self.solution_table_button = None
        self.start_node = None
        self.end_node = None

    def create(self):
        with dpg.group(horizontal=False):
            with dpg.child_window(height=495) as self.parent:
                dpg.add_text("Grafo asociado a la matriz de adyacencia")
                dpg.add_separator()
            with dpg.child_window():
                self.text_info = dpg.add_text(f"Elementos del grafo:\n{str(self.graph.edges)}\n", wrap=900)
                dpg.add_spacer(height=10)
                dpg.add_separator()
                self.solution_table_button = dpg.add_button(label="Demostración de Dijkstra", callback=self.show_solution_table, enabled=False)
    
    def add_nodes_and_edges(self):
        self.graph.clear()
        size = len(self.matrix)
        for i in range(size):
            for j in range(size):
                if self.matrix[i][j] != 0:
                    self.graph.add_edge(i, j, weight=self.matrix[i][j])
    
    def file_path(self):
        assets_dir = os.path.join(os.path.dirname(__file__),'..', 'assets')
        if not os.path.exists(assets_dir):
            os.makedirs(assets_dir)
        image_path = os.path.join(assets_dir, 'frame.png')

        return image_path 

    def load_img(self, image_path):
        width, height, channels, first_image = dpg.load_image(image_path)

        texture_tag = str(uuid.uuid4())

        with dpg.texture_registry():
            dpg.add_static_texture(width, height, first_image, tag=texture_tag)
        
        return texture_tag
    
    def show_solution_table(self):
        SolutionTable().create(self.graph, self.start_node, self.end_node)
    
    def save_img(self, start_node=0, end_node=0, node_size=500, graph_seed=100):
        import matplotlib
        matplotlib.use('Agg')
    
        pos = nx.spring_layout(self.graph, seed=graph_seed)
        plt.figure(figsize=(9, 4.5))

        nx.draw(self.graph, pos, with_labels=True, 
                node_color='#98c6ea',
                node_size=node_size, 
                edge_color='black',  
                width=1.5,                  
                edgecolors='#1270c0',
                linewidths=2)
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        self.start_node = start_node
        self.end_node = end_node
        
        if start_node!=end_node and 0<=start_node<len(self.matrix) and 0<=end_node<len(self.matrix):
            self.shortest_path = nx.shortest_path(self.graph, source=start_node, target=end_node, weight='weight')
            #Resaltar el camino más corto en otro color
            path_edges = list(zip(self.shortest_path, self.shortest_path[1:]))
            nx.draw_networkx_edges(self.graph, pos, edgelist=path_edges, edge_color='red', width=2)
            nx.draw_networkx_nodes(self.graph, pos, nodelist=self.shortest_path, node_color='#f2ad77', node_size=node_size, linewidths=2, edgecolors='#ed652a')

            # Obtener nodo padre y distancia recurrente con Dijkstra
            self.dijkstra_result = nx.dijkstra_predecessor_and_distance(self.graph, source=start_node)
            predecessors, distances = self.dijkstra_result
            
            distance_labels = {node: f"[{distances[node]}, {predecessors[node][0] if predecessors[node] else '-'}]" 
                            for node in self.graph.nodes if node in distances}
            
            pos_labels = {node: (x, y + 0.1) for node, (x, y) in pos.items()}
            
            nx.draw_networkx_labels(self.graph, pos_labels, labels=distance_labels, font_color='black', font_size=10)
        
            
        else:
            self.shortest_path = None

        image_path = self.file_path()
        plt.savefig(image_path)
        plt.close()

        return image_path
    
    def update(self, matrix, start_node=0, end_node=0, node_size=500, graph_seed=100):
        self.matrix = matrix
        self.add_nodes_and_edges()
        path = self.save_img(start_node, end_node, node_size, graph_seed)
        tag = self.load_img(path)

        if self.shortest_path:
            dpg.set_value(self.text_info, f"Elementos del grafo:\n{str(self.graph.edges)}\nCamino más corto de {start_node} a {end_node}:\n {self.shortest_path}")
            dpg.enable_item(self.solution_table_button)
        else:
            dpg.set_value(self.text_info, f"Elementos del grafo:\n{str(self.graph.edges)}")
            dpg.disable_item(self.solution_table_button)

        if self.image !=None:
            dpg.configure_item(self.image, texture_tag=tag)
        else:
            self.image = dpg.add_image(tag, parent=self.parent)
        