# -*- coding: utf-8 -*-
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
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackContext
from telegram.constants import ParseMode
from datetime import datetime

#API's
import requests
import json

#
# Conexión de APIS
#

## LA LIGA


#API de Partidos básica
response_API = requests.get('https://api.sportsdata.io/v4/soccer/scores/json/SchedulesBasic/liga/2024?key=ca27f55a3e214fafb7c8d98721b170d0')
#print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)
equipo1 = parse_json[1]['AwayTeamName']
equipo2 = parse_json[1]['HomeTeamName']
fecha_partido = parse_json[1]['DateTime']

#API de Jugadores
jugadores_API = requests.get('https://api.sportsdata.io/v4/soccer/stats/json/PlayerSeasonStats/liga/2024?key=ca27f55a3e214fafb7c8d98721b170d0')
#print(response_API.status_code)
data_jugadores = jugadores_API.text
parse_json_jugadores = json.loads(data_jugadores)
jugador_pichichi = parse_json_jugadores[0]['PlayerSeasons'][184]['Name']
equipo_pichichi = parse_json_jugadores[0]['PlayerSeasons'][184]['Team']
goles_pichichi = parse_json_jugadores[0]['PlayerSeasons'][184]['Goals']

#API de stats de equipos
equipos_stats_API = requests.get('https://api.sportsdata.io/v4/soccer/scores/json/TeamSeasonStats/liga/2024?key=ca27f55a3e214fafb7c8d98721b170d0')
#print(response_API.status_code)
data_stats_equipos = equipos_stats_API.text
parse_json_stats_equipos = json.loads(data_stats_equipos)

#API stats equipos mejorada_LaLiga
equipos_stats_API_mejorada = requests.get('https://api.sportsdata.io/v4/soccer/scores/json/Standings/liga/2024?key=ca27f55a3e214fafb7c8d98721b170d0')
data_stats_equipos_mejorada = equipos_stats_API_mejorada.text
parse_json_stats_equipos_mejorada = json.loads(data_stats_equipos_mejorada)

#API odds 
API_odds = requests.get('https://api.the-odds-api.com/v4/sports/soccer/odds/?apiKey=78dd1b7f48ef9c786df6a6add154c41e&regions=eu&markets=h2h')
data_API_odds = API_odds.text
parse_json_API_odds = json.loads(data_API_odds)

#API Lesionados
API_lesionados = requests.get('https://api.sportsdata.io/v4/soccer/projections/json/InjuredPlayers/liga?key=ca27f55a3e214fafb7c8d98721b170d0')
data_API_lesionados = API_lesionados.text
parse_json_API_lesionados = json.loads(data_API_lesionados)




##PREMIER LEAGUE


#API stats equipos mejorada_Premier
equipos_stats_API_premier = requests.get('https://api.sportsdata.io/v4/soccer/scores/json/Standings/EPL/2024?key=ca27f55a3e214fafb7c8d98721b170d0')
data_stats_equipos_premier = equipos_stats_API_premier.text
parse_json_stats_equipos_premier = json.loads(data_stats_equipos_premier)

#API de stats de equipos básica premier
response_API_premier = requests.get('https://api.sportsdata.io/v4/soccer/scores/json/SchedulesBasic/EPL/2024?key=ca27f55a3e214fafb7c8d98721b170d0')
#print(response_API.status_code)
data_premier = response_API_premier.text
parse_json_premier = json.loads(data_premier)
equipo1 = parse_json_premier[1]['AwayTeamName']
equipo2 = parse_json_premier[1]['HomeTeamName']
fecha_partido = parse_json_premier[1]['DateTime']

#API de Jugadores Premier League
jugadores_API_premier = requests.get('https://api.sportsdata.io/v4/soccer/stats/json/PlayerSeasonStats/EPL/2024?key=ca27f55a3e214fafb7c8d98721b170d0')
#print(response_API.status_code)
data_jugadores_premier = jugadores_API_premier.text
parse_json_jugadores_premier = json.loads(data_jugadores_premier)
jugador_pichichi_premier = parse_json_jugadores_premier[0]['PlayerSeasons'][184]['Name']
equipo_pichichi_premier = parse_json_jugadores_premier[0]['PlayerSeasons'][184]['Team']
goles_pichichi_premier = parse_json_jugadores_premier[0]['PlayerSeasons'][184]['Goals']

#API Lesionados_premier
API_lesionados_premier = requests.get('https://api.sportsdata.io/v4/soccer/projections/json/InjuredPlayers/EPL?key=ca27f55a3e214fafb7c8d98721b170d0')
data_API_lesionados_premier = API_lesionados_premier.text
parse_json_API_lesionados_premier = json.loads(data_API_lesionados_premier)


##CHAMPIONS LEAGUE


#API stats equipos mejorada UCL
equipos_stats_API_ucl = requests.get('https://api.sportsdata.io/v4/soccer/scores/json/Standings/UCL/2024?key=ca27f55a3e214fafb7c8d98721b170d0')
data_stats_equipos_ucl = equipos_stats_API_ucl.text
parse_json_stats_equipos_ucl = json.loads(data_stats_equipos_ucl)


#API de stats de equipos básica UCL
response_API_ucl = requests.get('https://api.sportsdata.io/v4/soccer/scores/json/SchedulesBasic/UCL/2024?key=ca27f55a3e214fafb7c8d98721b170d0')
#print(response_API.status_code)
data_ucl = response_API_ucl.text
parse_json_ucl = json.loads(data_ucl)
equipo1 = parse_json_ucl[1]['AwayTeamName']
equipo2 = parse_json_ucl[1]['HomeTeamName']
fecha_partido_ucl = parse_json_ucl[1]['DateTime']

#API de Jugadores UCL
jugadores_API_ucl = requests.get('https://api.sportsdata.io/v4/soccer/stats/json/PlayerSeasonStats/UCL/2024?key=ca27f55a3e214fafb7c8d98721b170d0')
#print(response_API.status_code)
data_jugadores_ucl = jugadores_API_ucl.text
parse_json_jugadores_ucl = json.loads(data_jugadores_ucl)
jugador_pichichi_premier = parse_json_jugadores_ucl[0]['PlayerSeasons'][0]['Name']
equipo_pichichi_ucl = parse_json_jugadores_ucl[0]['PlayerSeasons'][0]['Team']
goles_pichichi_ucl = parse_json_jugadores_ucl[0]['PlayerSeasons'][0]['Goals']


#API Lesionados_UCL
API_lesionados_ucl = requests.get('https://api.sportsdata.io/v4/soccer/projections/json/InjuredPlayers/EPL?key=ca27f55a3e214fafb7c8d98721b170d0')
data_API_lesionados_ucl = API_lesionados_ucl.text
parse_json_API_lesionados_ucl = json.loads(data_API_lesionados_ucl)





#Dia formatado d/m/a
ahora = datetime.now()

ano = ahora.strftime("%Y")

mes = ahora.strftime("%m")

dia = ahora.strftime("%d")

fechahoy = ahora.strftime("%d/%m/%Y")


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

#
# Mensage del bot
#

    #Hola
async def hola(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hola👋, soy un bot!🤖 \n¿Como te puedo ayudar?\n/comandos para mostrar todos los comandos!")

    #Comandos
async def comandos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🆘  Lista de Comandos  🆘\n\n⚙️ Básicos ⚙️\n/hola\n/comandos\n/fecha\n\n🇪🇸 La Liga 🇪🇸\n/laliga\n/partidos\n/resultados\n/pichichi\n/asistencias\n/lesionados\n\n🇬🇧 Premier League 🇬🇧\n/premier\n/partidos_premier\n/resultados_premier\n/pichichi_premier\n/asistencias_premier\n/lesionados_premier\n\n🇪🇺 UEFA Champions League 🇪🇺\n/ucl\n/partidos_ucl\n/resultados_ucl\n/pichichi_ucl\n/asistencias_ucl\n/lesionados_ucl\n\n🎰 Odds 🎰\n/odds")

    #Fecha
async def fecha(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="La fecha de hoy es: " +fechahoy)

    #Partidos
async def partidos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    current_datetime = datetime.now()

    next_matches_info = []

    for i, match in enumerate(parse_json):
        match_datetime_str = match.get('DateTime')
        if match_datetime_str:
            match_datetime = datetime.strptime(match_datetime_str, '%Y-%m-%dT%H:%M:%S')
            if match_datetime > current_datetime:

                match_datetime += timedelta(hours=1)

                equipo1 = match['AwayTeamName']
                equipo2 = match['HomeTeamName']
                fecha_partido = match_datetime.strftime('%d/%m/%Y %H:%M')

               
                next_matches_info.append(f"Partido: {equipo1} 🆚 {equipo2}\nFecha del partido: {fecha_partido} ⏰")

                
                if len(next_matches_info) == 10:
                    break

    if next_matches_info:
       
        message_text = "\n\n".join(next_matches_info)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="🔜⚽️ Próximos 10 partidos de LaLiga ⚽️🔜")
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No hay partidos programados en el futuro cercano.")


    #Pichichi
async def pichichi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pichichis = sorted(parse_json_jugadores[0]['PlayerSeasons'], key=lambda x: x['Goals'], reverse=True)[:10]

    
    message_text = ""

    for rank, jugador in enumerate(pichichis, start=1):
        jugador_pichichi = jugador['Name']
        equipo_pichichi = jugador['Team']
        goles_pichichi = jugador['Goals']

        
        message_text +=f'{rank}º {jugador_pichichi}\nEquipo: {equipo_pichichi}\nGoles: {goles_pichichi}\n\n'

    # enviar mensage
    await context.bot.send_message(chat_id=update.effective_chat.id, text="⚽️ Lista de Goleadores de LaLiga ⚽️")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)


     #laliga
async def laliga(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    equipo_por_puntos = sorted(parse_json_stats_equipos_mejorada[0]["Standings"], key=lambda x: x["Points"], reverse=True)
    processed_teams = set()
    message_text = ""
    rank = 1
    for equipo in equipo_por_puntos:
        equipo_stats = equipo["Name"]
        equipo_stats_points = equipo["Points"]
        equipo_stats_partidos = equipo["Games"]
        equipo_stats_vitorias = equipo["Wins"]
        equipo_stats_empates = equipo["Draws"]
        equipo_stats_derrotas = equipo["Losses"]
        equipo_stats_goles_marcados = equipo["GoalsScored"]
        equipo_stats_goles_contra = equipo["GoalsAgainst"]
        equipo_stats_saldo_goles = equipo["GoalsDifferential"]

        if equipo_stats not in processed_teams:
            message_text += f'{rank}º {equipo_stats}\nPJ: {equipo_stats_partidos}|VIT: {equipo_stats_vitorias}|E: {equipo_stats_empates}|DER: {equipo_stats_derrotas}|GM: {equipo_stats_goles_marcados}|GC: {equipo_stats_goles_contra}|SG: {equipo_stats_saldo_goles}|Pts: {equipo_stats_points}\n\n'
            processed_teams.add(equipo_stats)
            rank += 1

    # Send the accumulated message
    await context.bot.send_message(chat_id=update.effective_chat.id, text="👑👑 Tabla de clasificación de LaLiga 👑👑")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)

    #Resultados
async def resultados(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    current_datetime = datetime.now()

    # Encuentra el index del proximo partido baseado en la fecha y el horario
    next_match_index = None
    for i, match in enumerate(parse_json):
        match_datetime_str = match.get('DateTime')
        if match_datetime_str:
            match_datetime = datetime.strptime(match_datetime_str, '%Y-%m-%dT%H:%M:%S')
            if match_datetime > current_datetime:
                next_match_index = i
                break

    if next_match_index is not None:
        # Extrae informacion sobre los ultimos 10 partidos
        last_10_games_info = []
        for i in range(next_match_index - 10, next_match_index):
            if i >= 0:
                home_team = parse_json[i]['HomeTeamName']
                away_team = parse_json[i]['AwayTeamName']
                score_home = parse_json[i]['HomeTeamScore']
                score_away = parse_json[i]['AwayTeamScore']

                game_info = f"Partido : {home_team} 🆚 {away_team}\nResultado: {score_home} - {score_away}"
                last_10_games_info.append(game_info)

        # Informacion sobre todos los partidos
        message_text = "\n".join(last_10_games_info[::-1])  # Lista al reves para mostrar los ultimos partidos en primero
        await context.bot.send_message(chat_id=update.effective_chat.id, text="🥅 ⚽️ Últimos resultados de la LaLiga ⚽️ 🥅")
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)

    #Asistencias
async def asistencias(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    jugador_assists = sorted(parse_json_jugadores[0]['PlayerSeasons'], key=lambda x: x['Assists'], reverse=True)[:10]

    
    message_text = ""

    for rank, assists in enumerate(jugador_assists, start=1):
        jugador_asistencias = assists['Name']
        equipo_asistencias = assists['Team']
        asistencias_asistencias = assists['Assists']

        
        message_text += f'{rank}º {jugador_asistencias}\nEquipo: {equipo_asistencias}\nAsistencias: {asistencias_asistencias}\n\n'

    await context.bot.send_message(chat_id=update.effective_chat.id, text="🤵 Lista de Asistentes de LaLiga 🤵")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)

    #Odds
async def odds(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = ""

    for game in parse_json_API_odds:
        odd_nombre1 = game["bookmakers"][3]["markets"][0]["outcomes"][0]["name"]
        odd_equipo1 = game["bookmakers"][3]["markets"][0]["outcomes"][0]["price"]
        odd_nombre2 = game["bookmakers"][3]["markets"][0]["outcomes"][1]["name"]
        odd_equipo2 = game["bookmakers"][3]["markets"][0]["outcomes"][1]["price"]
        odd_empate = game["bookmakers"][3]["markets"][0]["outcomes"][2]["price"]
        casa_apuesta = game["bookmakers"][3]["title"]

        message_text += f'🎰🍀Odds de los partidos de hoy en: {casa_apuesta}\n{odd_nombre1} 🆚 {odd_nombre2}\n| 1️⃣ | | ✖️ | | 2️⃣ | \n|{odd_equipo1}| |{odd_empate}| |{odd_equipo2}|\n\n'

    if message_text:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="🎰🍀🤑 Odds de las casas de apuestas 🤑🍀🎰")
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No hay partidos programados para hoy.")

#Lesionados
import random

async def lesionados(update: Update, context: ContextTypes.DEFAULT_TYPE):
    random_lesionado = random.choice(parse_json_API_lesionados)

    lesionados_nombre = random_lesionado["CommonName"]
    lesionados_fecha_str = random_lesionado["InjuryStartDate"]
    lesionados_fecha = datetime.strptime(lesionados_fecha_str, '%Y-%m-%dT%H:%M:%S')
    lesionados_fecha_formatted = lesionados_fecha.strftime('%d/%m/%Y')
    lesionados_foto = random_lesionado["PhotoUrl"]

    message_text = f'🚑 Jugadores Lesionados 🚑 \n\nJugador : {lesionados_nombre}\nFecha de lesión : {lesionados_fecha_formatted}\nFoto del Jugador : {lesionados_foto}\n\nQuieres ver otro jugador? /lesionados'

    await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)

 #Premier
async def premier(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    equipo_por_puntos = sorted(parse_json_stats_equipos_premier[0]["Standings"], key=lambda x: x["Points"], reverse=True)
    processed_teams = set()
    message_text = ""
    rank = 1
    for equipo in equipo_por_puntos:
        equipo_stats = equipo["Name"]
        equipo_stats_points = equipo["Points"]
        equipo_stats_partidos = equipo["Games"]
        equipo_stats_vitorias = equipo["Wins"]
        equipo_stats_empates = equipo["Draws"]
        equipo_stats_derrotas = equipo["Losses"]
        equipo_stats_goles_marcados = equipo["GoalsScored"]
        equipo_stats_goles_contra = equipo["GoalsAgainst"]
        equipo_stats_saldo_goles = equipo["GoalsDifferential"]

        if equipo_stats not in processed_teams:
            message_text += f'{rank}º {equipo_stats}\nPJ: {equipo_stats_partidos}|VIT: {equipo_stats_vitorias}|E: {equipo_stats_empates}|DER: {equipo_stats_derrotas}|GM: {equipo_stats_goles_marcados}|GC: {equipo_stats_goles_contra}|SG: {equipo_stats_saldo_goles}|Pts: {equipo_stats_points}\n\n'
            processed_teams.add(equipo_stats)
            rank += 1

    # Send the accumulated message
    await context.bot.send_message(chat_id=update.effective_chat.id, text="👑👑 Tabla de clasificación de la Premier League 👑👑")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)



     #Resultados_Premier
async def resultados_premier(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    current_datetime = datetime.now()

    # Encuentra el index del proximo partido baseado en la fecha y el horario
    next_match_index = None
    for i, match in enumerate(parse_json_premier):
        match_datetime_str = match.get('DateTime')
        if match_datetime_str:
            match_datetime = datetime.strptime(match_datetime_str, '%Y-%m-%dT%H:%M:%S')
            if match_datetime > current_datetime:
                next_match_index = i
                break

    if next_match_index is not None:
        # Extrae informacion sobre los ultimos 10 partidos
        last_10_games_info = []
        for i in range(next_match_index - 10, next_match_index):
            if i >= 0:
                home_team = parse_json_premier[i]['HomeTeamName']
                away_team = parse_json_premier[i]['AwayTeamName']
                score_home = parse_json_premier[i]['HomeTeamScore']
                score_away = parse_json_premier[i]['AwayTeamScore']

                # Divide el score por 2 si es igual o mayor que 2
                if score_home >= 2:
                    score_home /= 2
                if score_away >= 2:
                    score_away /= 2

                game_info = f"Partido : {home_team} 🆚 {away_team}\nResultado: {int(score_home)} - {int(score_away)}"
                last_10_games_info.append(game_info)

        # Informacion sobre todos los partidos
        message_text = "\n".join(last_10_games_info[::-1])  # Lista al reves para mostrar los ultimos partidos en primero
        await context.bot.send_message(chat_id=update.effective_chat.id, text="🥅 ⚽️ Últimos resultados de la Premier League ⚽️ 🥅")
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)


    #Partidos_Premier
async def partidos_premier(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        current_datetime = datetime.now()

        next_matches_info = []

        for i, match in enumerate(parse_json_premier):
            match_datetime_str = match.get('DateTime')
            if match_datetime_str:
                match_datetime = datetime.strptime(match_datetime_str, '%Y-%m-%dT%H:%M:%S')
                if match_datetime > current_datetime:

                    match_datetime += timedelta(hours=1)

                    equipo1 = match['AwayTeamName']
                    equipo2 = match['HomeTeamName']
                    fecha_partido = match_datetime.strftime('%d/%m/%Y %H:%M')

                
                    next_matches_info.append(f"Partido: {equipo1} 🆚 {equipo2}\nFecha del partido: {fecha_partido} ⏰")


                    
                    if len(next_matches_info) == 10:
                        break

        if next_matches_info:
        
            message_text = "\n\n".join(next_matches_info)
            await context.bot.send_message(chat_id=update.effective_chat.id, text="🔜⚽️ Próximos 10 partidos de la Premier League ⚽️🔜")
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="No hay partidos programados en el futuro cercano.")

#Pichichi_Premier
async def pichichi_premier(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pichichis_premier = sorted(parse_json_jugadores_premier[0]['PlayerSeasons'], key=lambda x: x['Goals'], reverse=True)[:10]

    
    message_text = ""

    for rank, jugador in enumerate(pichichis_premier, start=1):
        jugador_pichichi_premier = jugador['Name']
        equipo_pichichi_premier = jugador['Team']
        goles_pichichi_premier = jugador['Goals']

        
        message_text +=f'{rank}º {jugador_pichichi_premier}\nEquipo: {equipo_pichichi_premier}\nGoles: {goles_pichichi_premier}\n\n'

    # enviar mensage
    await context.bot.send_message(chat_id=update.effective_chat.id, text="⚽️ Lista de Goleadores de la Premier League ⚽️")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)


#Asistencias_Premier
async def asistencias_premier(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    jugador_assists_premier = sorted(parse_json_jugadores_premier[0]['PlayerSeasons'], key=lambda x: x['Assists'], reverse=True)[:10]

    
    message_text = ""

    for rank, assists_premier in enumerate(jugador_assists_premier, start=1):
        jugador_asistencias_premier = assists_premier['Name']
        equipo_asistencias_premier = assists_premier['Team']
        asistencias_asistencias_premier = assists_premier['Assists']

        
        message_text += f'{rank}º {jugador_asistencias_premier}\nEquipo: {equipo_asistencias_premier}\nAsistencias: {asistencias_asistencias_premier}\n\n'

    await context.bot.send_message(chat_id=update.effective_chat.id, text="🤵 Lista de Asistentes de la Premier League 🤵")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)


#Lesionados_Premier
import random

async def lesionados_premier(update: Update, context: ContextTypes.DEFAULT_TYPE):
    random_lesionado_premier= random.choice(parse_json_API_lesionados_premier)

    lesionados_nombre = random_lesionado_premier["CommonName"]
    lesionados_fecha_str = random_lesionado_premier["InjuryStartDate"]
    lesionados_fecha = datetime.strptime(lesionados_fecha_str, '%Y-%m-%dT%H:%M:%S')
    lesionados_fecha_formatted = lesionados_fecha.strftime('%d/%m/%Y')
    lesionados_foto = random_lesionado_premier["PhotoUrl"]

    message_text = f'🚑 Jugadores Lesionados 🚑 \n\nJugador : {lesionados_nombre}\nFecha de lesión : {lesionados_fecha_formatted}\nFoto del Jugador : {lesionados_foto}\n\nQuieres ver otro jugador? /lesionados'

    await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)


    ##  CHAMPIONS LEAGUE ##

#UCL
async def ucl(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    equipo_por_puntos_ucl = parse_json_stats_equipos_ucl[6]["Standings"]

    # Lista de Grupos de la champions
    ucl_groups = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    for group in ucl_groups:
        # Filter equipos en el grupo
        group_teams = [equipo for equipo in equipo_por_puntos_ucl if equipo["Group"] == f'Group {group}']

        # Sort de equipos por numerode partidos en orden descendiente
        sorted_teams_by_games = sorted(group_teams, key=lambda x: x["Games"], reverse=True)

        # Mejores4 equipos
        top_4_teams = sorted_teams_by_games[:4]

        # Message
        message_text = f'👑👑 Tabla de clasificación de la UCL - Grupo {group} 👑👑\n\n'
        for rank, equipo_stats_ucl in enumerate(top_4_teams, start=1):
            message_text += (
                f'{rank}º {equipo_stats_ucl["Name"]}\n'
                f'PJ: {equipo_stats_ucl["Games"]} | VIT: {equipo_stats_ucl["Wins"]} | '
                f'E: {equipo_stats_ucl["Draws"]} | DER: {equipo_stats_ucl["Losses"]} | '
                f'GM: {equipo_stats_ucl["GoalsScored"]} | GC: {equipo_stats_ucl["GoalsAgainst"]} | '
                f'SG: {equipo_stats_ucl["GoalsDifferential"]} | Pts: {equipo_stats_ucl["Points"]}\n\n'
            )

        
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text, parse_mode=ParseMode.MARKDOWN)


#Partidos_UCL
from datetime import datetime, timedelta

async def partidos_ucl(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    current_datetime = datetime.now()

    next_matches_info = []

    for i, match in enumerate(parse_json_ucl):
        match_datetime_str = match.get('DateTime')
        if match_datetime_str:
            match_datetime = datetime.strptime(match_datetime_str, '%Y-%m-%dT%H:%M:%S')
            if match_datetime > current_datetime:
                
                match_datetime += timedelta(hours=1)

                equipo1 = match['AwayTeamName']
                equipo2 = match['HomeTeamName']
                fecha_partido = match_datetime.strftime('%d/%m/%Y %H:%M')

                next_matches_info.append(f"Partido: {equipo1} 🆚 {equipo2}\nFecha del partido: {fecha_partido} ⏰")

                if len(next_matches_info) == 10:
                    break

    if next_matches_info:
        message_text = "\n\n".join(next_matches_info)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="🔜⚽️ Próximos 10 partidos de la UEFA Champions League ⚽️🔜")
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No hay partidos programados en el futuro cercano.")


#Resultados_UCL
async def resultados_ucl(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    current_datetime = datetime.now()

    # Encuentra el index del proximo partido baseado en la fecha y el horario
    next_match_index = None
    for i, match in enumerate(parse_json_ucl):
        match_datetime_str = match.get('DateTime')
        if match_datetime_str:
            match_datetime = datetime.strptime(match_datetime_str, '%Y-%m-%dT%H:%M:%S')
            if match_datetime > current_datetime:
                next_match_index = i
                break

    if next_match_index is not None:
        # Extrae informacion sobre los ultimos 10 partidos
        last_10_games_info = []
        for i in range(next_match_index - 10, next_match_index):
            if i >= 0:
                home_team = parse_json_ucl[i]['HomeTeamName']
                away_team = parse_json_ucl[i]['AwayTeamName']
                score_home = parse_json_ucl[i]['HomeTeamScore']
                score_away = parse_json_ucl[i]['AwayTeamScore']

                game_info = f"Partido : {home_team} 🆚 {away_team}\nResultado: {int(score_home)} - {int(score_away)}"
                last_10_games_info.append(game_info)

        # Informacion sobre todos los partidos
        message_text = "\n".join(last_10_games_info[::-1])  # Lista al reves para mostrar los ultimos partidos en primero
        await context.bot.send_message(chat_id=update.effective_chat.id, text="🥅 ⚽️ Últimos resultados de la UEFA Champions League ⚽️ 🥅")
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)



#Pichichi_UCL

async def pichichi_ucl(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pichichis_ucl = sorted(parse_json_jugadores_ucl[0]['PlayerSeasons'], key=lambda x: x['Goals'], reverse=True)[:10]

    
    message_text = ""

    for rank, jugador in enumerate(pichichis_ucl, start=1):
        jugador_pichichi_ucl = jugador['Name']
        equipo_pichichi_ucl = jugador['Team']
        goles_pichichi_ucl = jugador['Goals']

        
        message_text +=f'{rank}º {jugador_pichichi_ucl}\nEquipo: {equipo_pichichi_ucl}\nGoles: {goles_pichichi_ucl}\n\n'

    # enviar mensage
    await context.bot.send_message(chat_id=update.effective_chat.id, text="⚽️ Lista de Goleadores de la UEFA Champions ⚽️")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)


#Asistencias_UCL
async def asistencias_ucl(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    jugador_assists_ucl = sorted(parse_json_jugadores_ucl[0]['PlayerSeasons'], key=lambda x: x['Assists'], reverse=True)[:10]


    message_text = ""

    for rank, assists_ucl in enumerate(jugador_assists_ucl, start=1):
        jugador_asistencias_ucl = assists_ucl['Name']
        equipo_asistencias_ucl = assists_ucl['Team']
        asistencias_asistencias_ucl = assists_ucl['Assists']

        
        message_text += f'{rank}º {jugador_asistencias_ucl}\nEquipo: {equipo_asistencias_ucl}\nAsistencias: {asistencias_asistencias_ucl}\n\n'

    await context.bot.send_message(chat_id=update.effective_chat.id, text="🤵 Lista de Asistentes de la UCL 🤵")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)


#Lesionados_UCL
import random

async def lesionados_ucl(update: Update, context: ContextTypes.DEFAULT_TYPE):
    random_lesionado_ucl= random.choice(parse_json_API_lesionados_ucl)

    lesionados_nombre_ucl = random_lesionado_ucl["CommonName"]
    lesionados_fecha_str_ucl = random_lesionado_ucl["InjuryStartDate"]
    lesionados_fecha_ucl = datetime.strptime(lesionados_fecha_str_ucl, '%Y-%m-%dT%H:%M:%S')
    lesionados_fecha_formatted_ucl = lesionados_fecha_ucl.strftime('%d/%m/%Y')
    lesionados_foto_ucl = random_lesionado_ucl["PhotoUrl"]

    message_text = f'🚑 Jugadores Lesionados 🚑 \n\nJugador : {lesionados_nombre_ucl}\nFecha de lesión : {lesionados_fecha_formatted_ucl}\nFoto del Jugador : {lesionados_foto_ucl}\n\nQuieres ver otro jugador? /lesionados'

    await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)
    



#
# Comando introducido por el usuario
#


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

    ## LA LIGA ##

    #Partido
    partidos_handler = CommandHandler('partidos', partidos)
    application.add_handler(partidos_handler)

    #Pichichi
    pichichi_handler = CommandHandler('pichichi', pichichi)
    application.add_handler(pichichi_handler)

    #laliga
    laliga_handler = CommandHandler('laliga', laliga)
    application.add_handler(laliga_handler)

    #Resultados
    resultados_handler = CommandHandler('resultados', resultados)
    application.add_handler(resultados_handler)

    #Asistencias
    asistencias_handler = CommandHandler('asistencias', asistencias)
    application.add_handler(asistencias_handler)

    #Lesionados
    lesionados_handler = CommandHandler('lesionados', lesionados)
    application.add_handler(lesionados_handler)

        ## PREMIER LEAGUE ##

    #Premier
    premier_handler = CommandHandler('premier', premier)
    application.add_handler(premier_handler)
    
    #Resultados_Premier
    resultados_premier_handler = CommandHandler('resultados_premier', resultados_premier)
    application.add_handler(resultados_premier_handler)

    #Partido_Premier
    partidos_premier_handler = CommandHandler('partidos_premier', partidos_premier)
    application.add_handler(partidos_premier_handler)
 
    #Pichichi_Premier
    pichichi_premier_handler = CommandHandler('pichichi_premier', pichichi_premier)
    application.add_handler(pichichi_premier_handler)

    #Asistencias_Premier
    asistencias_premier_handler = CommandHandler('asistencias_premier', asistencias_premier)
    application.add_handler(asistencias_premier_handler)

    #Lesionados_Premier
    lesionados_premier_handler = CommandHandler('lesionados_premier', lesionados_premier)
    application.add_handler(lesionados_premier_handler)


    ## CHAMPIONS LEAGUE ##

    #UCL
    ucl_handler = CommandHandler('ucl', ucl)
    application.add_handler(ucl_handler)

    #Partido_UCL
    partidos_ucl_handler = CommandHandler('partidos_ucl', partidos_ucl)
    application.add_handler(partidos_ucl_handler)

    #Resultados_UCL
    resultados_ucl_handler = CommandHandler('resultados_ucl', resultados_ucl)
    application.add_handler(resultados_ucl_handler)

    #Pichichi_UCL
    pichichi_ucl_handler = CommandHandler('pichichi_ucl', pichichi_ucl)
    application.add_handler(pichichi_ucl_handler)

    #Asistencias_UCL
    asistencias_ucl_handler = CommandHandler('asistencias_ucl', asistencias_ucl)
    application.add_handler(asistencias_ucl_handler)

    #Lesionados_UCL
    lesionados_ucl_handler = CommandHandler('lesionados_ucl', lesionados_ucl)
    application.add_handler(lesionados_ucl_handler)
    


    ## ODDS ##

    #Odds
    odds_handler = CommandHandler('odds', odds)
    application.add_handler(odds_handler)


    application.run_polling()