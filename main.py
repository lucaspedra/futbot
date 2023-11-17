##import telegram.ext

##from typing import Final
##from telegram import Update
##from telegram.ext import Apllication, CommandHandler, filters, ContextTypes


##TOKEN: Final  = '6985250842:AAFVfBqd-vKh0UqI6myyeV4GoSr5Yojq8vk'
##BOT_USERNAME: Final = '@futboldiario_bot'

##async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
##    await update.message.reply_text("¡Hola, Bienvenido!")

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from datetime import datetime

#API's
import requests
import json

#API de Partidos
response_API = requests.get('https://api.sportsdata.io/v4/soccer/scores/json/SchedulesBasic/liga/2024?key=2243fc17850844ae8e464b01e260795c')
#print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)
equipo1 = parse_json[355]['AwayTeamName']
equipo2 = parse_json[355]['HomeTeamName']
fecha_partido = parse_json[355]['DateTime']

#API de Jugadores
jugadores_API = requests.get('https://api.sportsdata.io/v4/soccer/stats/json/PlayerSeasonStats/liga/2024?key=2243fc17850844ae8e464b01e260795c')
#print(response_API.status_code)
data_jugadores = jugadores_API.text
parse_json_jugadores = json.loads(data_jugadores)
jugador_pichichi = parse_json_jugadores[0]['PlayerSeasons'][184]['Name']
equipo_pichichi = parse_json_jugadores[0]['PlayerSeasons'][184]['Team']
goles_pichichi = parse_json_jugadores[0]['PlayerSeasons'][184]['Goals']

#API de stats de equipos
equipos_stats_API = requests.get('https://api.sportsdata.io/v4/soccer/scores/json/TeamSeasonStats/liga/2024?key=2243fc17850844ae8e464b01e260795c')
#print(response_API.status_code)
data_stats_equipos = equipos_stats_API.text
parse_json_stats_equipos = json.loads(data_stats_equipos)

#jugador_pichichi = parse_json_stats_equipos[0]['PlayerSeasons'][184]['Name']

for i in range(0, 17, +1):
    equipo_stats = parse_json_stats_equipos[0]["TeamSeasons"][i]["Name"]
    equipo_stats_goles = parse_json_stats_equipos[0]["TeamSeasons"][i]["Score"]
    print(equipo_stats )

async def laliga(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for i in range(0, 17, +1):
    equipo_stats = parse_json_stats_equipos[0]["TeamSeasons"][i]["Name"]
    equipo_stats_goles = parse_json_stats_equipos[0]["TeamSeasons"][i]["Score"]
        context.bot.send_message(chat_id=update.effective_chat.id, text=equipo_stats )





#Dia formatado d/m/a
ahora = datetime.now()

año = ahora.strftime("%Y")

mes = ahora.strftime("%m")

dia = ahora.strftime("%d")

fechahoy = ahora.strftime("%d/%m/%Y")


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

    #Hola
async def hola(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hola, soy un bot! \n¿Como te puedo ayudar?")

    #Comandos
async def comandos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Lista de Comandos:\n/hola\n/comandos\n/fecha\n/partido")

    #Fecha
async def fecha(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="La fecha de hoy es: " +fechahoy)

    #Partidos
async def partido(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Próximo Partido : " +equipo1+ " vs " +equipo2  )
    #await context.bot.send_message(chat_id=update.effective_chat.id, text=equipo1)
    #await context.bot.send_message(chat_id=update.effective_chat.id, text="vs")
    #await context.bot.send_message(chat_id=update.effective_chat.id, text=equipo2)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Fecha del próximo partido :" +fecha_partido)

    #Pichichi
async def pichichi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="El jugador con mas goles en LaLiga es : "+jugador_pichichi+ " \nEquipo : " +equipo_pichichi+ " \nGoles : "+str(goles_pichichi))

     #laliga
#async def laliga(update: Update, context: ContextTypes.DEFAULT_TYPE):
 #   await context.bot.send_message(chat_id=update.effective_chat.id, text="")


if __name__ == '__main__':
    application = ApplicationBuilder().token('6985250842:AAFVfBqd-vKh0UqI6myyeV4GoSr5Yojq8vk').build()

    #Hola
    hola_handler = CommandHandler('hola', hola)
    application.add_handler(hola_handler)

    #Comandos
    comandos_handler = CommandHandler('comandos', comandos)
    application.add_handler(comandos_handler)

    #Fecha
    fecha_handler = CommandHandler('fecha', fecha)
    application.add_handler(fecha_handler)

    #Partido
    partido_handler = CommandHandler('partido', partido)
    application.add_handler(partido_handler)

    #Pichichi
    pichichi_handler = CommandHandler('pichichi', pichichi)
    application.add_handler(pichichi_handler)

    #laliga
    laliga_handler = CommandHandler('laliga', laliga)
    application.add_handler(laliga_handler)












    application.run_polling()