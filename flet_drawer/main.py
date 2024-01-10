from flet import *


def main(page: Page):
    page.padding = 0
    page.spacing = 0

    def hidenav(e):
        pass

    def shownav(e):
        pass

    layer = Container(
        width=page.window_width,
        height=page.window_height,
        on_click=lambda e:hidenav
        content = Column([
            Container(
                bgcolor="blue",
                content=Row([
                    IconButton(
                        icon="menu",
                        icon_color="white",
                        on_click=shownav
                    ), 
                    Text("My pets", animate_size=30, color="white")
                ])
            )
        ])
    )
    page.add(
        Text("123")
    )


app(main)
