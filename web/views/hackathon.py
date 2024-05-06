import reflex as rx
from web.components.event_text import event_text
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
            "Decide los 3 proyectos ganadores durante el evento en directo.",
            True, True, Color.ACCENT
        ),
        print_text("Premios: 1º - 600$ | 2º - 300$ | 3º - 100$"),
        partner(
            "/reflex.svg",
            "https://reflex.dev",
            ""
        ),
        rx.text("Reflex es el framework web revolucionario que te permite crear aplicaciones web frontend y backend utilizando Python puro."),
        text(
            "Intrucciones:",
            True, True, Color.ACCENT
        ),
        event_text("Proyecto: ", "El objetivo de la hackathon era desarrollar un proyecto web utilizando Reflex que sirva para \"ayudar a la comunidad de desarrollo de software\"."),
        # event_text(
        #     "Votación: ", "Hasta el 5 de mayo utilizando el siguiente formulario. El día 6 se presentarán los finalistas."
        # ),
        # button(
        #     constants.HACKATHON_FORM_URL,
        #     "Votar",
        #     "file-input"
        # ),
        event_text("Final: ", "Entre los 3 proyectos más votados se realizará una votación el día del evento. Los finalistas podrán hablar en directo sobre su proyecto antes de la votación definitiva."),
        rx.text("¿Quieres aprender Reflex? Tengo un curso gratis."),
        button(
            constants.REFLEX_TUTORIAL_URL,
            "Curso",
            "file-input",
            True,
            id="networking"
        ),
        spacing=Size.DEFAULT.value,
        style=styles.container
    )
