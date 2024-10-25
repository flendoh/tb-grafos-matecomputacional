import dearpygui.dearpygui as dpg

with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        # Colores de fondo
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (25, 25, 25, 255))  # Fondo de ventana casi negro
        dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (40, 40, 40, 255))  # Fondo de título oscuro
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (60, 60, 60, 255))  # Título activo más claro
        dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 8, 8)  # Bordes más redondeados

        # Colores de texto
        dpg.add_theme_color(dpg.mvThemeCol_Text, (220, 220, 220, 255))  # Texto principal claro
        dpg.add_theme_color(dpg.mvThemeCol_TextDisabled, (140, 140, 140, 255))  # Texto deshabilitado

        # Colores de botones
        dpg.add_theme_color(dpg.mvThemeCol_Button, (80, 80, 80, 255))  # Botón gris medio
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (100, 100, 100, 255))  # Hover más claro
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (120, 120, 120, 255))  # Activo aún más claro

        # Quitar bordes y sombras
        dpg.add_theme_color(dpg.mvThemeCol_Border, (0, 0, 0, 0))  # Borde transparente
        dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, (0, 0, 0, 0))  # Sombra transparente

        # Colores adicionales para mejorar el contraste
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (45, 45, 45, 255))  # Fondo de widgets
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (55, 55, 55, 255))  # Hover de widgets
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (65, 65, 65, 255))  # Widget activo

        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4, 4)  # Bordes redondeados en widgets
        dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 0)  # Sin borde de ventana
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0)  # Sin borde en frames
        dpg.add_theme_style(dpg.mvStyleVar_TabRounding, 4)  # Pestañas redondeadas
