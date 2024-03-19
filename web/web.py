import reflex as rx
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
    style=BASE_STYLE
)
app.add_page(index)
