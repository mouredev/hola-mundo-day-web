import reflex as rx
import web.styles.styles as styles
from web.components.event_text import event_text
from web.components.print_text import print_text
from web.components.terminal_text import terminal_text
from web.styles.styles import Size


def raffle() -> rx.Component:
    return rx.vstack(
        terminal_text(quoted_text="Sorteos"),
        rx.text("Durante el evento se realizarán diferentes sorteos entre toda la comunidad que asista al directo."),
        event_text("x5 Becas de 6 meses para estudiar en Platzi"),
        event_text("x1 Hosting anual + Dominio en Raiola Networks"),
        event_text("x1 Steam Deck Mobile de Elgato"),
        event_text("x10 Libros Git y GitHub desde cero de MoureDev"),
        event_text(
            "x5 Pack de libros Aprender a Programar despues de los 40 de Gerardo Arrieta"
        ),
        event_text("x2 Libros Ultimate Python de Nicolás Schürmann"),
        event_text("x2 Libros Aprendiendo React de Carlos Azaustre"),
        event_text("x2 Libros Aprendiendo C# de Héctor de León"),
        event_text("x2 Libros No todo es programar de Kiko Palomares"),
        event_text("x3 Libros Patrones de diseño de Refactoring Guru"),
        spacing=Size.DEFAULT.value,
        style=styles.container
    )
