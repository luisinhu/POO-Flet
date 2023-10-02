from flet import *
from pages.cadastro_page import CadastroPage
from pages.login_page import LoginPage

def views_handler(page):
    return {
        '/login':View(
            '/login',
            controls=[
                LoginPage(page)
                ]
            ),
        '/cadastro':View(
            '/cadastro',
            controls=[
                CadastroPage(page)
                ]
            )
    }
