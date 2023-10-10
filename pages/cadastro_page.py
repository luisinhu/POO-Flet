from flet import *
from classes import *


class PageCadastro(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.entry_nome = TextField(width=300, label='Nome', label_style=TextStyle(
            color=colors.WHITE), border_color=colors.WHITE)

        self.entry_mat = TextField(width=300, label='Matricula', label_style=TextStyle(
            color=colors.WHITE), border_color=colors.WHITE, keyboard_type=KeyboardType.NUMBER)

        self.entry_senha = TextField(width=300, label='Senha', password=True, can_reveal_password=True,
                                    label_style=TextStyle(color=colors.WHITE), border_color=colors.WHITE)

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

        self.turma = Dropdown(
                options=[
                    dropdown.Option('1 INFO A'),
                    dropdown.Option('1 INFO B'),
                    dropdown.Option('1 ELET A'),
                    dropdown.Option('1 ELET B'),
                    dropdown.Option('1 EDIF A'),
                    dropdown.Option('1 EDIF B'),
                    dropdown.Option('1 QUIM A'),
                    dropdown.Option('1 QUIM B'),
                    dropdown.Option('2 INFO M'),
                    dropdown.Option('2 INFO V'),
                    dropdown.Option('2 ELET M'),
                    dropdown.Option('2 ELET V'),
                    dropdown.Option('2 EDIF M'),
                    dropdown.Option('2 EDIF V'),
                    dropdown.Option('2 QUIM M'),
                    dropdown.Option('2 QUIM V'),
                    dropdown.Option('3 INFO M'),
                    dropdown.Option('3 INFO V'),
                    dropdown.Option('3 ELET M'),
                    dropdown.Option('3 ELET V'),
                    dropdown.Option('3 EDIF M'),
                    dropdown.Option('3 EDIF V'),
                    dropdown.Option('3 QUIM M'),
                    dropdown.Option('3 QUIM V'),

                ],
                width=200,
                border_color=colors.WHITE,
                label='Turma',
                label_style= TextStyle(color=colors.WHITE)
            )

        

        self.divisoria = Container(height=20)

    def build(self):
        return Column(
            controls=[
                Container(
                    width=800,
                    height=800,
                    gradient=LinearGradient(
                        begin=alignment.bottom_left,
                        end=alignment.top_right,
                        colors=[colors.BLACK87, colors.INDIGO]
                    ),
                    border_radius=border_radius.all(15),
                    content=Column(
                        horizontal_alignment='center',
                        controls=[
                            self.divisoria,
                            Text(
                                'Cadastro',
                                text_align='center',
                                size=40,
                                color=colors.BLUE_50,
                            ),
                            self.entry_nome,
                            self.entry_mat,
                            self.entry_senha,
                            self.turma,
                            self.entry_sexo,
                            ElevatedButton(
                                'Cadastra-se', on_click= lambda _: self.cadastrar()),
                            self.divisoria,
                            Text('Caso já tenha uma conta, faça Login'),
                            ElevatedButton(
                                'Login', on_click=lambda _: self.page.go('/login'))
                        ]
                    )
                )
            ],
        )

    def cadastrar(self):
        aluno = Aluno(nome= self.entry_nome.value, matricula= self.entry_mat.value,senha= self.entry_senha.value, sexo= self.entry_sexo.value, turma= self.turma.value)
        
        aluno.Cadastrar()