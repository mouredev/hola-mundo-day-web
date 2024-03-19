import reflex as rx
import web.constants as constants
from web.components.navbar import navbar
from web.styles.colors import Color
from web.styles.styles import BASE_STYLE, STYLESHEETS, Size, SizeEM
from web.views.about import about
from web.views.event import event
from web.views.footer import footer
from web.views.header import header
from web.views.info import info
from web.views.other import other
from web.views.partners import partners
from web.views.speakers import speakers


def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                info(),
                event(),
                _divider(),
                partners(),
                _divider(),
                speakers(),
                _divider(),
                other(),
                _divider(),
                about(),
                spacing=Size.VERY_BIG.value,
                align="center",
                width="100%"
            ),
            padding_top=SizeEM.DEFAULT.value,
            padding_bottom=SizeEM.VERY_BIG.value
        ),
        _divider(),
        footer(),
    )


def _divider() -> rx.Component:
    return rx.divider(background=Color.SECONDARY.value)


app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    head_components=[
        rx.script(
            src=f"https://www.googletagmanager.com/gtag/js?id={constants.GOOGLE_ANALYTICS_TAG}"
        ),
        rx.script(
            f"""
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', '{constants.GOOGLE_ANALYTICS_TAG}');
"""
        ),
    ],
)

title = "\"Hola Mundo\" day | 7 de mayo | La conferencia de programación de la comunidad para la comunidad"
description = "Conferencia tecnológica sobre programación y desarrollo de software 100% online, gratis, para todos los niveles y donde la comunidad será la verdadera protagonista, ya que se encargará de llevar a cabo los diferentes eventos del día. Charlas, talleres, networking, sorteos y más..."
preview = "https://holamundo.day/preview.jpg"

app.add_page(
    index,
    title=title,
    description=description,
    image=preview,
    meta=[
        {"name": "og:type", "content": "website"},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@mouredev"},
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": preview}
    ]
)
