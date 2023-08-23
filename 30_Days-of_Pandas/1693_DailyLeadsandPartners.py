# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-1693. Daily Leads and Partners =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 23 - August - 2023
# Leetcode link = https://leetcode.com/problems/daily-leads-and-partners/description/

# There are some bugs on leetcode right now and my RUNTIME is wrong ; Memory 62MB Beats 50.78%of users with Pandas

import pandas as pd


def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    uniques_sales = (
        daily_sales.groupby(["date_id", "make_name"]).nunique().reset_index()
    )
    uniques_sales.rename(
        columns={"lead_id": "unique_leads", "partner_id": "unique_partners"},
        inplace=True,
    )
    return uniques_sales
