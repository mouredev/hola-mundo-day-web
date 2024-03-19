import reflex as rx
from enum import Enum
from web.styles.colors import Color
from web.styles.fonts import FontWeight


MAX_WIDTH = "1200px"
FONT_FAMILY = "\"Fira Code\", monospace"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&display=swap",
    "/css/styles.css"
]


class SizeEM(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    DEFAULT = "1em"
    MEDIUM = "2em"
    BIG = "3em"
    VERY_BIG = "4em"


class Size(Enum):
    ZERO = "0"
    SMALL = "2"
    DEFAULT = "4"
    MEDIUM = "5"
    VERY_BIG = "9"


BASE_STYLE = {
    "font_family": FONT_FAMILY,
    "font_weight": FontWeight.DEFAULT.value,
    "color": Color.PRIMARY.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading: {
        "font_family": FONT_FAMILY,
        "font_weight": FontWeight.BOLD.value,
        "line_height": "normal"
    },
    rx.text.strong: {
        "font_family": FONT_FAMILY,
    },
    rx.button: {
        "font_weight": FontWeight.MEDIUM.value,
        "cursor": "pointer",
        "_hover": {
            "background": f"{Color.PRIMARY.value}"
        }
    },
    rx.link: {
        "color": Color.ACCENT.value,
        "_hover": {
            "color": f"{Color.PRIMARY.value}"
        }
    }
}

container = dict(
    padding_x=SizeEM.DEFAULT.value,
    width="100%",
    max_width=MAX_WIDTH
)
