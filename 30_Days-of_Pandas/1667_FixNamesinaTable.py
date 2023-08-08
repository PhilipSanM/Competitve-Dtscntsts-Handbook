# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-= 1667. Fix Names in a Table -=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 08 - August - 2023
# Leetcode link = https://leetcode.com/problems/fix-names-in-a-table/description/

# 279ms Beats 40.64%of users with Pandas ; 61.10mb Beats 93.53%of users with Pandas

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.title()
    return users.sort_values(by = 'user_id')


# Runtime 270 ms Beats 59.41% ; Memory 61.7 MB Beats 43.90%
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.lower()
    users['name'] = [name[0].upper() + name[1::] for name in users['name']]
    return users.sort_values(by= 'user_id')