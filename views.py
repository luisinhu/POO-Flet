from flet import *
from pages.login_page import LoginPage
from pages.cadastro_page import PageCadastro
from pages.first import FirstPage
from pages.cadastro_prof import ProfCadastro


def views_handler(page):
    return {
        '/': View(
            '/',
            horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER,
            controls=[
                FirstPage(page)
            ]
        ),
        '/login': View(
            '/login',
            horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER,
            controls=[
                LoginPage(page)
            ]
        ),
        '/cadastro': View(
            '/cadastro',
            horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER,
            controls=[
                PageCadastro(page)
            ]
        ),
        '/cadastro_prof': View(
            '/cadastro_prof',
            horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER,
            controls=[
                ProfCadastro(page)
            ]
        )
    }
