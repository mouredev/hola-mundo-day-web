import reflex as rx
from web.styles.colors import Color
from web.styles.styles import Size


def text(text: str, bold=False, big=False, color=Color.PRIMARY) -> rx.Component:
    return rx.text(
        text,
        font_weight="bold" if bold else "normal",
        color=color.value,
        size=Size.MEDIUM.value if big else Size.DEFAULT.value
    )
