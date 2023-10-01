from flet import *

class PageCadastro(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
    
    def build (self):
        return Column(
            controls=[
                Container(
                    height=800,
                    width=200,
                    bgcolor='blue',
                    content=Column(
                        controls=[
                            Text('LOGIN PAGE'), 
                            Container(
                                on_click=lambda _: self.page.go('/') ,
                                content=Text(
                                    'ir para homepage'
                                    )
                                )
                            ]
                        )
                    )
            ]
        )