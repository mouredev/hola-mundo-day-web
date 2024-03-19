import reflex as rx
from web import constants
from web.components.button import button
from web.components.print_text import print_text
from web.components.span import span
import web.styles.styles as styles
from web.styles.colors import Color
from web.components.terminal_text import terminal_text
from web.styles.styles import Size


def partners() -> rx.Component:
    return rx.vstack(
        terminal_text(quoted_text="Patrocinado", end_text=" por"),
        rx.text("¿Quieres patrocinar el evento? ¡NO TENGO PALABRAS!"),
        rx.text(
            "Puedes escribirme a ",
            rx.link(
                "braismoure@mouredev.com",
                href="mailto:braismoure@mouredev.com",
                is_external=True
            ),
            " o contactarme a través de mis redes sociales como ",
            rx.link(
                "@mouredev",
                href=constants.MOUREDEV_URL,
                is_external=True
            ),
            "."
        ),
        print_text("El patrocinio servirá para pagar los participantes, realizar sorteos y cubrir los gastos de la organización. También se realizarán menciones y aparecerás destacado en todas las comunicaciones relacionadas con el evento."),
        button(
            constants.COFFEE_URL,
            "Colabora con un café",
            "coffee",
            True
        ),
        spacing=Size.DEFAULT.value,
        style=styles.container
    )
