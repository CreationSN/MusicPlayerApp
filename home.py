import flet as ft
import os

def main(page: ft.Page):
    page.title = "Music Player - Home"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 10
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
            ft.Container(
                content=ft.Image(src=image_path("image-1.png"), fit=ft.ImageFit.COVER),
                width=70, height=70, padding=5,
            ),
            ft.Container(
                content=ft.Image(src=image_path("image-2.png"), fit=ft.ImageFit.COVER),
                width=70, height=70, padding=5,
            ),
            ft.Container(
                content=ft.Image(src=image_path("image-3.png"), fit=ft.ImageFit.COVER),
                width=70, height=70, padding=5,
            ),
            ft.Container(
                content=ft.Image(src=image_path("image-4.png"), fit=ft.ImageFit.COVER),
                width=70, height=70, padding=5,
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
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
                                size=10, 
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
                spacing=10,
            ),
            ft.Row(
                [
                    ft.Container(
                        content=ft.Image(src=image_path("image-6.png"), fit=ft.ImageFit.COVER),
                        width=120, height=120, padding=5,
                    ),
                    ft.Container(
                        content=ft.Image(src=image_path("image-7.png"), fit=ft.ImageFit.COVER),
                        width=120, height=120, padding=5,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=15,
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
                    ft.Container(
                        content=ft.Image(src=image_path("image-8.png"), fit=ft.ImageFit.COVER),
                        width=70, height=70, padding=5,
                    ),
                    ft.Container(
                        content=ft.Image(src=image_path("image-9.png"), fit=ft.ImageFit.COVER),
                        width=70, height=70, padding=5,
                    ),
                    ft.Container(
                        content=ft.Image(src=image_path("image-10.png"), fit=ft.ImageFit.COVER),
                        width=70, height=70, padding=5,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
        ],
        spacing=8,
    )

    # Bottom Navigation Bar
    bottom_navigation = ft.Column(
        [
            ft.Divider(height=1, thickness=2, color=ft.colors.RED_ACCENT_100),
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

ft.app(target=main, assets_dir="assets")
