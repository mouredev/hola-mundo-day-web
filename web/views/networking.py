import web.styles.styles as styles
import reflex as rx
from web.styles.colors import Color
from web import constants
from web.components.text import text
from web.components.button import button
from web.components.print_text import print_text
from web.components.terminal_text import terminal_text
from web.styles.styles import Size


def networking() -> rx.Component:
    return rx.vstack(
        terminal_text(quoted_text="Networking"),
        text(
            "¡El networking ya está abierto!",
            True, True, Color.ACCENT
        ),
        rx.text("Durante las 24 horas anteriores al evento, podrás acceder a salas de chat en Discord para conocer a la comunidad y charlar sobre lo que quieras."),
        print_text("¡Anímate a descubrir el poder de la comunidad!"),
        button(
            constants.DISCORD_URL,
            "Salas de networking",
            "discord"
        ),
        spacing=Size.DEFAULT.value,
        style=styles.container
    )
