import requests
import json

#API de stats de equipos
equipos_stats_API = requests.get('https://api.sportsdata.io/v4/soccer/scores/json/TeamSeasonStats/liga/2024?key=2243fc17850844ae8e464b01e260795c')
#print(response_API.status_code)
data_stats_equipos = equipos_stats_API.text
parse_json_stats_equipos = json.loads(data_stats_equipos)

#jugador_pichichi = parse_json_stats_equipos[0]['PlayerSeasons'][184]['Name']

for i in range(0, 17, +1):
    equipo_stats = parse_json_stats_equipos[0]["TeamSeasons"][i]["Name"]
    #equipo_stats_goles = parse_json_stats_equipos[0]["TeamSeasons"][i]["Score"]
    print(equipo_stats)
    
    #print(equipo_stats_goles)
    