# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-2889. Reshape Data: Pivot=-=-=-=-==-=-=-=-=-=-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# Introduction to Pandas
# Date: 29 - October - 2023
# Leetcode link = https://leetcode.com/problems/reshape-data-pivot/

import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index="month", columns="city", values="temperature")
