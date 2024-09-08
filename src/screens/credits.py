import dearpygui.dearpygui as dpg

class Credits:
    def __init__(self) -> None:
        self.texto = """Sección: SX41
Profesor: Jonathan Abrahan Sueros Zarate
Grupo: 5
Integrantes:
- Cossar Sanchez, Eduardo Jose
- Hallasi Saravia, Miguel Angel
- Meza Puchoc, Raul Jean
- Oliva Lopez, Fabian Alejandro
- Rengifo Del Castillo, River Martín
"""
        pass

    def create(self):
        with dpg.window(label="Credítos"):
            dpg.add_text(self.texto)