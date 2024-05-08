import reflex as rx
import web.styles.styles as styles
from web import constants
from web.components.button import button
from web.components.text import text
from web.styles.colors import Color
from web.styles.styles import Size, SizeEM


def info() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.icon(
                    "terminal",
                    size=32,
                    color=Color.BACKGROUND.value
                ),
                text(
                    "Últimas noticias:",
                    True,
                    True,
                    Color.BACKGROUND
                ),
                spacing=Size.SMALL.value
            ),
            text(
                "¡Nos vemos en el Hola Mundo day 2025!",
                big=True,
                color=Color.BACKGROUND
            ),
            # button(
            #     constants.TWITCH_URL,
            #     "En directo",
            #     icon="radio",
            #     is_external=True
            # ),
            spacing=Size.SMALL.value,
            padding_y=SizeEM.MEDIUM.value,
            style=styles.container
        ),
        width="100%",
        background=Color.ACCENT.value
    )
