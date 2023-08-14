
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=- 184. Department Highest Salary =-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Medium


# 30 Days of Pandas Challenge
# Date: 14 - August - 2023
# Leetcode link = https://leetcode.com/problems/department-highest-salary/description/

# Runtime: 334ms Beats 49.75%of users with Pandas; Memory: 62.71mb Beats 33.81%of users with Pandas

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    department = department.rename(columns = {'name' : 'Department'})
    employee = employee.rename(columns= {'name': 'Employee', 'salary' : 'Salary'})
    merged = employee.merge(department, left_on = 'departmentId', right_on = 'id', how= 'left')
    highest = merged.groupby('Department').apply(lambda x: x[x['Salary'] == x['Salary'].max()])
    
    return highest[['Department', 'Employee', 'Salary']]