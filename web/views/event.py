import reflex as rx
from web import constants
from web.components.button import button
from web.components.event_text import event_text
import web.styles.styles as styles
from web.styles.colors import Color
from web.components.terminal_text import terminal_text
from web.components.text import text
from web.styles.styles import Size


def event() -> rx.Component:
    return rx.vstack(
        terminal_text("¿Qué es el ", "Hola Mundo", " day?"),
        text("Es una conferencia tecnológica sobre programación y desarrollo de software 100% online, gratis, para todos los niveles y donde la comunidad será la verdadera protagonista, ya que se encargará de llevar a cabo los diferentes eventos del día."),
        text("¡Te esperamos el día 128 del año!", True, True, Color.ACCENT),
        rx.flex(
            event_text("Charlas"),
            event_text("Talleres"),
            event_text("Networking"),
            event_text("Mesa redonda"),
            event_text("Sorteos"),
            event_text("Sorpresas"),
            spacing=Size.SMALL.value,
            flex_direction=["column", "row"],
            justify="between",
            width="100%"
        ),
        rx.flex(
            button(
                "https://twitter.com/intent/tweet?text=Ven%20al%20%23HolaMundoDay,%20la%20conferencia%20de%20programaci%C3%B3n%20y%20desarrollo%20de%20software%20creada%20por%20y%20para%20la%20comunidad.%0A%0A7%20de%20Mayo%20%7C%20Twitch%20%7C%20Gratis%20y%20para%20todos%20los%20niveles.%0A%0AÚnete%20al%20holamundo.day%20organizado%20por%20@mouredev",
                "Compártelo en X",
                "x"
            ),
            button(
                constants.NEWSLETTER_URL,
                "Suscríbete a la newsletter",
                "mail",
                True
            ),
            flex_direction=["column", "row"],
            spacing=Size.DEFAULT.value
        ),
        spacing=Size.DEFAULT.value,
        style=styles.container
    )
