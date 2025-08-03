import discord
from discord.ext import commands
import datetime


#creacion y configuracion de los persimos
permisos=discord.Intents.default()
permisos.message_content = True

#creacion del bot
NP2Bbot = commands.Bot(command_prefix="$",intents=permisos)

#eventos
@NP2Bbot.event
async def on_ready():
    print("NP2Bbot esta en linea")

@NP2Bbot.command()
async def hola(ctx):
    await ctx.send(f"hola mi nombre es {NP2Bbot.user.name}")

@NP2Bbot.command()
async def info(ctx):
    server = ctx.guild
    nombre = server.name
    miembros = server.member_count
    dueno = server.owner
    await ctx.send(f"**Información del servidor:**"
                   f"Nombre: {nombre}"
                   f"Miembros: {miembros}"
                   f"Dueño: {dueno}")
    
@NP2Bbot.command()
async def hora(ctx):
    ahora = datetime.datetime.now()
    await ctx.send(f"🕒 Hora actual: {ahora.strftime('%H:%M:%S')}")

@NP2Bbot.command()
async def ayuda(ctx):
    await ctx.send("**Comandos disponibles:**"
                   "/hola - El bot te saluda"
                   "/info - Info del servidor"
                   "/hora - Ver hora actual")



