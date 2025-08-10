import discord
from discord.ext import commands
import datetime
import os
import random
import urllib.request
import json

# Creación y configuración de los permisos
permisos = discord.Intents.default()
permisos.message_content = True

# Creación del bot
NP2Bbot = commands.Bot(command_prefix="'", intents=permisos)

#Funcion para los patos
def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
    return data['url']

#Eventos
@NP2Bbot.event
async def on_ready():
    print("NP2Bbot está en línea, escribe: 'ayuda para saber todos los comandos disponibles")

@NP2Bbot.command()
async def hola(ctx):
    await ctx.send(f"hola mi nombre es {NP2Bbot.user.name}")

@NP2Bbot.command()
async def info(ctx):
    server = ctx.guild
    nombre = server.name
    miembros = server.member_count
    dueno = server.owner
    await ctx.send(f"**Información del servidor: **"
                   f"Nombre: {nombre}, "
                   f"Miembros: {miembros}, "
                   f"Dueño: {dueno}. ")

@NP2Bbot.command()
async def hora(ctx):
    ahora = datetime.datetime.now()
    await ctx.send(f"Hora actual: {ahora.strftime('%H:%M:%S')}")

@NP2Bbot.command()
async def meme(ctx):
    lista_memes = os.listdir("image")
    meme_random = random.choice(lista_memes)
    await ctx.send("Aquí tienes un meme divertido sobre programación.")
    with open(f"image/{meme_random}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@NP2Bbot.command()
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@NP2Bbot.command()
async def ayuda(ctx):
    await ctx.send("**Comandos disponibles:**\n"
                   "'hola - El bot te saluda\n"
                   "'info - Info del servidor\n"
                   "'hora - Ver hora actual\n"
                   "'meme - Mandar un meme divertido\n"
                   "'duck - Enviar un pato aleatorio")


#rememmber to put the token.



