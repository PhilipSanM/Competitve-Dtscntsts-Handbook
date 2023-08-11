# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=- 176. Second Highest Salary =-=-=-=-==-=-=-=-=-=-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Medium


# 30 Days of Pandas Challenge
# Date: 11 - August - 2023
# Leetcode link = https://leetcode.com/problems/second-highest-salary/description/
# Runtime 223ms Beats 86.26%of users with Pandas ; Memory 60.48mb Beats 77.83%of users with Pandas

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates()
    
    if 2 > len(unique_salaries):
        return pd.DataFrame({'SecondHighestSalary': [None]})
    else:
        first = max(unique_salaries)
        index = unique_salaries[unique_salaries == first].index[0]
        unique_salaries = unique_salaries.drop(index)
        second = max(unique_salaries)
        return pd.DataFrame({'SecondHighestSalary': [second]})