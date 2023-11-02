import PySimpleGUI as sg
from sympy import sympify


class Application:
    @staticmethod
    def run(window: sg.Window) -> None:
        """ Run the application. """
        expression = ""

        def reset_expression() -> None:
            """ Resets the user input """
            nonlocal expression
            expression = ""

        def update_display() -> None:
            """ Update the displaying value """
            nonlocal window
            window['result'].update(expression)

        while True:
            event, value = window.read()
            if not expression and (event == "/" or event == "*"):
                expression = "0"

            match event:
                case sg.WIN_CLOSED:
                    break

                case "=":
                    try:
                        result = float(sympify(expression))
                        window['result'].update(f"{result}")
                        reset_expression()
                    except TypeError:
                        window['result'].update(f"Black Hole")
                        reset_expression()
                    except Exception:
                        reset_expression()
                        continue

                case "reset":
                    reset_expression()
                    update_display()
                    continue

                case _:
                    # to catch on-close None event
                    if event is not None:
                        expression += event
                        window['result'].update(expression)
                    else:
                        expression = ""

        window.close()
