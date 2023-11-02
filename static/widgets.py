import PySimpleGUI
import PySimpleGUI as sg


class ButtonsGenerator:
    __button_style = {"color": ('Black', 'LightGray'),
                      "size": (6, 3),
                      "font": ("Helvetica", 11, "bold"),
                      "relief": sg.RELIEF_RIDGE}

    @classmethod
    def generate_button(cls, button_text, key, text_color=None) -> sg.Button:
        """Generates and returns a PySimpleGUI button according to given params"""
        button_color_ = (text_color, 'AliceBlue') if text_color else cls.__button_style["color"]

        button = sg.Button(
            button_text=button_text, button_color=button_color_,
            size=cls.__button_style["size"], font=cls.__button_style["font"], key=key)

        return button


class ColumnsGenerator:
    @classmethod
    def generate_column(cls, *buttons: PySimpleGUI.Button) -> sg.Column:
        """Packs and returns a PySimpleGUI column """
        column_layout = [[button] for button in buttons]
        column = sg.Column(column_layout)
        return column
