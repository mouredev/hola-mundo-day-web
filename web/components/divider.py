import reflex as rx
from web.styles.colors import Color


def divider() -> rx.Component:
    return rx.divider(background=Color.SECONDARY.value)
