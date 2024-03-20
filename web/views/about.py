import reflex as rx
import web.styles.styles as styles
from web import constants
from web.components.button import button
from web.components.terminal_text import terminal_text
from web.styles.styles import Size


def about() -> rx.Component:
    return rx.flex(
        rx.vstack(
            terminal_text("Hola mundo, soy ", "Brais Moure"),
            rx.text("Me dedico al desarrollo de software desde 2010."),
            rx.text("En 2018 comencé a divulgar contenido sobre programación en redes sociales como @mouredev, descubriendo el mayor superpoder del sector: una comunidad que ni descansa ni cesa en su labor de compartir conocimiento y ayudar día a día. Los verdaderos protagonistas de este \"Hola Mundo\" day."),
            rx.hstack(
                button(constants.MOUREDEV_URL, icon="link"),
                button(constants.TWITCH_URL, icon="twitch", secondary=True),
                button(constants.YOUTUBE_URL, icon="youtube", secondary=True),
                button(constants.DISCORD_URL, icon="discord", secondary=True),
                spacing=Size.DEFAULT.value
            ),
            spacing=Size.DEFAULT.value
        ),
        rx.image(
            src="/mouredev_glitch.gif",
            width="220px",
            height="220px"
        ),
        flex_direction=["column", "row"],
        spacing=Size.DEFAULT.value,
        style=styles.container
    )
