# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=- 1907. Count Salary Categories =-=-=-=-=-=-=-=-=-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Medium


# 30 Days of Pandas Challenge
# Date: 16 - August - 2023
# Leetcode link = https://leetcode.com/problems/count-salary-categories/description

# Runtime 303 ms Beats 90.02% ; Memory 83.90 MB Beats 83.14%
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_valid = accounts['income'] < 20000
    average_valid = (accounts['income'] >= 20000) & (accounts['income'] <= 50000)
    high_valid = accounts['income'] > 50000
    
    low_total = low_valid.sum()
    average_total = average_valid.sum()
    high_total = high_valid.sum()
 
    return pd.DataFrame({'category': ["Low Salary", 'Average Salary', 'High Salary'], 'accounts_count': [low_total, average_total, high_total]})