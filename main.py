import flet as ft
import random

def main(page: ft.Page):
    page.title = "Images Example"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 450
    page.window_height = 700
    page.padding = 50

    images = ft.Column(expand=False, wrap=False, scroll=ft.ScrollMode.HIDDEN, adaptive=True, alignment=ft.MainAxisAlignment.CENTER)

    imgFiles = ['1.png', '2.jpg', '1.png', '2.jpg', '1.png', '2.jpg', '1.png']

    for i in imgFiles:
        images.controls.append(ft.Text(f"Name: {random.choice(["BOB", "Bryan", "Britny"])}"))

        images.controls.append(
            ft.Image(
                src=i,
                width=300,
                height=400,
                fit=ft.ImageFit.CONTAIN,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
                gapless_playback=False
            ),
        )

        images.controls.append(ft.ElevatedButton())

    page.add(ft.Row([images], expand=True, alignment=ft.MainAxisAlignment.CENTER))
    page.update()
ft.app(main)