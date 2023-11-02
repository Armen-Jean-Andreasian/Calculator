import PySimpleGUI
import PySimpleGUI as sg


class ButtonsGenerator:
    button_style = {"color": ('Black', 'AliceBlue'),
                    "size": (6, 3),
                    "font": ("Helvetica", 11, "bold"),
                    "relief": sg.RELIEF_RIDGE}



    @classmethod
    def generate_button(cls, button_text, key, text_color=None):

        button_color_ = (text_color, 'AliceBlue') if text_color else cls.button_style["color"]

        button = sg.Button(
            button_text=button_text, button_color=button_color_, size=cls.button_style["size"],
            font=cls.button_style["font"], key=key)

        return button


class ColumnsGenerator:
    @classmethod
    def generate_column(cls, *buttons: PySimpleGUI.Button):
        column_layout = [[button] for button in buttons]
        column = sg.Column(column_layout)
        return column
