from fastapi import FastAPI
import datetime
import requests

app = FastAPI()
# http://127.0.0.1:8000/docs   
# 
@app.get("/health")
def health():
    return {"status": "ok"}



@app.get("/scoreboard/today")
def scoreboard_today():
    today = datetime.date.today().isoformat()

    url = "https://statsapi.mlb.com/api/v1/schedule"
    # ID1 means MLB. Hydrate means get extra/all data for team and linescore fields 
    params = {
        "sportId": 1,
        "date": today,
        "hydrate": "team,linescore"
    }

    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()

    games_out = []

    dates = data.get("dates", [])
    if dates:
        games = dates[0].get("games", [])
        for g in games:
            game_pk = g.get("gamePk")
            status = g.get("status", {}).get("detailedState")

            teams = g.get("teams", {})
            away = teams.get("away", {})
            home = teams.get("home", {})

            games_out.append({
                "gameId": game_pk,
                "status": status,
                "away": {
                    "name": away.get("team", {}).get("name"),
                    "score": away.get("score"),
                },
                "home": {
                    "name": home.get("team", {}).get("name"),
                    "score": home.get("score"),
                },
            })

    return {
        "date": today,
        "games": games_out,
        "count": len(games_out),
    }