import PySimpleGUI as sg

from static.widgets import ButtonsGenerator
from static.widgets import ColumnsGenerator

sg.theme("Black")
text = sg.Text("Calculator")

button1 = ButtonsGenerator.generate_button(button_text="1", key="1")
button2 = ButtonsGenerator.generate_button(button_text="2", key="2")
button3 = ButtonsGenerator.generate_button(button_text="3", key="3")
button4 = ButtonsGenerator.generate_button(button_text="4", key="4")
button5 = ButtonsGenerator.generate_button(button_text="5", key="5")
button6 = ButtonsGenerator.generate_button(button_text="6", key="6")
button7 = ButtonsGenerator.generate_button(button_text="7", key="7")
button8 = ButtonsGenerator.generate_button(button_text="8", key="8")
button9 = ButtonsGenerator.generate_button(button_text="9", key="9")
button0 = ButtonsGenerator.generate_button(button_text="0", key="0")

button_plus = ButtonsGenerator.generate_button(button_text="+", key="+")
button_minus = ButtonsGenerator.generate_button(button_text="-", key="-")
button_mult = ButtonsGenerator.generate_button(button_text="*", key="*")
button_div = ButtonsGenerator.generate_button(button_text="/", key="/")

button_reset = ButtonsGenerator.generate_button(button_text="R", key="reset", text_color="Red")
button_equal = ButtonsGenerator.generate_button(button_text="=", key="=",  text_color="Green")


col1 = ColumnsGenerator.generate_column(button7, button4, button1, button_reset)
col2 = ColumnsGenerator.generate_column(button8, button5, button2, button0)
col3 = ColumnsGenerator.generate_column(button9, button6, button3, button_equal)
col4 = ColumnsGenerator.generate_column(button_plus, button_minus, button_mult, button_div)

WINDOW = sg.Window("Calculator", layout=[[col1, col2, col3, col4]])
