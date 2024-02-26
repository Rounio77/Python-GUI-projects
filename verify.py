#python projects
#password generator and validator gui using flet

import flet as ft
import pyperclip
import random
import re
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent

def main(page: ft.Page) -> None:
    page.title = "password creator/validator"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 500
    page.window_height = 500
    page.window_resizable = False

    password_generator: TextField = TextField(label="digit(8-100)", text_align=ft.TextAlign.LEFT, width=200)
    checkbox_copy: Checkbox = Checkbox(label="copy to clipboard", value=False)
    button_generate: ElevatedButton = ElevatedButton(text="generate", width=200, disabled=True) 
    password_validator = TextField(label="password", text_align=ft.TextAlign.LEFT, width=200)
    button_validate = ElevatedButton(text="validate", width=200, disabled=True)   

    password_length = password_generator.value
    data = {
            'digits':range(10),'string':['a', 'b',"KD","JEI","NDN3", "WS","HEI", '77;', '!js', 'kk',"F", "G", "H", 
            "J", "K", "J", "G", "K", "O", "G", "F", "H", "K", "J", "Y", "F", "N", "R", "E", "W", "A", "S" 'knsuj',
            'c', 'd', '+)#j', 'skER', 'knur', 'ioe', 'f', 'hjkskkksjo', 'g', 'h', 'i', 'j', 'hejikdnhjd', 'k', 'l',
            'm', 'n', 'o', 'p', 'qbsnoku+$();', 'r', 's', 't', 'uvw', 'x', 'y', 'z'] ,
            'symbols': ['@', '!', '^', '_', '=' '#', '$', '%', '&']
            }

    def generate(param: ControlEvent) -> None:
        global password_length, selected_cases
        selected_cases = []
        password_length = int(password_generator.value) # type: ignore
        num_cases = password_length

        # Select random cases
        for _ in range(num_cases):
            key = random.choice(list(data.keys()))
            values = random.choice(data[key])
            selected_cases.append((key, values))
        for key, values in selected_cases:    
            print(f"{values}", end="")
           
            
        button_generate.disabled = not checkbox_copy.value
        page.update()
        
    def submit_generate(param: ControlEvent) -> None:       
        page.add(
            Row(
                controls=[
                    Text(value=f"password: {''.join(str(values) for key, values in selected_cases)}", size=20, disabled=False)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        def clipboard():
            text_to_copy = "".join(str(values) for key, values in selected_cases)
            if checkbox_copy.value:
                pyperclip.copy(text_to_copy)
        clipboard()
 
    checkbox_copy.on_change = generate
    password_generator.on_change = generate
    button_generate.on_click = submit_generate
    
    page.add(
        Row(
            controls=[
                Column(
                  [password_generator,
                   checkbox_copy, 
                   button_generate])
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    ) 
    
    def validate(param: ControlEvent) -> None:
        button_validate.disabled = not password_validator.value
        page.update()

    def validate_password(password_validator) -> str:
        if len(password_validator.value) <= 7:
            return "Password must be more than 7 characters"
        elif len(password_validator.value) >= 50:
            return "Password length may be too long!!"
        elif not re.search(r"[A-Z]", password_validator.value):
            return "Password must consist of uppercase"
        elif not re.search(r"[a-z]", password_validator.value):
            return "Password must consist of lowercase"
        elif not re.search(r"[0-9]", password_validator.value):
            return "Password must consist of numbers"
        elif not re.search(r"[#,@,\$,\.,/?,&,%,*,^,!,_]", password_validator.value):
            return "Password must consist of special characters"
        else:
            return "Password is strong✅"

    def submit_validate(param: ControlEvent) -> None:
        validation_message = validate_password(password_validator)
        page.add(
            Row(
                controls=[
                    Text(value=validation_message, size=20, disabled=False)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    password_validator.on_change = validate
    button_validate.on_click = submit_validate

    page.add(
        Row(
            controls=[
                Column(
                    [password_validator, button_validate])
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )



if __name__ == "__main__":
    ft.app(target=main)
    