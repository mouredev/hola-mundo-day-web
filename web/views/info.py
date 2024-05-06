import reflex as rx
from web.components.button import button
import web.styles.styles as styles
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
                "Accede al networking con la comunidad previo al evento.",
                big=True,
                color=Color.BACKGROUND
            ),
            button(
                "./#networking",
                "Networking",
                icon="file-input",
                is_external=False
            ),
            spacing=Size.SMALL.value,
            padding_y=SizeEM.MEDIUM.value,
            style=styles.container
        ),
        width="100%",
        background=Color.ACCENT.value
    )
