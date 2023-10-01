from flet import *


class LoginPage(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return Column(
            
            controls=[
                
                Container(
                    width=500,
                    height=500,
                    gradient=LinearGradient(
                        begin=alignment.bottom_left,
                        end=alignment.top_right,
                        colors=['#1F2937 ,#111827']
                    ),
                    border_radius=border_radius.all(15),
                    content=Column(
                        horizontal_alignment='center',
                        controls=[
                            Divider(),
                            Text(
                                'LOGIN',
                                text_align='center',
                                size=40,
                                color=colors.BLUE_50,
                            ),
                            Divider(color=colors.TRANSPARENT),
                            TextField(
                                width=300,
                                label='Matricula',
                                border_color=colors.WHITE,
                                label_style=TextStyle(
                                    color=colors.WHITE
                                ),
                            ),
                            TextField(
                                width=300,
                                label='Senha',
                                label_style=TextStyle(
                                    color=colors.WHITE
                                ),
                                border_color=colors.WHITE
                            ),
                            Divider(color=colors.TRANSPARENT),
                            ElevatedButton(
                                width=100,
                                height=50,
                                text='Login',
                                style=ButtonStyle(
                                    color=colors.WHITE
                                ),
                                on_click= lambda _: self.page.go('/login'),
                            ),
                            Divider(color=colors.TRANSPARENT),
                            
                            Text(
                                'Caso não tenha uma conta, faça seu cadastro', color=colors.WHITE,
                                size=15
                            ),
                            ElevatedButton(
                                height=60,
                                text='Cadastra-se',
                                style=ButtonStyle(
                                    color=colors.WHITE
                                )
                            ),
                            Divider(),

                        ]
                    )
                ),
            ],
            alignment= MainAxisAlignment.CENTER,
        )
