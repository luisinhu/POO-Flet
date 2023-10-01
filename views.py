from flet import *
from pages.loginpage import LoginPage
from pages.cadastropage import PageCadastro

def views_handler(page):
    return {
        '/':View(
            '/',
            controls=[
                LoginPage(page)
                ]
            ),
        '/login':View(
            '/login',
            controls=[
                PageCadastro(page)
                ]
            )
    }
