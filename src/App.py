import dearpygui.dearpygui as dpg
from screens.config_graph import ConfigGraph
from screens.credits import Credits
from screens.instructions import Instructions
dpg.create_context()
from themes.font import *
from themes.theme import *

class App:
    def __init__(self, title="Problema del camino minimo", width=1480, height=820):
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

    def display_menu(self):
        with dpg.window(label="Menú", no_close=True, no_resize=True):
            dpg.add_button(label="Generar Grafo", width=200, callback=lambda: self.add_screen(ConfigGraph()))
            dpg.add_button(label="Enunciado", width=200, callback=lambda: self.add_screen(Instructions()))
            dpg.add_button(label="Credítos", width=200, callback=lambda: self.add_screen(Credits()))
            dpg.add_button(label="Salir", width=200, callback=dpg.stop_dearpygui)

    def add_screen(self, screen):
        screen.create()

if __name__ == "__main__":
    app = App()
    app.display_menu()
    app.run()


