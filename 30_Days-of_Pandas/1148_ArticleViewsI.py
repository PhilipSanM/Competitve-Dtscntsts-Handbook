# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=- 1148. Article Views I =-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 07 - August - 2023
# Leetcode link = https://leetcode.com/problems/article-views-i/description/

# 247ms Beats 94.22%of users with Pandas ; 61.53mb Beats 53.51%of users with Pandas


import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    authors = views[views['author_id'] == views['viewer_id']][['author_id']].rename(columns = {'author_id' : 'id'}).drop_duplicates(subset = 'id')
    
    return authors.sort_values(by = 'id')