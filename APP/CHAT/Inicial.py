# Flet - Flutter
import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = "stretch"
    page.title = "Chat Unihosp"
    page.add(
        ft.Row(
            [
                ft.Icon(name=ft.icons.FACE, color=ft.colors.BLUE_300)

           
            ]
            )
    )

ft.app(target=main, view=ft.WEB_BROWSER, port=8000)


