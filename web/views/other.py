import reflex as rx
import web.styles.styles as styles
from web.components.print_text import print_text
from web.components.terminal_text import terminal_text
from web.styles.styles import Size


def other() -> rx.Component:
    return rx.vstack(
        terminal_text(quoted_text="Hackathon, Networking, Sorteos, Agenda..."),
        print_text("Próximamente..."),
        spacing=Size.DEFAULT.value,
        style=styles.container
    )
