import reflex as rx
from web import constants
from web.components.button import button
from web.styles.colors import Color
from web.styles.styles import Size, SizeEM


def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.link(
                rx.icon(
                    "terminal",
                    size=32,
                    color=Color.ACCENT.value
                ),
                href="/",
                is_external=False
            ),
            rx.spacer(),
            button(
                "./#speakers",
                "Vota",
                icon="file-input",
                is_external=False
            ),
            button(constants.TWITCH_URL, icon="twitch"),
            spacing=Size.DEFAULT.value,
            padding=SizeEM.DEFAULT.value,
            width="100%",
            align="center"
        ),
        rx.divider(background=Color.SECONDARY.value),
        spacing=Size.ZERO.value,
        position="sticky",
        bg=Color.BACKGROUND.value,
        z_index="10",
        top="0"
    )
