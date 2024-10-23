import dearpygui.dearpygui as dpg

class Instructions:
    def __init__(self) -> None:
        pass

    def create(self):
        with dpg.window(label="Enunciado", modal=True, show=True, tag="instructions_popup", no_resize=True, pos=(400, 225), on_close=lambda: dpg.delete_item("instructions_popup")):
            dpg.add_text("""Problema del camino mínimo
Dado n pertenece [8, 16] ingresado por el usuario, el programa debe generar aleatoriamente
una matriz simétrica n x n (con elementos positivos) o solicitar el ingreso de cada
elemento de la matriz (según decisión del usuario). Además, debe mostrar el grafo
etiquetado asociado a esta matriz y el camino mínimo que existe entre dos vértices
seleccionados por el usuario. Todo el proceso, desde la generación de la matriz hasta
el cálculo del camino mínimo, se debe mostrar paso a paso, proporcionando una
visualización clara y detallada del funcionamiento interno del algoritmo.""")