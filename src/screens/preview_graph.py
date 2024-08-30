import dearpygui.dearpygui as dpg
import networkx as nx
import matplotlib.pyplot as plt
import os
import uuid

class PreviewGraph:
    def __init__(self):
        self.matrix = None
        self.graph = nx.Graph()
        self.seed = 100
        self.parent = None
        self.image = None
        self.text_info = None
        self.shortest_path = None

    def create(self, matrix):
        self.matrix = matrix
        self.display_graph()
    
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
    
    def save_img(self, start_node=0, end_node=0):
        import matplotlib
        matplotlib.use('Agg')

        pos = nx.spring_layout(self.graph, seed=self.seed)
        plt.figure(figsize=(8, 5))

        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray')
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)

        
        if start_node!=end_node and 0<=start_node<len(self.matrix) and 0<=end_node<len(self.matrix):
            self.shortest_path = nx.shortest_path(self.graph, source=start_node, target=end_node, weight='weight')
            #Resaltar el camino más corto en otro color
            path_edges = list(zip(self.shortest_path, self.shortest_path[1:]))
            nx.draw_networkx_edges(self.graph, pos, edgelist=path_edges, edge_color='red', width=2)
            nx.draw_networkx_nodes(self.graph, pos, nodelist=self.shortest_path, node_color='orange', node_size=700)
        else:
            self.shortest_path = None

        image_path = self.file_path()
        plt.savefig(image_path)
        plt.close()

        return image_path

    
    def update(self, matrix, start_node, end_node):
        self.matrix = matrix
        self.add_nodes_and_edges()
        path = self.save_img(start_node, end_node)
        tag = self.load_img(path)

        if self.shortest_path:
            dpg.set_value(self.text_info, f"Elementos del grafo:\n{str(self.graph.edges)}\nCamino más corto de {start_node} a {end_node}:\n {self.shortest_path}")
        else:
            dpg.set_value(self.text_info, f"Elementos del grafo:\n{str(self.graph.edges)}")

        if self.image !=None:
            dpg.configure_item(self.image, texture_tag=tag)
        else:
            self.image = dpg.add_image(tag, parent=self.parent)
        

    def display_graph(self):
        with dpg.window(label="Grafo asociado a la matriz", width=700, height=600) as self.parent:
            self.text_info = dpg.add_text(f"Elementos del grafo:\n{str(self.graph.edges)}\n")