# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=- 178. Rank Scores =-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Medium


# 30 Days of Pandas Challenge
# Date: 14 - August - 2023
# Leetcode link = https://leetcode.com/problems/rank-scores/description

# Runtime: 249ms Beats 61.32%of users with Pandas; Memory: 61.21mb Beats 91.80%of users with Pandas


import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.sort_values(by='score', ascending = False)
    index = 0
    scores['rank'] = scores['score'].rank(method = 'dense', ascending = False)
    return scores[['score', 'rank']]