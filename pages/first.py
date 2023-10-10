from flet import *


class FirstPage(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return Column(
            controls=[
                Container(
                    
                    width=400,
                    height=400,
                    border_radius=border_radius.all(10),
                    gradient=LinearGradient(
                        begin=alignment.top_left,
                        end=alignment.bottom_right,
                        colors=[colors.CYAN, colors.PURPLE]
                    ),
                    content=Column(
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text('Você é Aluno ou Professor?', size=20),
                            ElevatedButton('Aluno', style=ButtonStyle(
                                bgcolor=colors.CYAN,
                                color=colors.WHITE
                            ),
                                on_click=lambda _: self.page.go('/cadastro')
                            ),
                            ElevatedButton('Professor', style=ButtonStyle(
                                bgcolor=colors.PURPLE,
                                color=colors.WHITE
                            ), on_click=lambda _: self.page.go('/cadastro_prof'))
                        ]
                    )


                )
            ]
        )
