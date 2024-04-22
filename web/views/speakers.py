import reflex as rx
import web.styles.styles as styles
from web import constants
from web.components.button import button
from web.components.event_text import event_text
from web.components.print_text import print_text
from web.components.terminal_text import terminal_text
from web.components.text import text
from web.styles.colors import Color
from web.styles.styles import Size


def speakers() -> rx.Component:
    return rx.vstack(
        terminal_text(quoted_text="Charlas"),
        _speaker(
            "¿Qué hace que un GitHub sea \"bueno\"?",
            "Github es la red social de los programadores y nuestro portfolio de trabajo. Es la ventana a nuestra experiencia técnica y las empresas le dan mucha importancia. Por esta razón, si somos desarrolladores de software, deberíamos preguntarnos... ¿Sé cómo presentarme en Github? En esta charla aprenderás tips y sugerencias para que tu profile de Github sea llamativo, además te contaré lo que me ha ayudado a mi a mejorar mi perfil.",
            "Pablo Marino",
            "https://www.linkedin.com/in/pablomarinotech",
            "/speakers/pablo_marino.jpg"
        ),
        _speaker(
            "Ser autodidacta en el mundo del software",
            "Hablaré sobre cómo aprender a ser autodidacta y contaré mi experiencia de cómo me cambió la vida. Cómo en el mundo del desarrollo necesitas estar siempre al día y cómo un desarrollador nunca para de aprender. Además, explicaré como bonus las ventajas de usar Jetpack Compose y SwiftUI.",
            "Kevin Morales",
            "https://www.kevinhomorales.com",
            "/speakers/kevin_morales.jpg"
        ),
        _speaker(
            "Soft skills que todo programador debería tener",
            "En ocasiones, priorizamos el conocimiento técnico sobre el desarrollo de habilidades blandas. En esta charla exploraré la importancia de equilibrar ambos aspectos para el crecimiento profesional.",
            "Geraldhy Messu",
            "https://github.com/gerald-M14",
            "/speakers/geraldhy_messu.jpg"
        ),
        _speaker(
            "Cómo entrar el mundo de freelance internacional: motivaciones, estrategias y retos",
            "El freelancing es una oportunidad genial para ganar dinero desde cualquier lugar del mundo, usando tus habilidades y destrezas. Tiene sentido considerar esta opción y entender sus ventajas y desventajas, sin importar el nivel. Como Upwork Top Rated Plus, quisiera compartir mis experiencias, métodos y estrategias.",
            "Dmitry Zhukov",
            "https://www.linkedin.com/in/dmitryjima",
            "/speakers/dmitry_zhukov.jpg"
        ),
        _speaker(
            "¡No dejes para mañana tu código de hoy! Cómo vencer la procrastinación en programación",
            "Como alguien que ha superado la procrastinación en programación, estoy aquí para compartir cómo logré vencer este obstáculo. Aprendí a establecer metas claras, dividir proyectos en tareas manejables y eliminar distracciones. Con determinación y autodisciplina, logré mejorar mi productividad y calidad de trabajo. Ahora quiero ayudarte a hacer lo mismo. Juntos, podemos superar la procrastinación y alcanzar nuestro máximo potencial como desarrolladores.",
            "José Ángel Polanco",
            "https://www.instagram.com/joseangelpolanco77",
            "/speakers/jose_angel.jpg"
        ),
        _speaker(
            "Desbloquea tu creatividad: Prompt engineering con Gemini AI y ChatGPT",
            "¡Despierta tu lado creativo! Aprende a usar Prompt Engineering con Gemini AI y ChatGPT para generar textos increíbles y soluciones creativas para tus proyectos, desde recomendaciones en Markdown hasta estructuras de tú código optimizadas.",
            "Juliana Castillo",
            "https://www.linkedin.com/in/julianacastilloaraujo",
            "/speakers/juliana_castillo.jpg"
        ),
        _speaker(
            "UX Design",
            "Explora las claves del diseño de experiencia de usuario para crear productos que no solo satisfagan, sino que deleiten. Descubre cómo la empatía y la innovación se unen para transformar la interacción usuario-producto.",
            "Angela Martínez",
            "https://www.linkedin.com/in/amfprogramacion/",
            "/speakers/angela_martinez.jpg"
        ),

        terminal_text(quoted_text="Talleres"),
        _speaker(
            "Open Source: Configura tu editor, consola y entorno para contribuir a proyectos de código abierto",
            "Taller práctico donde te explicarán paso a paso cómo configurar tu entorno de desarrollo para contribuir a proyectos de código abierto, repasando comandos útiles, configuración de SSH, personalización del editor (Visual Studio Code), etc. Como ejemplo práctico, configuraremos un repo desde cero para contribuir al roadmap de la comunidad.",
            "Jamer José",
            "https://jamerrq.deno.dev",
            "/speakers/jamer_jose.jpg"
        ),
        _speaker(
            "Crea tu propio bot de Telegram con Python",
            "Descubre cómo crear un bot de Telegram utilizando la biblioteca Telebot de Python. Explorarás la interacción con la API de Telegram y aprenderás a configurar respuestas automáticas a los mensajes.",
            "Karoll Escalante",
            "https://www.linkedin.com/in/karollescalanteg",
            "/speakers/karoll_escalante.jpg"
        ),
        _speaker(
            "Desmitificando el Testing: Aprende a probar como un profesional",
            "¿Te apasiona el mundo del software y quieres aprender a probar como un profesional? En este taller práctico te guiaré a través de los fundamentos del testing de software, desde los conceptos básicos hasta las técnicas más avanzadas.",
            "María Morán",
            "https://twitter.com/_mariamoraan",
            "/speakers/maria_moran.jpg"
        ),
        text(
            "NO se han admitido propuestas de personas con experiencia como ponentes.",
            True, True, Color.ACCENT
        ),
        rx.text("En el \"Hola Mundo\" day la comunidad es la protagonista. No hace falta que tengas años de experiencia en el sector o te dediques profesionalmente a dar ponencias. Aquí no hay limitaciones. No importa si has comenzado a estudiar o llevas programando desde hace décadas."),
        rx.text("Por suerte, este tipo de eventos están llenos de referentes conocidos por un gran número de personas, pero en este caso no será así. Cualquier persona puede compartir conocimientos de gran valor."),
        event_text("Charla: ", "Una ponencia relacionada con el mundo de la programación o el desarrollo de sofware que esté dirigida a todos los niveles. Que sirva para enseñar o motivar."),
        event_text("Taller: ", "Un espacio dedicado a aprender sobre programación y desarrollo de software. Debe ser generalista y comprensible por personas que estén empezando."),
        print_text("Su duración debe ser de entre 15/20 minutos, con una ronda de preguntas de 5 minutos. La comunidad será la encargara de votar las propuestas seleccionadas (7 charlas y 3 talleres). Cada charla y taller será remunerado con 100$."),
        rx.flex(
            # button(
            #     constants.VOTE_FORM_URL,
            #     "Votar",
            #     "file-input"
            # ),
            button(
                "https://www.youtube.com/playlist?list=PLNdFk2_brsRdi01BE_sWyQ8e9FBmdrxGz",
                "Ver edición 2023",
                "youtube",
                True,
                id="hackathon"
            ),
            spacing=Size.DEFAULT.value,
            flex_direction=["column", "row"]
        ),
        spacing=Size.DEFAULT.value,
        style=styles.container
    )


def _speaker(title: str, body: str, author: str, url: str, avatar: str) -> rx.Component:
    return rx.flex(
        rx.image(
            src=avatar,
            width="180px",
            height="180px",
            border_radius="10px"
        ),
        rx.vstack(
            event_text(
                title,
                big=True
            ),
            rx.text(body),
            rx.link(
                f"- {author}",
                href=url,
                is_external=True
            ),
            rx.divider()
        ),
        spacing=Size.DEFAULT.value,
        flex_direction=["column-reverse", "row"]
    )
