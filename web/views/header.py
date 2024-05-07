import reflex as rx
import web.styles.styles as styles
from web import constants
from web.components.button import button
from web.components.span import span
from web.components.terminal_text import terminal_text
from web.components.ticket import ticket
from web.styles.colors import Color
from web.styles.styles import Size, SizeEM


def header() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.hstack(
                    _window_icon(),
                    _window_icon(),
                    _window_icon(),
                    rx.box(
                        rx.text(
                            "Segunda edición",
                            size=Size.SMALL.value,
                            color=Color.PRIMARY.value,
                            background=Color.BACKGROUND.value,
                            border_color=Color.BACKGROUND.value,
                            padding_x=SizeEM.MEDIUM.value,
                            padding_y=SizeEM.DEFAULT.value,
                            border_radius=f"{SizeEM.DEFAULT.value} {SizeEM.DEFAULT.value} 0 0"
                        ),
                        padding_left=SizeEM.DEFAULT.value
                    ),
                    padding_left=SizeEM.DEFAULT.value,
                    align="center",
                    height="100%"
                ),
                background=Color.SECONDARY.value,
                position="absolute",
                top=SizeEM.ZERO.value,
                height=SizeEM.BIG.value,
                width="100%"
            ),
            terminal_text(quoted_text="Hola Mundo", end_text=" day", big=True),
            rx.heading(
                span("print(", Color.SECONDARY),
                span('"', Color.ACCENT),
                "La conferencia de programación creada por y para la comunidad",
                span('"', Color.ACCENT),
                span(")", Color.SECONDARY),
                as_="h2"
            ),
            rx.heading("Día 128 | 7 de mayo | 16:00 CET", as_="h3"),
            ticket(),
            rx.flex(
                button(
                    constants.TWITCH_URL,
                    "twitch.tv/mouredev",
                    "twitch"
                ),
                button(
                    constants.EVENT_URL,
                    "Crear recordatorio",
                    "discord"
                ),
                flex_direction=["column", "row"],
                spacing=Size.DEFAULT.value
            ),
            rx.link(
                rx.hstack(
                    rx.icon(
                        "radio",
                        size=32,
                        color="crimson"
                    ),
                    rx.heading(
                        id="countdown",
                        color=Color.PRIMARY.value
                    ),
                    spacing=Size.SMALL.value,
                    align="center"
                ),
                href=constants.TWITCH_URL,
                is_external=True
            ),
            rx.link(
                "#HolaMundoDay",
                href="https://twitter.com/hashtag/HolaMundoDay",
                is_external=True
            ),
            rx.script(src="/js/countdown.js"),
            position="relative",
            align="center",
            spacing=Size.DEFAULT.value,
            padding_x=SizeEM.DEFAULT.value,
            padding_y=SizeEM.VERY_BIG.value,
            border=f"{SizeEM.SMALL.value} solid {Color.SECONDARY.value}",
            border_radius=SizeEM.DEFAULT.value
        ),
        style=styles.container
    )


def _window_icon() -> rx.Component:
    return rx.icon(
        "circle",
        color=Color.BACKGROUND.value
    )
