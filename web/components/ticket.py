import reflex as rx
from web import constants
from web.components.text import text
from web.styles.colors import Color
from web.styles.styles import Size, SizeEM


def ticket() -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.icon(
                "ticket",
                size=64,
                stroke_width=1,
                color=Color.BACKGROUND.value
            ),
            rx.vstack(
                rx.hstack(
                    rx.icon(
                        "terminal",
                        size=32,
                        color=Color.BACKGROUND.value
                    ),
                    text(
                        "Consigue tu entrada gratis",
                        True,
                        True,
                        Color.BACKGROUND
                    ),
                    spacing=Size.SMALL.value
                ),
                text(
                    "(Y compártela en redes)",
                    color=Color.BACKGROUND
                ),
                align="center",
                spacing=Size.ZERO.value
            ),
            class_name="ticket",
            align="center",
            spacing=Size.SMALL.value,
            padding=SizeEM.MEDIUM.value,
            background=Color.ACCENT.value
        ),
        href=constants.TICKETS_URL,
        is_external=True
    )
