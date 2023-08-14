# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=- 196. Delete Duplicate Emailss =-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 14 - August - 2023
# Leetcode link = https://leetcode.com/problems/delete-duplicate-emails/description/

# Runtime: 252ms Beats 66.17%of users with Pandas; Memory: 60.45mb Beats 93.75%of users with Pandas

import pandas as pd

# Modify Person in place
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by = 'id', inplace = True)
    person.drop_duplicates(subset = 'email', keep='first', inplace = True)
