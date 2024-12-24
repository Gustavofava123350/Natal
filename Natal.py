import flet as ft
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='d2f2b7b8cc6944a0bbb9237d31b29793',
    client_secret='15895a1683d348c39eb6ecda56f4fb9a',
    redirect_uri= 'https://github.com/Gustavofava123350/Natal'
))

def main(page: ft.Page):
    #addicionado o tema de Natal na interface
    page.bgcolor = "ligthgreen" #cor de fundo verde
    page.add(ft.Text("🎄 Músicas de Natal 🎶 ",size=30, color="red", weight="blod"))

    #função para pegar músicas de uma playlist de Natal
    def fetch_data():
        try:
            playlist = sp.playlist_tracks("37i9dQZF1DX4rrZkqR8cUp")
            tracks = playlist['items']
            track_names = [track['track']['name'] for track in tracks]
            return track_names
        except spotipy.exceptions.SpotifyException as e:
            return["Erro ao acessar a API do Spotify, verifique as credeciais ou conexão. "]
        except Exception as e:
            return[f"Error desconhecido: {str(e)}"]
        
        #obter músicas de Natal
        track_names = fetch_data()

        #Exibir músicas com trema de Natal
        track_list = ft.Column([ft.Text(track, color="green",size=20)for track in track_names])

        #botão para voltar ao início
        button_back = ft.ElevatedButton("Voltar ao inicio", on_click=lambda e: page.update())

        #add os items na tela 
        page.add(track_list, button_back)

#iniciar o app
ft.app(target=min)


    
