from flet import *
from flet_navigator import PageData, template, NavigatorAnimation, FletNavigator, Arguments

def goto_page(pg:PageData, args:Arguments):
    pg.page.add(
        ElevatedButton(args[0], on_click=lambda _: pg.navigator.navigate(args[1], pg.page, args[2]))
    )

def home(pg:PageData):
    pg.page.add(
        Container(
            bgcolor="red",
            padding=10,
            width=pg.page.window_width,
            content=Text("home", size=30, color="white")
        )
    )
    template(goto_page, pg, ("go to page 2", "twopage", None))

def twopage(pg:PageData):
    pg.page.add(
        Container(
            bgcolor="red",
            padding=10,
            width=pg.page.window_width,
            content=Text("twopage", size=30, color="white")
        )
    )
    template(goto_page, pg, ("go to Home", "/", None))

def main(page:Page):
    navigator = FletNavigator(
        page, {
            "/":home,
            "twopage":twopage
        },
        navigator_animation=NavigatorAnimation(
            NavigatorAnimation.SCALE
        )
    )
    navigator.render(page)


app(main, view=WEB_BROWSER)
