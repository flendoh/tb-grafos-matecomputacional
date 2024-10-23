import dearpygui.dearpygui as dpg

with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        # Establecer colores de fondo
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (30, 30, 30, 255))  # Fondo de la ventana
        dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (35, 35, 38, 255))  # Fondo del título
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (75, 75, 78, 255))  # Fondo del título activ
        dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 4, 4)

        # Establecer colores de texto
        dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))  # Color del texto
        dpg.add_theme_color(dpg.mvThemeCol_TextDisabled, (128, 128, 128, 255))  # Color del texto deshabilitad
        # Establecer colores de botones
        dpg.add_theme_color(dpg.mvThemeCol_Button, (70, 70, 70, 255))  # Fondo del botón
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (90, 90, 90, 255))  # Fondo del botón al pasar el ratón
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (110, 110, 110, 255))  # Fondo del botón activ
        # Establecer colores de bordes
        dpg.add_theme_color(dpg.mvThemeCol_Border, (0, 0, 0, 0))  # Color del borde
        dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, (0, 0, 0, 0))  # Sombra del borde
