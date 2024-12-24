import flet as ft
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Autenticação com o Spotify usando o fluxo OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='d2f2b7b8cc6944a0bbb9237d31b29793',
    client_secret='8020fe7845174b30af263e52daf753ab',
    redirect_uri="https://github.com/Gustavofava123350/Natal",  # Substitua pelo URI correto
    scope="user-library-read user-top-read playlist-modify-public"
))

def main(page: ft.Page):
    # Adicionando o tema de Natal na interface
    page.title = "🎄 Músicas de Natal 🎶"
    page.bgcolor = "lightgreen"
    page.add(ft.Text("🎄 Músicas de Natal 🎶", size=30, color="red", weight="bold"))

    # Função para pegar músicas de uma playlist de Natal
    def fetch_data():
        try:
            playlist = sp.playlist_tracks("37i9dQZF1DX4dyxBJJ2Ibc")  # ID da playlist de Natal
            tracks = playlist['items']
            return [track['track']['name'] for track in tracks]
        except spotipy.exceptions.SpotifyException:
            return ["Erro: Não foi possível acessar a API do Spotify. Verifique suas credenciais."]
        except Exception as e:
            return [f"Erro desconhecido: {str(e)}"]

    # Função para atualizar a lista de músicas
    def update_playlist(e):
        track_names = fetch_data()
        track_list.controls = [ft.Text(track, color="green", size=20) for track in track_names]
        page.update()

    # Obter músicas de Natal
    track_names = fetch_data()

    # Exibir músicas com tema de Natal
    track_list = ft.Column([ft.Text(track, color="green", size=20) for track in track_names])
    page.add(track_list)

    # Botão para atualizar a lista de músicas
    button_refresh = ft.ElevatedButton("Atualizar Músicas", on_click=update_playlist)
    page.add(button_refresh)

# Iniciar o app na web
ft.app(target=main, view=ft.WEB_BROWSER)  # Isso faz o app abrir diretamente no navegador
