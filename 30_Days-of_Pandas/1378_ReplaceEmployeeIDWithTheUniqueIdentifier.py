# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=-1378. Replace Employee ID With The Unique Identifier -=-=-=-=-=-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 23 - August - 2023
# Leetcode link = https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/

# There are some bugs on leetcode right now and my RUNTIME is wrong ; Memory 61.50MB Beats 78.41%of users with Pandas

import pandas as pd


def replace_employee_id(
    employees: pd.DataFrame, employee_uni: pd.DataFrame
) -> pd.DataFrame:
    uniques_id = pd.merge(employees, employee_uni, on="id", how="left")
    return uniques_id[["unique_id", "name"]]
