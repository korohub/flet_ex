from flet import *


def main(page: Page):
    page.padding = 0
    page.spacing = 0
    page.window_height=740
    page.window_width=360


    def shownav(e):
        sidemenu.offset = transform.Offset(0,0)
        page.update()

    def hidenav(e):
        sidemenu.offset = transform.Offset(-5,0)
        page.update()

    sidemenu = Container(
        content=Text("hello", size=17), padding=10, bgcolor="red",
        width=page.window_width*0.7,
        height=page.window_height,
        margin=margin.only(top=44),
        offset=transform.Offset(-5,0),
        animate_offset=animation.Animation(200)
    )
    
    layer = Container(
        width=page.window_width,
        height=page.window_height,
        on_click=lambda e: hidenav(e),
        content = Column([
            Container(
                bgcolor="blue",
                content=Row([
                    
                    Text("My pets", size=30, color="white"),
                    IconButton(
                        icon = "menu",
                        icon_color = "white",
                        on_click = shownav,
                    ),
                ], alignment=MainAxisAlignment.END),
            )
        ])
    )

    page.add(
        Stack([
                layer,
                sidemenu
            ])
    )


app(main)
