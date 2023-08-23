# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=-=-=-=-=-=-=-=-= 607. Sales Person =-=--=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 23 - August - 2023
# Leetcode link = https://leetcode.com/problems/sales-person/description/

# There are some bugs on leetcode right now and my RUNTIME is wrong ; Memory 61.2MB Beats 98.86%of users with Pandas


import pandas as pd


def sales_person(
    sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame
) -> pd.DataFrame:
    companies = pd.merge(company, orders, on="com_id")
    not_ids = companies[companies["name"] == "RED"]["sales_id"].unique()

    return sales_person[~sales_person["sales_id"].isin(not_ids)][["name"]]
