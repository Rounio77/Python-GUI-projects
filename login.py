import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Row, Column, Text
from flet_core.control_event import ControlEvent


def main(page: ft.Page) -> None:
    page.title = "Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    username_text: TextField = TextField(
        label="Username", text_align=ft.TextAlign.LEFT, width=200
    )
    password_text: TextField = TextField(
        label="Password", text_align=ft.TextAlign.LEFT, width=200, password=True
    )
    checkbox_signup: Checkbox = Checkbox(
        label="I agree to the Terms and Conditions", value=False
    )
    submit_button: ElevatedButton = ElevatedButton(
        text="Login", disabled=True, width=200
    )

    def validate(param: ControlEvent) -> None:
        if all([username_text.value, password_text.value, checkbox_signup.value]):
            submit_button.disabled = False
        else:
            submit_button.disabled = True
        page.update()

    def submit(param: ControlEvent) -> None:
        print("Username: ", username_text.value)
        print("Password: ", password_text.value)

        page.clean()
        page.add(
            Row(
                controls=[
                    Text(
                        value=f"Welcome {username_text.value}", size=20, disabled=False
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    username_text.on_change = validate
    password_text.on_change = validate
    checkbox_signup.on_change = validate
    submit_button.on_click = submit

    page.add(
        Row(
            controls=[
                Column(
                    [
                        username_text,
                        password_text,
                        checkbox_signup,
                        submit_button,
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


if __name__ == '__main__':
    ft.app(target=main)
