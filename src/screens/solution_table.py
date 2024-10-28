import math
import dearpygui.dearpygui as dpg
import networkx as nx

class SolutionTable:
    def __init__(self): 
        self.steps = []
        self.current_step = 0
        self.final_path = []
        self.total_weight = 0

    def create(self, graph: nx.Graph, start_node, end_node):
        self.calculate_steps(graph, start_node, end_node)

        with dpg.window(label="Demostración de Dijkstra", height=410, width=500, modal=True, show=True, tag="solution_table", 
                       on_close=lambda: dpg.delete_item("solution_table"), pos=(360, 100)):
            dpg.add_text("Progreso del Algoritmo de Dijkstra", bullet=True)
            dpg.add_separator()
            dpg.add_text("", tag="current_node_text")
            dpg.add_separator()
            
            with dpg.table(header_row=True):
                dpg.add_table_column(label="Nodo")
                dpg.add_table_column(label="Distancia")
                dpg.add_table_column(label="Predecesor")
                for node in graph.nodes:
                    with dpg.table_row(tag=f"row_{node}"):
                        dpg.add_text("", tag=f"node_{node}")
                        dpg.add_text("", tag=f"distance_{node}")
                        dpg.add_text("", tag=f"predecessor_{node}")

            with dpg.group(horizontal=True):
                dpg.add_button(label="Paso Anterior", callback=self.previous_step, width=100)
                dpg.add_button(label="Siguiente Paso", callback=self.next_step, width=100)

            dpg.add_separator()
            dpg.add_text("", tag="final_path_text")
            dpg.add_text("", tag="total_weight_text")

        self.show_step()

    def calculate_steps(self, graph, start_node, end_node):
        distances = {node: float('inf') for node in graph.nodes}
        predecessors = {node: None for node in graph.nodes}
        distances[start_node] = 0
        unvisited = set(graph.nodes)

        while unvisited:
            current_node = min(unvisited, key=lambda node: distances[node])
            unvisited.remove(current_node)
            self.steps.append((current_node, dict(distances), dict(predecessors)))

            if current_node == end_node:
                self.final_path = self.reconstruct_path(predecessors, start_node, end_node)
                self.total_weight = distances[end_node]
                break

            for neighbor in graph.neighbors(current_node):
                if neighbor in unvisited:
                    weight = graph[current_node][neighbor].get('weight', 1)
                    new_distance = distances[current_node] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        predecessors[neighbor] = current_node

    def reconstruct_path(self, predecessors, start_node, end_node):
        path = []
        current = end_node
        while current is not None:
            path.append(current)
            current = predecessors[current]
        path.reverse()
        return path if path[0] == start_node else []

    def show_step(self):
        if 0 <= self.current_step < len(self.steps):
            current_node, distances, predecessors = self.steps[self.current_step]
            dpg.set_value("current_node_text", f"Paso {self.current_step + 1}: Nodo actual procesado: {current_node}")
            
            for node in distances:
                dist = distances[node] if distances[node] != float('inf') else 'Inf'
                pred = predecessors[node] if predecessors[node] is not None else '-'
                node_text = f"{node} (actual)" if node == current_node else str(node)
                dpg.set_value(f"node_{node}", node_text)
                dpg.set_value(f"distance_{node}", dist)
                dpg.set_value(f"predecessor_{node}", pred)

            if self.current_step == len(self.steps) - 1:
                path_str = " -> ".join(map(str, self.final_path))
                dpg.set_value("final_path_text", f"Camino más corto: {path_str}")
                dpg.set_value("total_weight_text", f"Peso total: {self.total_weight}")

    def previous_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            self.show_step()

    def next_step(self):
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
            self.show_step()
