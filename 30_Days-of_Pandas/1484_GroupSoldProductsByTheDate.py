# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-1484. Group Sold Products By The Date =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 23 - August - 2023
# Leetcode link = https://leetcode.com/problems/group-sold-products-by-the-date/description/

# There are some bugs on leetcode right now and my RUNTIME is wrong ; Memory 61.10MB Beats 99.53%of users with Pandas

import pandas as pd


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    # if empty
    if activities.empty:
        return pd.DataFrame({"sell_date": [], "num_sold": [], "products": []})

    # Using agregation: agg() in a groupbyObject
    sold_products = activities.groupby(["sell_date"])

    sold_products = sold_products.agg(
        num_sold=("product", "nunique"),
        products=("product", lambda x: ",".join(sorted(set(x)))),
    ).reset_index()

    return sold_products
