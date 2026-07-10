import discord
from discord.ext import commands
from musica import Jukebox
import asyncio


intents = discord.Intents.all()
bot = commands.Bot('.', intents=intents)

jukebox = Jukebox()

##Eventos
@bot.event
async def on_ready():
    print(f'Bot: {bot.user} pronto')

@bot.event
async def on_member_join(member:discord.Member):
    canal = bot.get_channel(1524752841506557972)
    img_membro_novo = 'https://img.ifunny.co/images/c7fd922abed13efb24e7ce0c0b4a786c0cef8f0adc401ed17e38efc448994ae4_1.jpg'

    await canal.send(f'{member.mention} entrou no server')
    await canal.send(img_membro_novo)

#Comandos
@bot.command()
async def add(ctx, link:str):
    jukebox.add_music(link)

@bot.command()
async def addpl(ctx, link:str):
    jukebox.add_playlist(link)

@bot.command()
async def clear(ctx):
    jukebox.clear_all()

@bot.command()
async def tocar(ctx: commands.Context):

    voice = None
    
    if ctx.author.voice is None:
        await ctx.send('Entre no canal primeiro')
        return
    
    if ctx.voice_client is None:
        canal = ctx.author.voice.channel
        voice = await canal.connect()
    else:
        voice = ctx.voice_client
    
    if not jukebox.has_music():
        await ctx.send('Adicione as musicas')
    
    while jukebox.has_music():

        audio = await jukebox.listen_music()

        voice.play(audio)
        
        while voice.is_playing() and not voice.is_paused():
            await asyncio.sleep(1)

        jukebox.next_music()
    
@bot.command()
async def next(ctx: commands.Context):
     
    if ctx.author.voice is None:
        await ctx.send('Entre no canal primeiro')
        return
    

    if ctx.voice_client is not None and ctx.voice_client.is_playing():
        await ctx.voice_client.stop()

    await asyncio.sleep(2)
    await tocar(ctx)

@bot.command()
async def stop(ctx: commands.Context):
     
    if ctx.voice_client is not None and ctx.voice_client.is_playing():
        ctx.voice_client.pause()

@bot.command()
async def unpause(ctx: commands.Context):
    if ctx.voice_client is not None and ctx.voice_client.is_paused():
        ctx.voice_client.resume()
    
@bot.command()
async def bomdia(ctx: commands.Context):
    nome = ctx.author.name
    await ctx.send(f'bom dia {nome}')
    await ctx.send('https://img.ifunny.co/images/2904acea4b6e8a2aec25b114d968ee620469f6282bf1d18ce7cc9e0c9932f39e_1.jpg')


@bot.command()
async def kick(ctx: commands.Context):
    try:
        print('quicado')
    except:
        await ctx.send(f'você não pode banir o homi {ctx.author.name}')

    



