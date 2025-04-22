import flet as ft
import random

def profile(page: ft.Page, id: str = None):
    page.clean()
    page.update()

def main(page: ft.Page):
    page.title = "Ooga Booga"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 450
    page.window_height = 700

    images = ft.Column(expand=False, wrap=False, scroll=ft.ScrollMode.HIDDEN, alignment=ft.MainAxisAlignment.CENTER)

    imgFiles = ['1.png', '1.png', '1.png', '1.png', '1.png', '1.png', '1.png']

    for i in imgFiles:
        #images.controls.append()
        name = random.choice(["BOB", "Bryan", "Britny", "Laim", "Jhon", "Josh"])

        images.controls.append(
            ft.Card(
            content=ft.Container(content=ft.Column([
            ft.Image(
                src=i,
                width=300,
                height=400,
                fit=ft.ImageFit.CONTAIN,
                repeat=ft.ImageRepeat.NO_REPEAT,
                gapless_playback=False
            ),
            ft.Row([ft.Text(f"Name: {name}"), ft.Container(width=65), ft.ElevatedButton(text="View Profile", icon="profile", on_click=lambda a: profile(page, id=name))]),
            #ft.Container(height=5)
        ], alignment=ft.MainAxisAlignment.CENTER), padding=15))
        )

    page.add(ft.Row([images], expand=True, alignment=ft.MainAxisAlignment.CENTER))
    page.update()
ft.app(main)
