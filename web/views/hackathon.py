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
            "Participa en la hackathon y gana 1000$ en premios (hasta el 2 de mayo).",
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
        event_text("Proyecto: ", "Desarrolla un proyecto web utilizando Reflex que cumpla un único objetivo: \"Ayudar a la comunidad de desarrollo de software\" (de la manera que se te ocurra)."),
        event_text("Requisitos: ", "El proyecto deberá tener publicado su código en GitHub y estar desplegado en una url pública, utilizando el servicio de hosting que quieras (Recuerda que Reflex posee su propio hosting con un sólo comando)."),
        event_text("Fechas: ", "Desarrollo y envío: Hasta el 2 de mayo | Votaciones por parte de la comunidad: Del 3 al 5 de mayo | Final: 7 de mayo durante el evento."),
        event_text("Final: ", "Entre los 3 proyectos más votados se realizará una votación el día del evento. Los finalistas podrán hablar en directo sobre su proyecto antes de la votación definitiva."),
        event_text("Participación: ", "Para participar deberás rellenar el siguiente formulario con todos los datos del proyecto a presentar. Podrás hacerlo hasta el 2 de mayo (incluido)."),
        button(
            constants.HACKATHON_FORM_URL,
            "Participar",
            "file-input"
        ),
        rx.text("¿Quieres aprender Reflex para participar? Tengo un curso gratis."),
        button(
            constants.REFLEX_TUTORIAL_URL,
            "Curso",
            "file-input",
            True
        ),
        spacing=Size.DEFAULT.value,
        style=styles.container
    )
