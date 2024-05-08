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
        # text(
        #     "Decide los 3 proyectos ganadores durante el evento en directo.",
        #     True, True, Color.ACCENT
        # ),
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
        # button(
        #     constants.HACKATHON_FORM_URL,
        #     "Votar",
        #     "file-input"
        # ),
        # event_text("Final: ", "Entre los 3 proyectos más votados se realizará una votación el día del evento. Los finalistas podrán hablar en directo sobre su proyecto antes de la votación definitiva."),
        text(
            "Proyectos presentados:",
            True, True, Color.ACCENT
        ),
        rx.vstack(
            _project(
                "WebWizard ",
                "Carlos Abadía",
                "https://webwizard.reflex.run",
                "https://github.com/carlosabadia/webwizard",
                True
            ),
            _project(
                "Codex me ",
                "Giovanny Kelly",
                "https://codexme.reflex.run",
                "https://github.com/Gioak1993/CodeXme",
                True
            ),
            _project(
                "Fonts Web ",
                "Nicolas Vargas",
                "https://fontsweb.online",
                "https://github.com/uprizingFaze/fontsweb",
                True
            ),
            _project(
                "Recursos-IT",
                "Ricardo",
                "https://recursosit.reflex.run",
                "https://github.com/Rikmij/RecursosIT-ReflexHacktaton"
            ),
            _project(
                "Comandos de linux",
                "Sergio Ruiz",
                "https://comandos-de-linux.reflex.run",
                "https://github.com/pyramsd/Pagina-de-documentacion-comandos-linux"
            ),
            _project(
                "ReflexLlama",
                "Johan Manuel Grisales",
                "http://elsoaverso.com:3000",
                "https://github.com/johanmanuelle/reflexLlama"
            ),
            _project(
                "AGTool",
                "Brahian Arias",
                "https://agtool.reflex.run",
                "https://github.com/aquelaronte/aquelaronte_git_tool"
            ),
            _project(
                "VSCode Gallery",
                "Alberto",
                "https://vscodegallery.reflex.run",
                "https://github.com/AlbertoAIG/vscode_gallery"
            ),
            _project(
                "DevForum",
                "Javier Gonzalez",
                "https://devforum-production.up.railway.app",
                "https://github.com/JavierGonzalez998/DevForum"
            ),
            _project(
                "MagicMP3web",
                "Jonathan B.V",
                "https://magic-mp3-rx.reflex.run",
                "https://github.com/MagoOscuro91/Magic_MP3_web"
            ),
            _project(
                "Lector de documentos",
                "Andres Perez",
                "https://pyrumind.reflex.run",
                "https://github.com/andreselcientifico/PDF-TRANSLATE-WEB"
            ),
            _project(
                "Docflow",
                "Miguel Cárdenas",
                "https://docflow.reflex.run",
                "https://github.com/miguelcsx/docflow"
            ),
            _project(
                "resources4dev",
                "Ylenia Díaz",
                "https://resource4dev.reflex.run",
                "https://github.com/YleniaDiaz/hackathon-moure-dev"
            ),
            _project(
                "Componentes predefinidos",
                "Eric",
                "https://predefined-components-ericcode29.reflex.run",
                "https://github.com/ericcode29/hackaton_mouredev"
            ),
            _project(
                "My portafolio",
                "Daniel Santiago Angel",
                "https://danidev.reflex.run",
                "https://github.com/DANIElPEZ/My-web"
            ),
        ),
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


def _project(name: str, author: str, url: str, github: str, winner=False) -> rx.Component:
    return rx.hstack(
        button(url, icon="link", secondary=True),
        button(github, icon="github", secondary=True),
        event_text(f"{name} ", author),
        rx.cond(
            winner,
            rx.icon("award")
        ),
        align="center"
    )
