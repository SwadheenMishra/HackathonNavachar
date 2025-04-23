import flet as ft
import google.generativeai as genai
from datetime import datetime
import pyttsx3
import threading
import random
import time
from APIKEY import key #can't include obv


genai.configure(api_key=key)
engine = pyttsx3.init()
engine.setProperty("rate", 90)

model = genai.GenerativeModel('gemini-1.5-flash')

translate = False

def say(txt: str):
    global engine
    engine.say(txt)
    engine.runAndWait()

def chat(page: ft.Page, id: str):
    page.clean()
    page.bgcolor = None
    page.padding = 5
    page.vertical_alignment = ft.MainAxisAlignment.END
    
    page.appbar = ft.AppBar(
    leading=ft.IconButton(
        icon=ft.icons.HOME,
        width=30,
        height=30,
        on_click=lambda a: main(page)
    ),

    title=ft.Text(f"Chat with {id}"),
    center_title=True,
    bgcolor=ft.colors.BLUE,
    title_text_style=ft.TextStyle(color=ft.colors.WHITE, size=22),
    )   

    chat_column = ft.Column(expand=True, scroll=ft.ScrollMode.AUTO,)

    def send_message(e):
        text = message_field.value.strip()
        if text:
            time_str = datetime.now().strftime("%H:%M")
            chat_column.controls.append(
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text(text, color=ft.colors.WHITE),
                                    ft.Text(time_str, size=10, color=ft.colors.BLACK)
                                ]
                            ),
                            bgcolor=ft.colors.BLUE_400,
                            padding=10,
                            border_radius=10,
                            margin=5,
                            width=250,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.END,
                )
            )
            message_field.value = ""
            page.update()
            response = model.generate_content(
            f'Imagin like you are a cavemen on a dating site and your name is {id} and have the knowledge of a cavemen respond like a cave men to the following prompt in short: {text}').text
            add_message(response)

    def add_message(text: str):
        if text.strip():
            time_str = datetime.now().strftime("%H:%M")
            chat_column.controls.append(
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text(text, color=ft.colors.BLACK),
                                    ft.Text(time_str, size=10, color=ft.colors.BLACK)
                                ]
                            ),
                            bgcolor=ft.colors.LIGHT_GREEN_400,
                            padding=10,
                            border_radius=10,
                            margin=5,
                            width=250,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.START,
                )
            )
            page.update()

    message_field = ft.TextField(
        hint_text="Type a message...",
        expand=True,
        on_submit=send_message
    )

    send_button = ft.IconButton(
        icon=ft.icons.SEND,
        on_click=send_message
    )

    input_row = ft.Row(
        [message_field, send_button],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    page.add(
        ft.Column(
            controls=[
                ft.Container(
                    content=chat_column,
                    expand=True,
                    image_src="https://raw.githubusercontent.com/SwadheenMishra/HackathonNavachar/refs/heads/main/assets/3.png",
                    image_fit=ft.ImageFit.FILL,
                    image_opacity=0.5
                ),
                input_row
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    add_message(f"Ooga Booga i am {id}")

def profile(page: ft.Page, id: str="Cavemen"):
    page.clean()
    page.bgcolor = None
    page.appbar = ft.AppBar(leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda a: main(page)), 
                            bgcolor=ft.colors.BLUE,
                            title=ft.Text(id),
                            center_title=True
                            )
    
    profilePic = ft.CircleAvatar(
        foreground_image_src=f"https://raw.githubusercontent.com/SwadheenMishra/HackathonNavachar/refs/heads/main/assets/{id}.png",
        radius=30
    )

    def check(e):
        global translate
        
        translate = translateBtn.value

        print(translate)

    def play_audio(e):
        global engine, translate

        if not e.control.selected:
            n = random.randint(5, 8)

            if not translate:
                randomNoise = " ".join(random.choice(["OOOGA", "BOOOGA", "UHH"]) for i in range(n))
            else: 
                randomNoise = {
                    "Ben": "I Ben into hunting since i was 5 year's old",
                    "David": "I David love eating",
                    "James": "James sleep good",
                    "John": "John scared of fire",
                    "Michael": "Michael lonely",
                    "Robert": "Robert inscets bugs",
                    "Sophia": "Sophia Big strong",
                    }[id]
            # time.sleep(2)
            import pyttsx3
            
            engine = pyttsx3.init()
            engine.setProperty("rate", 90)
            engine.say(randomNoise)
            engine.runAndWait()
            engine.endLoop()

        e.control.update()

    audio = ft.Audio(src="https://github.com/SwadheenMishra/HackathonNavachar/blob/main/assets/cave%20(1).ogg")
    page.overlay.append(audio)
    
    lbl1 = ft.Text("About Me!", size=20)
    DiscriptionText = ft.Text(f"ooga booga! i am {id} booga ooga\ni like to uhhhh eat ooga and sleep booga")
    msgButton = ft.FloatingActionButton(icon=ft.icons.MESSAGE, on_click=lambda a, name=id: chat(page, id))
    audioLbl = ft.Text("Audio Description: ", size=20)
    playAudioBtn = ft.IconButton(icon=ft.icons.PLAY_CIRCLE, scale=1.6, on_click=play_audio, selected_icon=ft.icons.PAUSE_CIRCLE)
    translateBtn = ft.Checkbox("Translate", on_change=check)
    page.add(ft.Row([ft.Container(content=ft.Column([profilePic, lbl1, DiscriptionText, audioLbl, ft.Row([playAudioBtn, ft.Container(width=5), translateBtn])], expand=True), image_src="https://raw.githubusercontent.com/SwadheenMishra/HackathonNavachar/refs/heads/main/assets/2.png", image_opacity=0.2, expand=True, image_fit=ft.ImageFit.FILL)], expand=True), msgButton)
    audio.play()
    page.update()

def main(page: ft.Page):
    page.clean()
    page.appbar = None
    page.title = "Ooga Booga"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 450
    page.window_height = 700
    page.bgcolor = None
    

    images = ft.Column(expand=True, wrap=False, scroll=ft.ScrollMode.HIDDEN, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    imgFiles = ["Ben", "David", "James", "John", "Michael", "Robert", "Sophia"]


    for name in imgFiles:
        images.controls.append(
            ft.Card(
            content=ft.Container(content=ft.Column([
            ft.Image(
                src=f"https://raw.githubusercontent.com/SwadheenMishra/HackathonNavachar/refs/heads/main/assets/{name}.png",
                width=300,
                height=400,
                fit=ft.ImageFit.FILL,
                repeat=ft.ImageRepeat.NO_REPEAT,
                gapless_playback=False
            ),
            ft.Row([ft.Text(f"Name: {name}"), ft.ElevatedButton(text="View Profile", icon="profile", on_click=lambda a, name=name: profile(page, id=name))], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            #ft.Container(height=5)
        ], alignment=ft.MainAxisAlignment.CENTER), padding=15), surface_tint_color=ft.colors.BLUE_GREY_100, width=330)
        )

    page.add(ft.Row([ft.Container(content=images, image_src="https://raw.githubusercontent.com/SwadheenMishra/HackathonNavachar/refs/heads/main/assets/1.png", expand=True, image_fit=ft.ImageFit.FILL)], expand=True, alignment=ft.MainAxisAlignment.CENTER))
    page.update()

ft.app(main)
