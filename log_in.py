import flet as ft

def main(page: ft. Page):
    page.window_width = 360  # Smartphone-like width
    page.window_height = 800  # Smartphone-like height
    page.window_resizable = False  # Prevent resizing
    page.bgcolor = "black"