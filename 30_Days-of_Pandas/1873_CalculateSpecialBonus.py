# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-= 1873. Calculate Special Bonus -=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 08 - August - 2023
# Leetcode link = https://leetcode.com/problems/calculate-special-bonus/description/

# 264ms Beats 95.92%of users with Pandas ; 61.22mb Beats 58.88%of users with Pandas

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda row: row['salary'] if row['employee_id'] % 2 == 1 and not row['name'].startswith('M') else 0,
    axis = 1)

    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')