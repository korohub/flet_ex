from flet import app, Page, Text, ElevatedButton, WEB_BROWSER

from flet_navigator import VirtualFletNavigator, PageData, ROUTE_404


def main_page(pg: PageData) -> None:
    # pg.page.add(Text('Main page!'))
    pg.page.add(
        ElevatedButton("page 2", on_click= lambda _: pg.navigator.navigate(second_page, pg.page, None))
    )

def second_page(pg: PageData) -> None:
    pg.page.add(Text('Second page!'))

def route_404(pg: PageData) -> None:
    ... # 404 Page Content.

def main(page: Page) -> None:
    # Initialize navigator.
    flet_navigator = VirtualFletNavigator(
        {
            '/': main_page, # Main page route.
            'second_page': second_page, # Second page route.
            ROUTE_404: route_404 # 404 page route.
        }, lambda route: print(f'Route changed!: {route}') # Route change handler (optional).
    )

    flet_navigator.render(page) # Render current page.

app(target=main, view=WEB_BROWSER)
