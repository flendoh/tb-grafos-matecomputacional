import dearpygui.dearpygui as dpg

class Instructions:
    def __init__(self) -> None:
        pass

    def create(self):
        with dpg.window(label="Instrucciones"):
            dpg.add_text("""Enunciado: Problema del camino mínimo
Dado 𝑛 ∈ [8, 16] ingresado por el usuario, el programa debe generar aleatoriamente
una matriz simétrica 𝑛 × 𝑛 (con elementos positivos) o solicitar el ingreso de cada
elemento de la matriz (según decisión del usuario). Además, debe mostrar el grafo
etiquetado asociado a esta matriz y el camino mínimo que existe entre dos vértices
seleccionados por el usuario. Todo el proceso, desde la generación de la matriz hasta
el cálculo del camino mínimo, se debe mostrar paso a paso, proporcionando una
visualización clara y detallada del funcionamiento interno del algoritmo.""")