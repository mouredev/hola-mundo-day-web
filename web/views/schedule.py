import reflex as rx
from web.components.print_text import print_text
import web.styles.styles as styles
from web.components.terminal_text import terminal_text
from web.components.event_text import event_text
from web.components.divider import divider
from web.styles.styles import Size


def schedule() -> rx.Component:
    return rx.vstack(
        terminal_text(quoted_text="Agenda"),
        divider(),
        event_text("16:00 ", "Bienvenida"),
        divider(),
        event_text(
            "16:30 ", "Charla | ¡No dejes para mañana tu código de hoy! Cómo vencer la procrastinación en programación"
        ),
        event_text("17:00 ", "Charla | UX Design"),
        event_text(
            "17:30 ", "Taller | Crea tu propio bot de Telegram con Python"),
        divider(),
        event_text("18:00 ", "Sorteos"),
        divider(),
        event_text(
            "18:30 ", "Charla | Desbloquea tu creatividad: Prompt engineering con Gemini AI y ChatGPT"
        ),
        event_text(
            "19:00 ", "Taller | Desmitificando el Testing: Aprende a probar como un profesional"
        ),
        event_text("19:30 ", "Charla | Ser autodidacta en el mundo del software"),
        divider(),
        event_text("20:00 ", "Final Hackathon"),
        divider(),
        event_text("20:30 ", "Sorteos"),
        divider(),
        event_text(
            "21:00 ", "Charla | Cómo entrar el mundo de freelance internacional: motivaciones, estrategias y retos"
        ),
        event_text(
            "21:30 ", "Taller | Open Source: Configura tu entorno para contribuir a proyectos de código abierto"
        ),
        divider(),
        event_text("22:00 ", "Sorteos"),
        divider(),
        event_text(
            "22:30 ", "Charla | Soft skills que todo programador debería tener"
        ),
        event_text("23:00 ", "Charla | ¿Qué hace que un GitHub sea \"bueno\"?"),
        divider(),
        event_text("23:30 ", "Despedida"),
        divider(),
        print_text(
            "El horario puede sufrir modificaciones. Zona horaria: CET (España)"
        ),
        rx.vstack(
            rx.text.strong("Hora de inicio por país:"),
            rx.text("16:00 | España"),
            rx.text(
                "08:00 | México, Costa Rica, El Salvador, Guatemala, Honduras, Nicaragua"
            ),
            rx.text("09:00 | Colombia, Ecuador, Panamá, Perú, Perú"),
            rx.text(
                "10:00 | Chile, Bolivia, Cuba, Puerto Rico, República Dominicana, Venezuela, Paraguay"
            ),
            rx.text("11:00 | Argentina, Uruguay"),
            spacing=Size.ZERO.value
        ),
        spacing=Size.DEFAULT.value,
        style=styles.container
    )
