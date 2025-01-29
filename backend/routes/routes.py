from flask import Blueprint, jsonify
from ..models.models import ATSPicks
import json
main = Blueprint('main', __name__)


@main.route('/get_picks', methods=['GET'])
def get_picks():
    picks = ATSPicks.query.all()
    for pick in picks:
        pick.correct = testPick(pick)
    summary_2024 = getSeasonSummary(picks, 2024)
    for week in range(1, 19):
        week_summary = getWeekSummary(picks, 2024, week)
        summary_2024[f'week_{week}'] = week_summary
    return jsonify(summary_2024)

def getSeasonSummary(picks, season):
    season_picks = [pick for pick in picks if pick.season == season]
    correct_picks = [pick for pick in season_picks if testPick(pick)]
    season_sum = {
        'season': season,
        'total_picks': len(season_picks),
        'correct_picks': len(correct_picks),
        'accuracy': len(correct_picks) / len(season_picks)
    }
    return season_sum

def getWeekSummary(picks, season, week):
    week_picks = [pick for pick in picks if pick.season == season and pick.week == week]
    correct_picks = [pick for pick in week_picks if testPick(pick)]
    week_sum = {
        'season': season,
        'week': week,
        'total_picks': len(week_picks),
        'correct_picks': len(correct_picks),
        'accuracy': len(correct_picks) / len(week_picks)
    }
    return week_sum

def testPick(pick):
    home_team = pick.home_team
    home_score = pick.home_score

    away_team = pick.away_team
    away_score = pick.away_score

    team_picked = pick.pick
    spread = pick.spread
    
    # If the home team is the team picked
    if team_picked == home_team:
        if (home_score + spread) > away_score:
            return True
        else:
            return False
    # If the away team is the team picked   
    else:
        if (away_score + spread) > home_score:
            return True
        else:
            return False