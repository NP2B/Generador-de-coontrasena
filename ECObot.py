import discord
from discord.ext import commands
import random

# Creación y configuración de los permisos
permisos = discord.Intents.default()
permisos.message_content = True

# Creación del bot
ECObot = commands.Bot(command_prefix="!", intents=permisos, description="Tu bot ecológico")

# Creacion de listas
eco_tips = [
    " Lleva tu propia bolsa reutilizable cuando vayas de compras.",
    " Cierra el grifo mientras te cepillas los dientes para ahorrar agua.",
    " Planta un árbol: ayuda a absorber CO₂ y da sombra.",
    " Usa bicicleta o camina para distancias cortas, reduce la contaminación.",
    " Desconecta los cargadores cuando no los uses: siguen consumiendo energía."
]

eco_facts = [
    " Se necesitan unos 500 años para que una botella de plástico se degrade.",
    " Cambiar a bombillas LED puede ahorrar hasta un 80% de energía.",
    " Una sola persona reciclando papel durante un año puede salvar 17 árboles.",
    " El 97% del agua de la Tierra es salada, solo el 3% es dulce y limitada."
]

preguntas = [
    {
        "pregunta": "¿Cuánto tarda en degradarse una botella de plástico?",
        "opciones": ["50 años", "500 años", "1000 años"],
        "respuesta": "500 años"
    },
    {
        "pregunta": "¿Cuál es la fuente de energía renovable más usada en el mundo?",
        "opciones": ["Solar", "Hidráulica", "Eólica"],
        "respuesta": "Hidráulica"
    },
    {
        "pregunta": "¿Cuánto papel se ahorra reciclando 1 tonelada?",
        "opciones": ["5 árboles", "17 árboles", "25 árboles"],
        "respuesta": "17 árboles"
    }
]


#Eventos
@ECObot.event
async def on_ready():
    print("ECObot está en línea")

#Comandos
@ECObot.command()
async def hola(ctx):
    print("Hola soy **ECObot** vengo a darte tips y ayudarte a cuidar nuestro planeta!!", "Escribe !ayuda para averiguar todos los comandos disponibles")

@ECObot.command()
async def ayuda(ctx):
    await ctx.send(""" **Comandos disponibles**:
- !tip = Obtén un consejo ecológico práctico 
- !dato = Aprende un dato curioso sobre el medio ambiente 
- !reto = Acepta un reto ecológico del día
- !ecoquote = Te dice una frase importante sobre el ecosistema """)
    
@ECObot.command()
async def tip(ctx):
    consejo = random.choice(eco_tips)
    await ctx.send(consejo)

@ECObot.command()
async def dato(ctx):
    dato = random.choice(eco_facts)
    await ctx.send(dato)

@ECObot.command()
async def reto(ctx):
    retos = [
        " Reto del día: usa una botella reutilizable en lugar de botellas plásticas.",
        " Reto del día: lleva tu propia bolsa al supermercado.",
        " Reto del día: intenta no usar pajitas de plástico.",
        " Reto del día: apaga las luces de habitaciones que no uses.",
        " Reto del día: usa bici o camina al menos una parte de tu trayecto."
    ]
    reto = random.choice(retos)
    await ctx.send(reto)

@ECObot.commad()
async def ecoquote(ctx):
    print("La Tierra no es una herencia de nuestros padres, sino un préstamo de nuestros hijos.")


# No olvides poner el TOKEN
