
import yt_dlp
import discord
import asyncio
from collections import deque
from urllib.parse import urlparse, parse_qs


class Jukebox:

    def __init__(self):
        self.__musicas = deque()

    #limpar musicas
    def clear_all(self):
        self.__musicas.clear()



    #Adiconar musicas
    def add_music(self, url:str):
        self.__musicas.append(limpar_url(url))

    #Adiconar playlist
    def add_playlist(self, url: str):

        ydl_opts = {
            "quiet": True,
            "extract_flat": True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        for video in info["entries"]:
            video_id = video["id"]
            url_video = f"https://www.youtube.com/watch?v={video_id}"    
            self.add_music(url_video)
        
    #proxima musica
    def next_music(self):
        if self.has_music():
         return self.__musicas.popleft()
        
    
    def get_music(self):
        return self.__musicas


    #Ouvir a primeira musica e a mesma removê-la
    async def listen_music(self):

        ydl_opts = {
            "format": "bestaudio/best",
            "quiet": True,
            "no_warnings": True,
            "noplaylist": True
        }

        music_url = self.__musicas[0]

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            info = await asyncio.to_thread(
                ydl.extract_info,
                music_url,
                download=False
            )

        return discord.FFmpegPCMAudio(
            info["url"],
            executable=r"C:\Users\Carlos Felipe\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin\ffmpeg.exe",
            before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
        )
         
    

    
    
    def has_music(self):
        return len(self.__musicas) > 0
    
def limpar_url(url):
    query = parse_qs(urlparse(url).query)

    if "v" in query:
        return f"https://www.youtube.com/watch?v={query['v'][0]}"

    return url







