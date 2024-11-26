import flet as ft
import os


def main(page: ft.Page):
    page.window_width = 360  
    page.window_height = 800  
    page.window_resizable = False  
    page.bgcolor = "black"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    image_path = "assets/images/musicappicon.png"


    image=ft.Image(
        src=image_path, fit=ft.ImageFit.COVER,
        width=100,
        height=100,
    )

    #page.add(image)

    page.add(ft.Container(
        content=image,
        margin=ft.Margin(50, 300, 50, 50),   
    ))


ft.app(target=main)

