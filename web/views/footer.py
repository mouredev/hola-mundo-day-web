from os import link
import reflex as rx
from web import constants
import web.styles.styles as styles
from web.components.text import text
from web.styles.colors import Color
from web.styles.styles import Size, SizeEM


def footer() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.icon("terminal"),
                rx.link(
                    rx.hstack(
                        rx.text.strong("Hola mundo day 2024 v2"),
                        rx.icon("github")
                    ),
                    href=constants.REPO_URL,
                    is_external=True
                )
            ),
            rx.text(
                "Organizado con ♥ (y gracias a ti) por ",
                rx.link(
                    "@mouredev",
                    href=constants.MOUREDEV_URL,
                    is_external=True
                ),
                align="right"
            ),
            padding_y=SizeEM.MEDIUM.value,
            spacing=Size.SMALL.value,
            style=styles.container,
            align="end"
        ),
        width="100%"
    )
