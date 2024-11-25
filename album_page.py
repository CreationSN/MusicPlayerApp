import flet as ft 
from playsound import playsound
import threading

def main(page : ft.Page):

    page.window_width = 360
    page.window_height = 800
    #page.vertical_alignment = ft.MainAxisAlignment.START
    #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_resizable = False
    page.bgcolor = ft.LinearGradient(
        begin=ft.Alignment(0,0),  # Start the gradient from the top
        end=ft.Alignment(0,1),  # End the gradient at the bottom
        colors=["#00FF00", "#000000"],  # Green at the top (#00FF00) and black at the bottom (#000000)
    )
    
    
    bird_sound= "assets/music/Bird Sounds Spectacular _ Morning Bird Sound.mp3"
    cat_sound = "assets/music/REALISTIC CAT SOUND 15MIN!!.mp3"
    dog_sound = "assets/music/Sounds That Tilt a Dogs Head  Sounds Dogs Love.mp3"
    

    
    def play_sound(file_path):
        threading.Thread(target=playsound, args=(file_path,), daemon=True).start()
        
    def play_sound1(e):
        play_sound(bird_sound)
        
    def play_sound2(e):
        play_sound(cat_sound)
        
    def play_sound3(e):
        play_sound(dog_sound)
    

    #image  
    album_img = ft.Image(
        src=r"assets/images/cartoon-wild-animals-collection-set-2AN691H.jpg",
        width=150,
        height=150,
    )
    artist_img = ft.Image(
        src=r"assets/images/catpic.png",
        width=40,
        height=40,
        border_radius=ft.border_radius.all(15)
    )
    dot = ft.Image(
        src=r"assets/images/dot-small-svgrepo-com.svg",
        width=18,
        height=18,
        border_radius=ft.border_radius.all(15),
        color = "white"
    )
    
    
    Album_name = ft.Text("Animals Sounds",size= 20,weight=ft.FontWeight.BOLD)
    Artist_name = ft.Text("Animals",size= 15,weight=ft.FontWeight.BOLD)
    Album = ft.Text("Album",size = 10)
    Album_year=ft.Text("2024",size = 10)


    back_button = ft.Container(
            content =ft.Image(
                src=r"assets/images/navigation-back-arrow-svgrepo-com.svg",
                width=12,
                height=12,
                color = "white"           
            ),
            padding=ft.Padding(top=30, left=10, right=0, bottom=0)
    )                       


    play_button = ft.Container(        
            content=ft.Image(
                src=r"assets/images/play-button-svgrepo-com.svg",
                width=50,
                height=50,
                color = "green",                         
            ),
            padding=ft.padding.only(right=10)
        )
    
    shuffle_button = ft.Container(        
            content=ft.Image(
                src=r"assets/images/shuffle-svgrepo-com.svg",
                width=40,
                height=40,
                color = "white",            
            )
        )
    
    
    three_dots_button = ft.Container(        
            content=ft.Image(
                src=r"assets/images/3 dot.svg",
                width=20,
                height=20,
                color = "white"
            ),
        )

    heart_button = ft.Container(        
            content=ft.Image(
                src=r"assets/images/heart.svg",
                width=20,
                height=20,
                color = "white"
            ),
            padding=ft.Padding(top=0, left=10, right=0, bottom=0)
        )
    
    download_button =  ft.Container(        
            content=ft.Image(
                src=r"assets/images/download.png",
                width=20,
                height=20,
                color = "green"
            ),
        )

    right_group  = ft.Row(
        controls=[shuffle_button,play_button],
        alignment=ft.MainAxisAlignment.END, # Align the container to the left side
        spacing=20
    )

    left_group  = ft.Row(
        controls=[heart_button, download_button , three_dots_button],
        alignment=ft.MainAxisAlignment.START, # Align the container to the left side
        spacing=20
    )

    icon_group= ft.Row(
        controls=[left_group, right_group],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )
    
    
    content1=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        trailing = three_dots_button,
                        title=ft.Text("Bird sound"),
                        subtitle=ft.Text(
                            "Bird"
                        ),
                    ),
                    
                ]
            ),
            width=400,
            height=60,
            on_click= play_sound1,           
        )

    content2=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        trailing = three_dots_button,
                        title=ft.Text("Cat Sound"),
                        subtitle=ft.Text(
                            "Cat"
                        ),
                    ),
                    
                ]
            ),
            width=400,
            height=60,
            on_click= play_sound2           
        )

    content3=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        trailing = three_dots_button,
                        title=ft.Text("Dog Sound"),
                        subtitle=ft.Text(
                            "Dog"
                        ),
                    ),                    
                ]
            ),
            width=400,
            height=60,
            on_click= play_sound3           
        )

    #positioning image
    album_img_container = ft.Container(
        content=album_img,
        alignment=ft.alignment.center,  # Center the image horizontally
        padding=ft.Padding(top=30, left=0, right=0, bottom=0),  # Offset from the top (100px)
    )
    artist_img_container = ft.Container(
        content=artist_img,
        alignment=ft.alignment.center,  # Center the image horizontally
        padding=ft.Padding(top=0, left=10, right=0, bottom=0),  # Offset from the top (100px)
    )           
    
    Album_name_container = ft.Container(
        content=Album_name,
        padding=ft.Padding(top=10, left=20, right=0, bottom=0),  # 20px left padding for the text container
        alignment=ft.Alignment(0, 0),  # Align the text inside the container
    )   
    Artist_name_container = ft.Container(
        content=Artist_name,
        padding=ft.Padding(top=0, left=10, right=0, bottom=0),  # 20px left padding for the text container
        alignment=ft.Alignment(0, 0),  # Align the text inside the container
    )
    Album_container = ft.Container(
        content=Album,
        padding=ft.Padding(top=0, left=15, right=0, bottom=0),  # 20px left padding for the text container
        alignment=ft.Alignment(0, 0),  # Align the text inside the container
    )
    Album_row = ft.Row(
        controls=[Album_container,dot,Album_year],
        alignment=ft.MainAxisAlignment.START,
        spacing=2
    )  
    
    Album_name_row = ft.Row(
        controls=[Album_name_container],
        alignment=ft.MainAxisAlignment.START,  # Align the container to the left side
    )  
    # Use Row to horizontally align the container (text container)
    Artist_name_img_row = ft.Row(
        controls=[artist_img_container,Artist_name_container],
        alignment=ft.MainAxisAlignment.START,  # Align the container to the left side
    )  
    
    
    #adding navigation bar
    navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.icons.HOME,
                selected_icon=ft.icons.HOME_OUTLINED,                         
                label="Home"),
            ft.NavigationBarDestination( 
                icon=ft.icons.SEARCH,
                selected_icon=ft.icons.SEARCH_OUTLINED,                        
                label="Search"),
            ft.NavigationBarDestination(
                icon=ft.icons.LIBRARY_BOOKS,
                selected_icon=ft.icons.LIBRARY_BOOKS_OUTLINED,
                label="Your Library",
            ),
        ],
        bgcolor=ft.colors.TRANSPARENT,
    )

    
    
    #page.add(ft.Row(controls=back_button, alignment=ft.MainAxisAlignment.START))
    page.add(back_button)
    page.add(album_img_container) #placing image
    page.add(Album_name_row)
    page.add(Artist_name_img_row)
    page.add(Album_row)
    page.add(icon_group)
    page.add(ft.Column([content1,content2,content3], spacing=0))
    
    page.add(navigation_bar)
    
ft.app(target=main)

