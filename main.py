import flet as ft

def login_screen(page, navigate_to):
    page.clean()
    page.add(
        ft.Text("Millions of Free Songs.", size=24),
        ft.ElevatedButton("Log in", on_click=lambda _: navigate_to("home")),
        ft.Text("or Create an Account", size=12),
        ft.ElevatedButton("Create account", on_click=lambda _: navigate_to("signup"))
    )
    page.update()
