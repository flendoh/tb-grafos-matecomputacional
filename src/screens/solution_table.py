import dearpygui.dearpygui as dpg

class SolutionTable:
    def __init__(self):
        self.parent = None

    def create(self, dijkstra_result):
        with dpg.window(label="Solución", height=495, width=500, modal=True, show=True, 
                       on_close=lambda: dpg.delete_item("solution_table")) as self.parent:
            with dpg.table(header_row=True, parent=self.parent, resizable=False, pos=(500, 100)):
                predecessors, distances = dijkstra_result
                print(predecessors, distances)
                dpg.add_table_column(label="Nodo")
                
                num_steps = len(distances)
                for step in range(num_steps):
                    dpg.add_table_column(label=f"Paso {step + 1}")
                
                
                for node in distances:
                    with dpg.table_row():
                        dpg.add_text(node)
                        
                        for step in range(num_steps):
                            # TODO: Mostrar vertices adyacentes
                            dpg.add_text("-")
