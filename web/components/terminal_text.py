import reflex as rx
from web.components.span import span
from web.styles.colors import Color
from web.styles.styles import Size, SizeEM


def terminal_text(start_text="", quoted_text="", end_text="", big=False) -> rx.Component:
    return rx.flex(
        rx.icon(
            "chevron-right",
            size=65 if big else 45,
            color=Color.SECONDARY.value,
        ),
        rx.heading(
            start_text,
            span('"'),
            quoted_text,
            span('"'),
            end_text,
            span("_", Color.SECONDARY, True),
            font_size=SizeEM.VERY_BIG.value if big else SizeEM.MEDIUM.value,
            color=Color.ACCENT.value,
            letter_spacing=".15em",
            text_shadow=f"0 0 8px {Color.ACCENT.value}",
            as_="h1" if big else "h2"
        ),
        spacing=Size.ZERO.value,
        padding_top=SizeEM.BIG.value if big else SizeEM.ZERO.value,
        flex_direction=["column", "row"],
        align_items=["start", "center"]
    )
