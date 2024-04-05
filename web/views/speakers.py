import reflex as rx
import web.styles.styles as styles
from web import constants
from web.components.button import button
from web.components.event_text import event_text
from web.components.print_text import print_text
from web.styles.colors import Color
from web.components.terminal_text import terminal_text
from web.components.text import text
from web.styles.styles import Size


def speakers() -> rx.Component:
    return rx.vstack(
        terminal_text(quoted_text="Charlas y talleres"),
        text(
            "NO se han admitido propuestas de personas con experiencia como ponentes.",
            True, True, Color.ACCENT
        ),
        rx.text("En el \"Hola Mundo\" day la comunidad es la protagonista. No hace falta que tengas años de experiencia en el sector o te dediques profesionalmente a dar ponencias. Aquí no hay limitaciones. No importa si has comenzado a estudiar o llevas programando desde hace décadas."),
        rx.text("Por suerte, este tipo de eventos están llenos de referentes conocidos por un gran número de personas, pero en este caso no será así. Cualquier persona puede compartir conocimientos de gran valor."),
        text(
            "El lunes 8 de abril podrás comenzar a votar tus charlas o talleres favoritos:",
            True, True, Color.ACCENT
        ),
        rx.flex(
            # button(
            #     constants.TALK_FORM_URL,
            #     "Charla",
            #     "file-input"
            # ),
            # button(
            #     constants.WORKSHOP_FORM_URL,
            #     "Taller",
            #     "file-code-2"
            # ),
            button(
                "https://www.youtube.com/playlist?list=PLNdFk2_brsRdi01BE_sWyQ8e9FBmdrxGz",
                "Ver edición 2023",
                "youtube",
                True
            ),
            spacing=Size.DEFAULT.value,
            flex_direction=["column", "row"]
        ),
        event_text("Charla: ", "Una ponencia relacionada con el mundo de la programación o el desarrollo de sofware que esté dirigida a todos los niveles. Que sirva para enseñar o motivar."),
        event_text("Taller: ", "Un espacio dedicado a aprender sobre programación y desarrollo de software. Debe ser generalista y comprensible por personas que estén empezando."),
        print_text("Su duración debe ser de entre 15/20 minutos, con una ronda de preguntas de 5 minutos. La comunidad será la encargara de votar las propuestas seleccionadas (5 charlas y 3 talleres). Cada charla y taller será remunerado con 100$."),
        spacing=Size.DEFAULT.value,
        style=styles.container
    )
