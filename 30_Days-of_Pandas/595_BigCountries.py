# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=- 595. Big Countries =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 08 - August - 2023
# Leetcode link = https://leetcode.com/problems/big-countries/description/

# 246ms Beats 60.52%of users with Pandas ; 62.53mb Beats 42.88%of users with Pandas

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    big_countries = world[(world['population'] >= 25000000) | (world['area'] >= 3000000)]
    return big_countries[['name', 'population', 'area']]