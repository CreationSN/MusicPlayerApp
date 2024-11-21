import flet as ft


def main(page: ft.Page):
    page.window_width = 360  
    page.window_height = 800  
    page.window_resizable = False  
    page.bgcolor = "black"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    image=ft.Image(
        src=r"MusicPlayerApp\assets\images\musicappicon.png",
        width=100,
        height=100,
    )

    #page.add(image)

    page.add(ft.Container(
        content=image,
        margin=ft.Margin(50, 300, 50, 50),   
    ))


ft.app(main)
