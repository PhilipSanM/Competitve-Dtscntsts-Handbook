# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=-=-= 570. Managers with at Least 5 Direct Reports =-=--=-=-=-=-=-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 23 - August - 2023
# Leetcode link = https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/

# There are some bugs on leetcode right now and my RUNTIME is wrong ; Memory 61.74MB Beats 89.62%of users with Pandas

import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    reports = employee.groupby(["managerId"]).size().reset_index(name="cnt")
    managers = pd.merge(
        employee, reports, left_on="id", right_on="managerId", how="left"
    )

    return managers[managers["cnt"] >= 5][["name"]]
