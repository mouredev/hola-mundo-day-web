import reflex as rx
import web.styles.styles as styles
from web.components.event_text import event_text
from web.components.print_text import print_text
from web.components.terminal_text import terminal_text
from web.styles.styles import Size


def raffle() -> rx.Component:
    return rx.vstack(
        terminal_text(quoted_text="Sorteos"),
        rx.text("Durante el evento se realizarán diferentes sorteos entre toda la comunidad que asista al directo y participe en redes."),
        event_text("Becas de 6 meses para estudiar en Platzi"),
        event_text("Hosting anual + Dominio en Raiola Networks"),
        event_text("Libros y cursos"),
        print_text("Estos sólo son algunos de los regalos..."),
        spacing=Size.DEFAULT.value,
        style=styles.container
    )
