import reflex as rx
from web.styles.colors import Color


def event_text(title: str, body="") -> rx.Component:
    return rx.text(
        rx.icon(
            "terminal",
            color=Color.SECONDARY.value,
            display="inline"
        ),
        rx.text.strong(title),
        body,
        as_="span"
    )
