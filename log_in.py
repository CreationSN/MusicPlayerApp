import flet as ft

def main(page: ft. Page):
    page.window_width = 360  
    page.window_height = 800  
    page.window_resizable = False  
    page.bgcolor = "black"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER



    songs=ft.Text(
        "Millions of Free Songs.",
        color="white",
        size=25,
        weight="bold",
        text_align=ft.TextAlign.CENTER,
    )

    page.add(ft.Container(
        content=songs,
        #bgcolor="black",
        margin=ft.Margin(30, 200, 30, 0),
    ))    


    create=ft.ElevatedButton(
        "Log in",
        color="white",
        bgcolor="green",
        width=300,
        height=40,
        #on_click=lambda _: page.go("/form.result"),
    ) 
   
    button_row = ft.Column(
        controls=[
            create
        ],
        alignment=ft.MainAxisAlignment.START,
        expand=True,
    ) 
        
    page.add(ft.Container(
    content=button_row,
    expand=True,
    margin=ft.Margin(0, 20, 0, 0), 
))

ft.app(main)