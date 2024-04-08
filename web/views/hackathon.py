import reflex as rx
from web.components.partner import partner
import web.styles.styles as styles
from web import constants
from web.components.terminal_text import terminal_text
from web.components.text import text
from web.components.button import button
from web.components.print_text import print_text
from web.styles.colors import Color
from web.styles.styles import Size


def hackathon() -> rx.Component:
    return rx.vstack(
        terminal_text(quoted_text="Hackathon"),
        text(
            "Participa en la hackathon de Reflex y gana 1000$.",
            True, True, Color.ACCENT
        ),
        partner(
            "/reflex.svg",
            "https://reflex.dev",
            ""
        ),
        rx.text("Reflex es el framework web revolucionario que te permite crear aplicaciones web frontend y backend utilizando Python puro."),
        print_text("La hackathon se celebrará del 22 de abril al 5 de mayo. Toda la información y requisitos de participación se publicarán en esta sección de la web."),
        rx.text("¿Quieres aprender Reflex para participar? Tengo un curso gratis."),
        button(
            constants.REFLEX_TUTORIAL_URL,
            "Curso",
            "file-input"
        ),
        spacing=Size.DEFAULT.value,
        style=styles.container
    )
