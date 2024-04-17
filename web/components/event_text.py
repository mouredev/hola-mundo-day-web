import reflex as rx
from web.styles.colors import Color
from web.styles.styles import Size


def event_text(title: str, body="", big=False) -> rx.Component:
    return rx.text(
        rx.icon(
            "terminal",
            color=Color.SECONDARY.value,
            display="inline"
        ),
        rx.text.strong(
            title
        ),
        body,
        as_="span",
        size=Size.MEDIUM.value if big else Size.DEFAULT.value
    )
