import reflex as rx
from web.components.span import span
from web.styles.colors import Color


def print_text(text: str) -> rx.Component:
    return rx.text(
        "print(",
        span('"', Color.ACCENT),
        rx.text(
            text,
            color=Color.SECONDARY.value,
            as_="span"
        ),
        span('"', Color.ACCENT),
        ")"
    )
