# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=- 177. Nth Highest Salary -=-=-=-=-=-==-=-=-=-=-=-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Medium


# 30 Days of Pandas Challenge
# Date: 10 - August - 2023
# Leetcode link = https://leetcode.com/problems/nth-highest-salary/description/
# Runtime 251 ms Beats 53.41% ; Memory 60.1MB Beats 89.20%

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates()

    if N > len(unique_salaries):
        return pd.DataFrame({'Nth Highest Salary': [None]})
    else:
        nth = unique_salaries.sort_values(ascending=False).iloc[N-1]
        

        return pd.DataFrame({'Nth Highest Salary': [nth]})