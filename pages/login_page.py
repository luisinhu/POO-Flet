from flet import *
import sqlite3 as sql


class LoginPage(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.entry_mat = TextField(width=300, label='Matricula', label_style=TextStyle(
            color=colors.WHITE), border_color=colors.WHITE, keyboard_type=KeyboardType.NUMBER)
        self.senha = TextField(width=300, label='Senha', label_style=TextStyle(
            color=colors.WHITE), border_color=colors.WHITE )
        self.divisoria = Divider(color=colors.INDIGO)

    def build(self):
        return Column(
            controls=[
                Container(
                    padding=padding.all(80),
                    width=500,
                    height=545,
                    gradient=LinearGradient(
                        begin=alignment.bottom_left,
                        end=alignment.top_right,
                        colors=[colors.BLACK87, colors.INDIGO]
                    ),
                    border_radius=border_radius.all(15),
                    content=Column(
                        horizontal_alignment='center',
                        controls=[
                            Text(
                                'LOGIN',
                                text_align='center',
                                size=40,
                                color=colors.BLUE_50,
                            ),
                            self.entry_mat,
                            self.senha,
                            ElevatedButton(
                                'Login', on_click=lambda _: self.page.go('/cadastro'))

                        ]
                    )
                )
            ]
        )

    # def inserir_dados(self):
    #     matricula = self.entry_mat.value
    #     senha = self.senha.value
    #     banco = sql.connect("teste.db")
    #     cursor = banco.cursor()
    #     cursor.execute("INSERT INTO Alunos (matricula, senha) VALUES (?, ?)", [matricula, senha])
    #     banco.commit()
    #     banco.close()
    #     self.page.go('/')
