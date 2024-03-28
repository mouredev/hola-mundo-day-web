import reflex as rx
from web.styles.colors import Color
import web.styles.styles as styles
from web import constants
from web.components.button import button
from web.components.print_text import print_text
from web.components.span import span
from web.components.terminal_text import terminal_text
from web.styles.styles import Size, SizeEM


def partners() -> rx.Component:
    return rx.vstack(
        terminal_text(quoted_text="Patrocinado", end_text=" por"),
        rx.flex(
            _partner(
                "/partners/raiola.png",
                "https://mouredev.com/raiola",
                "20% en hosting"
            ),
            _partner(
                "/partners/nuwe.png",
                "https://bit.ly/JobOffersNUWE",
                "Aplica a vacantes Tech"
            ),
            _partner(
                "/partners/elgato.png",
                "https://elgato.sjv.io/mouredev",
                "5% código ZZ-MOUREDEV"
            ),
            spacing=Size.SMALL.value,
            wrap="wrap"
        ),
        rx.spacer(),
        rx.text("¿Quieres patrocinar el evento? ¡NO TENGO PALABRAS!"),
        rx.text(
            "Puedes escribirme a ",
            rx.link(
                "braismoure@mouredev.com",
                href="mailto:braismoure@mouredev.com",
                is_external=True
            ),
            " o contactarme a través de mis redes sociales como ",
            rx.link(
                "@mouredev",
                href=constants.MOUREDEV_URL,
                is_external=True
            ),
            "."
        ),
        print_text("El patrocinio servirá para pagar los participantes, realizar sorteos y cubrir los gastos de la organización. También se realizarán menciones y aparecerás destacado en todas las comunicaciones relacionadas con el evento."),
        button(
            constants.COFFEE_URL,
            "Colabora con un café",
            "coffee",
            True,
            id="speakers"
        ),
        spacing=Size.DEFAULT.value,
        style=styles.container
    )


def _partner(image: str, url: str, text: str) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.image(
                src=image,
                height="80px",
                width="auto",
                padding_right=SizeEM.MEDIUM.value
            ),
            rx.text(
                text,
                size=Size.SMALL.value,
                color=Color.PRIMARY.value
            ),
            spacing=Size.ZERO.value
        ),
        href=url,
        is_external=True
    )
