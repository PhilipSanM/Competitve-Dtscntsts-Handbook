# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--1050. Actors and Directors Who Cooperated At Least Three Times =-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 23 - August - 2023
# Leetcode link = https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/description/

# There are some bugs on leetcode right now and my RUNTIME is wrong ; Memory 61MB Beats 81.22%of users with Pandas
import pandas as pd


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    cooperated_directors = (
        actor_director.groupby(["actor_id", "director_id"])
        .size()
        .reset_index(name="times")
    )
    return cooperated_directors[cooperated_directors["times"] >= 3][
        ["actor_id", "director_id"]
    ]
