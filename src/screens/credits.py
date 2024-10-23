import dearpygui.dearpygui as dpg

class Credits:
    def __init__(self) -> None:
        self.texto = """Sección: SX41
Profesor: Jonathan Abrahan Sueros Zarate
Grupo: 5
Integrantes:
- Eduardo Jose Cossar Sanchez
- Miguel Angel Hallasi Saravia
- Raul Jean Meza Puchoc
- Fabian Alejandro Oliva Lopez
- River Martín Rengifo Del Castillo
"""
        pass

    def create(self):
        with dpg.window(label="Creditos", modal=True, show=True, tag="credits_popup", no_resize=True, pos=(500, 225), on_close=lambda: dpg.delete_item("credits_popup")):
            dpg.add_text(self.texto)