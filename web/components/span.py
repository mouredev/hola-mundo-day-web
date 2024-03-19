import reflex as rx
from web.styles.colors import Color


def span(text: str, color=Color.PRIMARY, blink=False) -> rx.Component:
    return rx.text(
        text,
        as_="span",
        color=color.value,
        text_shadow="none",
        class_name="blink" if blink else "none"
    )
