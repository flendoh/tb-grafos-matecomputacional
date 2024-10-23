import dearpygui.dearpygui as dpg
from screens.config_graph import ConfigGraph
from screens.credits import Credits
from screens.instructions import Instructions
dpg.create_context()
from themes.font import *
from themes.theme import *

class App:
    def __init__(self, title="Problema del camino minimo", width=900, height=600):
        self.title = title
        self.width = width
        self.height = height
        dpg.create_viewport(title=self.title, width=self.width, height=self.height)
        self.apply_styles()
        dpg.setup_dearpygui()
    
    def apply_styles(self):
        dpg.bind_font(global_font)
        dpg.bind_theme(global_theme)

    def run(self):
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

    def main_window_setup(self):
        with dpg.window() as self.main_window:
            self.display_menu_bar()
            with dpg.group(horizontal=True):
                with dpg.child_window(width=300) as self.graph_config:
                    pass
                with dpg.child_window() as self.graph_preview:
                    pass
        dpg.set_primary_window(self.main_window, True)

    def display_menu_bar(self):
        with dpg.menu_bar():
            with dpg.menu(label="Archivo"):
                dpg.add_menu_item(label="Resetear Grafo")
                dpg.add_menu_item(label="Salir", callback=dpg.stop_dearpygui)
            with dpg.menu(label="Acerca de"):
                dpg.add_menu_item(label="Enunciado")
                dpg.add_menu_item(label="Creditos")


    def add_screen(self, screen):
        screen.create()

if __name__ == "__main__":
    app = App()
    app.main_window_setup()
    app.run()


