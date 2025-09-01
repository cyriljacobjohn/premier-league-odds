import requests
import pandas as pd

API_KEY = "YOUR_API_KEY"   # put your API-Football key here
BASE_URL = "https://v3.football.api-sports.io"
headers = {"x-apisports-key": "718d63a3b3fa4a1ff426da6b429f9fb9"}

def get_fixtures(league_id=39, season=2024):
    """
    Fetch finished fixtures for a league/season.
    """
    url = f"{BASE_URL}/fixtures"
    params = {"league": league_id, "season": season, "status": "FT"}
    r = requests.get(url, headers=headers, params=params)
    r.raise_for_status()
    data = r.json()["response"]

    rows = []
    for match in data:
        home_goals = match["goals"]["home"]
        away_goals = match["goals"]["away"]

        if home_goals > away_goals:
            outcome = "home_win"
        elif away_goals > home_goals:
            outcome = "away_win"
        else:
            outcome = "draw"

        rows.append({
            "fixture_id": match["fixture"]["id"],
            "date": match["fixture"]["date"],
            "season": season,
            "home_team": match["teams"]["home"]["name"],
            "away_team": match["teams"]["away"]["name"],
            "home_goals": home_goals,
            "away_goals": away_goals,
            "outcome": outcome
        })

    return pd.DataFrame(rows)

if __name__ == "__main__":
    # ⚡ Adjust this list if you want more/less seasons
    seasons = [2021, 2022, 2023, 2024]

    all_data = []
    for season in seasons:
        print(f"Fetching EPL season {season}...")
        df = get_fixtures(39, season)
        all_data.append(df)

    full_df = pd.concat(all_data, ignore_index=True)
    full_df.to_csv("data/epl_fixtures_2021_2024.csv", index=False)
    print("✅ Saved data/epl_fixtures_2021_2024.csv with", len(full_df), "matches")
