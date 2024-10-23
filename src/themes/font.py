import dearpygui.dearpygui as dpg
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    return os.path.join(base_path, relative_path)

with dpg.font_registry():
    font_path = resource_path(os.path.join('assets','fonts', 'LibreFranklin-Thin.ttf'))
    global_font = dpg.add_font(file=font_path, size=14)