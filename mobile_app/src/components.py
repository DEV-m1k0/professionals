import flet as ft
from constants import PATH


def get_label_for_news():
    return ft.Row(
            controls=[
                ft.Text(
                    value="наименование",
                    color=ft.colors.BLACK,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )


def get_footer_news():
    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Text(
                    value="some1",
                    color=ft.colors.BLACK
                ),
                ft.Text(
                    value="some2",
                    text_align=ft.alignment.bottom_right,
                    color=ft.colors.BLACK
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        margin=ft.Margin(0, 20, 0, 0),
        bgcolor=ft.colors.BLACK
    )

def get_description_for_news():
    return ft.Row(
                    controls=[
                        ft.Text(
                            value="короткое описание",
                            color=ft.colors.BLACK,
                        )
                    ]
                )

def get_news_photo():
    return ft.Row(
        controls=[
            ft.Image(src=f"{PATH}/assets/default.jpg", width=75, height=75,
                    fit=ft.ImageFit.FILL, border_radius=50),
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

def get_container_with_navigate_btns():
    btn_news = ft.FilledButton(
        text="новости",
        bgcolor=ft.colors.RED,
        color=ft.colors.BLACK,
        adaptive=True
    )
    
    btn_events = ft.FilledButton(
        text="события",
        bgcolor=ft.colors.YELLOW,
        color=ft.colors.BLACK,
        adaptive=True
    )

    return ft.Container(
        content=ft.Row(
            controls=[
                btn_news,
                btn_events,
            ],
            adaptive=True,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        adaptive=True
    )