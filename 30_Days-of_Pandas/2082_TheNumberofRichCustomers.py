# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=- 2082. The Number of Rich Customers =-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 16 - August - 2023
# Leetcode link = https://leetcode.com/problems/the-number-of-rich-customers/description/

# Runtime: 235ms Beats 92.62%of users with Pandas; Memory: 60.44mb Beats 92.72%of users with Pandas

import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    rich_customers = store[store['amount'] > 500]
    # rich_customers = set(rich_customers['customer_id'])
    # count = len(rich_customers)
    count = rich_customers['customer_id'].nunique()
    return pd.DataFrame({'rich_count':[count]})
