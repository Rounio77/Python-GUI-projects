# python GUI projects
#     basic login GUI using flet

import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent

def main(page: ft.Page) -> None:
    """
    This function creates a basic login GUI using Flet.
    """
    page.title = "signup"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    text_username: TextField = TextField(
        label="username", text_align=ft.TextAlign.LEFT, width=200
    )
    text_password: TextField = TextField(
        label="pasword", text_align=ft.TextAlign.LEFT, width=200, password=True
    )
    Checkbox_signup: Checkbox = Checkbox(
        label="i agree to the terms and conditions", value=False
    )
    button_submit: ElevatedButton = ElevatedButton(
        text="signup", width=200, disabled=True
    )

    def validate(param: ControlEvent) -> None:
        """
        This function is triggered when the user enters input into the text fields or checks the checkbox.
        It enables or disables the submit button based on whether all the required fields have been filled out.
        """
        if all([text_username.value, text_password.value, Checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
        page.update()

    def submit(param: ControlEvent) -> None:
        """
        This function is triggered when the submit button is clicked.
        It prints the inputted username and password to the console, and then clears the form and adds a welcome message.
        """
        print("username:", text_username.value)
        print("password:", text_password.value)

        page.clean()
        page.add(
            Row(
                controls=[
                    Text(
                        value=f"Welcome: {text_username.value}", size=20, disabled=False
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    Checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit

    page.add(
        Row(
            controls=[
                Column(
                    [
                        text_username,
                        text_password,
                        Checkbox_signup,
                        button_submit,
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
    