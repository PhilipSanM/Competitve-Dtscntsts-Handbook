# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=- 511. Game Play Analysis I =-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 14 - August - 2023
# Leetcode link = https://leetcode.com/problems/game-play-analysis-i/description/

# Runtime: 262ms Beats 93.38%of users with Pandas; Memory: 62.26mb Beats 55.41%of users with Pandas

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(by='event_date', inplace = True)
    activity.drop_duplicates(subset = 'player_id', keep = 'first', inplace = True)
    return activity[['player_id', 'event_date']].rename(columns = {'event_date': 'first_login'})
