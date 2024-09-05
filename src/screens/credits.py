import dearpygui.dearpygui as dpg

class Credits:
    def __init__(self) -> None:
        self.texto = """
Sección: SX41
Profesor:
Grupo: 5
Integrantes:
-
-
-
-
                """
        pass

    def create(self):
        with dpg.window(label="Credítos"):
            dpg.add_text(self.texto)