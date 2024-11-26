import flet as ft
#import asyncio
#import log_in 


def main(page: ft.Page):
    page.window_width = 360  
    page.window_height = 800  
    page.window_resizable = False  
    page.bgcolor = "black"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    image_path = "assets/images/musicappicon.png"   


    
    image=ft.Image(
        src=image_path,
        fit=ft.ImageFit.COVER,
        width=100,
        height=100,
    )

    page.add(ft.Container(
        content=image,
        margin=ft.Margin(50, 300, 50, 50),   
    ))

    """


    image=ft.Image(
        src=image_path, fit=ft.ImageFit.COVER,
        width=100,
        height=100,
    )"""

    #page.add(image)


    """
    main_view = log_in.main(page)
    print(main_view) 
    main_view.visible = False  

    page.add(loading_view, main_view)

    page.add(loading_view)
    page.update()

    page.add(main_view)  
    page.update()
    """


    """
    main1 = ft.Column(
        visible=False
    )

    page.add(main1, loading_view)

    page.add(ft.Container(
        content=image,
        margin=ft.Margin(50, 300, 50, 50),   
    ))"""
"""
    async def switch_to_main_view():
        await asyncio.sleep(3)
        loading_view.visible = False  
        main_view.visible = True  
        page.update()


    asyncio.run(switch_to_main_view())"""

# I tried to make 3s delay and navigation to next page after that, I didn't succeed, dk how to do it


ft.app(target=main)

