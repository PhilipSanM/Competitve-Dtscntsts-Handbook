# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=- 183. Customers Who Never Order =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 07 - August - 2023
# Leetcode link = https://leetcode.com/problems/customers-who-never-order/

# 253ms Beats 75.63%of users with Pandas ; 61.26mb Beats 37.64%of users with Pandas

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    buyers = orders['customerId'].unique()
    return customers[~customers['id'].isin(buyers)][['name']].rename(columns={'name': 'Customers'})