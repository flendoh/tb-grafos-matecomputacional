import dearpygui.dearpygui as dpg

class App:
    def __init__(self, title="TB MateComputacional", width=1480, height=820):
        self.title = title
        self.width = width
        self.height = height
        dpg.create_context()
        dpg.create_viewport(title=self.title, width=self.width, height=self.height)
        self.apply_styles()
        dpg.setup_dearpygui()
    
    def apply_styles(self):
        with dpg.theme() as global_theme:
            with dpg.theme_component(dpg.mvAll):
                # Establecer colores de fondo
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (30, 30, 30, 255))  # Fondo de la ventana
                dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (45, 45, 48, 255))  # Fondo del título
                dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (75, 75, 78, 255))  # Fondo del título activo

                # Establecer colores de texto
                dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))  # Color del texto
                dpg.add_theme_color(dpg.mvThemeCol_TextDisabled, (128, 128, 128, 255))  # Color del texto deshabilitado

                # Establecer colores de botones
                dpg.add_theme_color(dpg.mvThemeCol_Button, (70, 70, 70, 255))  # Fondo del botón
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (90, 90, 90, 255))  # Fondo del botón al pasar el ratón
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (110, 110, 110, 255))  # Fondo del botón activo

                # Establecer colores de bordes
                dpg.add_theme_color(dpg.mvThemeCol_Border, (128, 128, 128, 255))  # Color del borde
                dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, (0, 0, 0, 0))  # Sombra del borde

        dpg.bind_theme(global_theme)

    def run(self):
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

    def add_screen(self, screen):
        screen.create()

if __name__ == "__main__":
    from screens.config_graph import ConfigGraph
    app = App()
    config_screen = ConfigGraph()
    app.add_screen(config_screen)
    app.run()


