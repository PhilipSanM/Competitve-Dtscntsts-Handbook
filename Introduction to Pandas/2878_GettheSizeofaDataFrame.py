# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-= 2878. Get the Size of a DataFrame =-=-=-=-==-=-=-=-=-=-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# Introduction to Pandas
# Date: 05 - October - 2023
# Leetcode link = https://leetcode.com/problems/get-the-size-of-a-dataframe/description/

import pandas as pd


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]
