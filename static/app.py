import PySimpleGUI as sg
from sympy import sympify



class Application:
    @staticmethod
    def run(window: sg.Window):
        expression = ""
        while True:
            event, value = window.read()

            match event:
                case sg.WIN_CLOSED:
                    break

                case "=":
                    try:
                        result = float(sympify(expression))
                        sg.popup(f"The result is: \n{result}", text_color="white", font=("Helvetica", 12, "bold"))
                    except TypeError:
                        sg.popup(f"The result is: \nBlack Hole", text_color="white", font=("Helvetica", 12, "bold"))

                    expression = ""
                    continue

                case "reset":
                    expression = ""
                    continue

                case _:
                    # to catch on-close None event
                    if event is not None:
                        expression += event

        window.close()
