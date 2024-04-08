import reflex as rx
from web.styles.styles import Size, SizeEM, Color


def partner(image: str, url: str, text: str) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.image(
                src=image,
                height="80px",
                width="auto",
                padding_right=SizeEM.MEDIUM.value
            ),
            rx.text(
                text,
                size=Size.SMALL.value,
                color=Color.PRIMARY.value
            ),
            spacing=Size.ZERO.value
        ),
        href=url,
        is_external=True
    )
