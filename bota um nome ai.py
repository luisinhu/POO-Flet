from flet import *
from views import views_handler

# Função para lidar com a mudança de rota.
def route_change(page, route):
    print(page.route)  # Imprime a rota atual da página.
    page.views.clear()  # Limpa a lista de "views" da página.
    
    # Adiciona a "view" correspondente à rota atual à lista de "views" da página.
    page.views.append(
        views_handler(page)[page.route]
    )

# Função principal do aplicativo.
def main(page: Page):
    
    page.window_width = 500
    page.window_height = 600
    
    
    page.on_route_change = lambda route: route_change(page, route)
    page.go('/cadastro')

# Chama o aplicativo, passando a função "main" como alvo para iniciar o aplicativo.
app(target=main)
