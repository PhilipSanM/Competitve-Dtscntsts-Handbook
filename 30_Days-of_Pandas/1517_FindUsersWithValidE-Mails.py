# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=- 1517. Find Users With Valid E-Mails =-=-=-=-=-=-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 10 - August - 2023
# Leetcode link = https://leetcode.com/problems/find-users-with-valid-e-mails/description/

# Runtime 253 ms Beats 89.5% ; Memory 61.5 MB Beats 14.8%

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users['mail'].str.contains(r"^[a-zA-Z][a-zA-Z0-9_.-]*\@leetcode\.com$")]