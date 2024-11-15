import flet as ft


def main(page: ft.Page):
    page.title = "Create account"
    page.window_width = 360  
    page.window_height = 800  
    page.window_resizable = False  
    page.bgcolor = "black"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    log_in=ft.Text(
        "Create account",
        color="white",
        size=25,
        weight="bold",
        text_align=ft.TextAlign.CENTER,
    )

    page.add(ft.Container(
        content=log_in,
        bgcolor="black",
        margin=ft.Margin(20, 0, 0, 0),
    ))

    name=ft.TextField(
        label="What's your name?",
        color="white",
        border_color="white",
        text_size=20,
        #weight="bold",
        border_width=2,
        width=300,
        height=50,
        text_align=ft.TextAlign.LEFT,
    )
  
    page.add(ft.Container(
        content=name,
        bgcolor="black",
        margin=ft.Margin(0, 20, 0, 0),  
    ))

    profile=ft.Text(
        "This name will appear in your profile",
        color="white",
        size=8,
        weight="bold",
        text_align=ft.TextAlign.LEFT,
    )
    page.add(ft.Container(
    content=profile,
    bgcolor="black",
    margin=ft.Margin(15, 1, 0, 0),  
    alignment=ft.alignment.top_left,
    ))

    line = ft.Divider(
        color="grey",  
        thickness=1,    
        
    )

   

    page.add(ft.Container(
    content=line,
    margin=ft.Margin(15, 0, 15, 0),  
))


    privacy=ft.Text(
        "By tapping on Create account you agree to our Privacy Policy and Terms of use",
        color="white",
        size=10,
        weight="bold",
        text_align=ft.TextAlign.LEFT,
    )

     

    page.add(ft.Container(
        content=privacy,
        bgcolor="black",
        margin=ft.Margin(15, 0, 10, 15),  
    ))

    create=ft.ElevatedButton(
        "Create an account",
        color="white",
        bgcolor="green",
        width=200,
        height=50,
        #on_click=lambda _: page.go("/form.result"),
    ) 
   
    button_row = ft.Column(
        controls=[
            create
        ],
        alignment=ft.MainAxisAlignment.END,
        expand=True,
    ) 
        
    page.add(ft.Container(
    content=button_row,
    expand=True,
    margin=ft.Margin(0, 0, 0, 60), 
))

 # I need to add link to make navigation between pages, I will do it later


ft.app(main)
