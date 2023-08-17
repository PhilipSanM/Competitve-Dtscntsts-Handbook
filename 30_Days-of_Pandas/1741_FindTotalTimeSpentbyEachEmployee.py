# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--1741. Find Total Time Spent by Each Employee =-=-=-=-=-=-=-=-=-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 17 - August - 2023
# Leetcode link = https://leetcode.com/problems/find-total-time-spent-by-each-employee/description/

# 306ms Beats 89.68%of users with Pandas ; 61.65mb Beats 77.83%of users with Pandas


import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']

    employees = employees.groupby(['event_day','emp_id'])['total_time'].sum().reset_index()
    employees.rename({'event_day': 'day'}, axis = 1, inplace = True)
    return employees

