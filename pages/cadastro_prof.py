from flet import *
from classes import *


class ProfCadastro(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.entry_nome = TextField(label='Nome', width=300, border_color=colors.WHITE, label_style=TextStyle(
            color=colors.WHITE,
        ))

        self.entry_matricula = TextField(label='Matricula', width=300, border_color=colors.WHITE, label_style=TextStyle(
            color=colors.WHITE,
        ))
        self.entry_senha = TextField(label='Senha', width=300, border_color=colors.WHITE, label_style=TextStyle(
            color=colors.WHITE,
        ))
        self.entry_sexo = RadioGroup(
            content=Container(
                padding=padding.only(left=70),
                content=Column(
                    controls=[
                        Text('Sexo:'),
                        Radio(value='M', label='Masculino'),
                        Radio(value='F', label='Feminario'),
                    ]
                )
            )
        )

    def build(self):
        return Column(
            controls=[
                Container(
                    width=500,
                    height=700,
                    gradient=LinearGradient(
                        begin=alignment.top_left,
                        end=alignment.bottom_right,
                        colors=[colors.PURPLE, colors.PINK]
                    ),
                    border_radius=border_radius.all(10),
                    content=Column(

                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                            Container(height=20),
                            Text('Cadastro Prof', size=40),
                            self.entry_nome,
                            self.entry_matricula,
                            self.entry_senha,
                            self.entry_sexo,
                            ElevatedButton('Cadastra-se', style=ButtonStyle(
                                bgcolor=colors.PURPLE,
                                color=colors.WHITE
                            ),
                                on_click=lambda _: self.cadastro()

                            ),
                            Container(height=20),
                            Text('Caso já tenha uma conta, faça login'),
                            ElevatedButton(
                                'Login',
                                on_click=lambda _: self.page.go('/login'),
                                style=ButtonStyle(
                                    bgcolor=colors.PURPLE,
                                    color=colors.WHITE
                                )

                            )
                        ]
                    )
                )
            ]
        )

    def cadastro(self):
        prof = Professor(nome=self.entry_nome.value, sexo=self.entry_sexo.value, matricula=self.entry_matricula.value, senha=self.entry_senha.value)
        prof.Cadastrar()
