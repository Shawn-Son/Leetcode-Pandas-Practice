import pandas as pd

def find_all_matches(teams: pd.DataFrame) -> pd.DataFrame:
    match=teams.merge(teams,how='cross')
    result=match[match['team_name_x']!=match['team_name_y']].rename(columns={'team_name_x':'home_team','team_name_y':'away_team'})
    return result