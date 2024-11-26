import flet as ft
import os

def main(page: ft.Page):
    page.title = "Music Player App - Home"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 10
    page.window_width = 360  
    page.window_height = 800  
    page.window_resizable = False 
    page.scroll = ft.ScrollMode.AUTO
    image_path = lambda img: os.path.join(os.getcwd(), "assets/images", img)

    # Header Section
    recently_played_header = ft.Row(
        [
            ft.Text(
                "Recently played", 
                style=ft.TextThemeStyle.TITLE_MEDIUM, 
                weight=ft.FontWeight.BOLD
            ),
            ft.Row(
                [
                    ft.IconButton(icon=ft.icons.NOTIFICATIONS, tooltip="Notifications", icon_size=18),
                    ft.IconButton(icon=ft.icons.HISTORY, tooltip="Your Library", icon_size=18),
                    ft.IconButton(icon=ft.icons.SETTINGS, tooltip="Settings", icon_size=18),
                ],
                spacing=5,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    # Recently Played Section
    recently_played_section = ft.Row(
        [
            ft.Column(
                [
                    ft.Container(
                        content=ft.Image(src=image_path("image-1.png"), fit=ft.ImageFit.COVER),
                        width=70, height=70, padding=5,
                    ),
                    ft.Text("1 (Remastered)", size=12, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            ft.Column(
                [
                    ft.Container(
                        content=ft.Image(src=image_path("image-2.png"), fit=ft.ImageFit.COVER),
                        width=70, height=70, padding=5,
                    ),
                    ft.Text("Lana Del Rey", size=12, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            ft.Column(
                [
                    ft.Container(
                        content=ft.Image(src=image_path("image-3.png"), fit=ft.ImageFit.COVER),
                        width=70, height=70, padding=5,
                    ),
                    ft.Text("Marvin Gaye", size=12, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            ft.Column(
                [
                    ft.Container(
                        content=ft.Image(src=image_path("image-4.png"), fit=ft.ImageFit.COVER),
                        width=70, height=70, padding=5,
                    ),
                    ft.Text("Indie Pop", size=12, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=5,
    )

    # Year in Review Section
    year_in_review_section = ft.Column(
        [
            ft.Row(
                [
                    ft.Container(
                        content=ft.Image(
                            src=image_path("image-5.png"),
                            fit=ft.ImageFit.COVER,
                        ),
                        width=50, height=50, border_radius=5, padding=5,
                    ),
                    ft.Column(
                        [
                            ft.Text(
                                "#SPOTIFYWRAPPED", 
                                color=ft.colors.GREEN_ACCENT_700, 
                                size=8, 
                                weight=ft.FontWeight.BOLD
                            ),
                            ft.Text(
                                "Your 2021 in review", 
                                style=ft.TextThemeStyle.TITLE_MEDIUM, 
                                weight=ft.FontWeight.BOLD
                            ),
                        ],
                        spacing=2,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=5,
            ),
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Container(
                                content=ft.Image(src=image_path("image-6.png"), fit=ft.ImageFit.COVER),
                                width=120, height=120, padding=5,
                            ),
                            ft.Text("Your Top Songs 2021", size=12, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                    ft.Column(
                        [ 
                            ft.Container(
                                content=ft.Image(src=image_path("image-7.png"), fit=ft.ImageFit.COVER),
                                width=120, height=120, padding=5,
                            ),
                            ft.Text("Your Artists", size=12, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),  
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=5,
            ),
        ],
        spacing=8,
    )

    # Editor's Picks Section
    editors_picks_section = ft.Column(
        [
            ft.Text(
                "Editor's picks", 
                style=ft.TextThemeStyle.TITLE_MEDIUM, 
                weight=ft.FontWeight.BOLD
            ),
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Container(
                                content=ft.Image(src=image_path("image-8.png"), fit=ft.ImageFit.COVER),
                                width=120, height=120, padding=5,
                            ),
                            ft.Text(
                                "Ed Sheeran, Big Sean, Juice WRLD, Post Malone",
                                size=10, text_align=ft.TextAlign.CENTER,
                                max_lines=2,
                                weight=ft.FontWeight.NORMAL,
                                width=120,  
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                    ft.Column(
                        [
                            ft.Container(
                                content=ft.Image(src=image_path("image-9.png"), fit=ft.ImageFit.COVER),
                                width=120, height=120, padding=5,
                            ),
                            ft.Text(
                                "Mitski, Tame Impala, Glass Animals, Charli XCX",
                                size=10, text_align=ft.TextAlign.CENTER,
                                max_lines=2,
                                weight=ft.FontWeight.NORMAL,
                                width=120,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                    ft.Column(
                        [
                            ft.Container(
                                content=ft.Image(src=image_path("image-10.png"), fit=ft.ImageFit.COVER),
                                width=120, height=120, padding=5,
                            ),
                            ft.Text(
                                "Rihanna, Drake, SZA, Tyler, The Creator",
                                size=10, text_align=ft.TextAlign.CENTER,
                                max_lines=2,
                                weight=ft.FontWeight.NORMAL,
                                width=120,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                ],
                spacing=10,
            ),
        ],
        spacing=8,
    )

    # Bottom Navigation Bar
    bottom_navigation = ft.Column(
        [
            ft.Divider(height=1, thickness=2, color=ft.colors.BLUE),
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Icon(ft.icons.HOME, tooltip="Home", size=24),
                            ft.Text("Home", size=12),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Column(
                        [
                            ft.Icon(ft.icons.SEARCH, tooltip="Search", size=24),
                            ft.Text("Search", size=12),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Column(
                        [
                            ft.Icon(ft.icons.LIBRARY_MUSIC, tooltip="Library Music", size=24),
                            ft.Text("Your Library", size=12),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                spacing=30,
            ),
        ],
        spacing=5,
    )

    # Page Layout
    page.add(
        ft.Column(
            [
                recently_played_header,
                ft.Container(recently_played_section, margin=ft.margin.symmetric(vertical=10)),
                year_in_review_section,
                editors_picks_section,
                bottom_navigation,
            ],
            spacing=15,
        )
    )

ft.app(target=main)
