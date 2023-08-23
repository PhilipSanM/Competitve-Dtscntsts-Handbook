# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-586. Customer Placing the Largest Number of Orders =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 23 - August - 2023
# Leetcode link = https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/

# There are some bugs on leetcode right now and my grades are

import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    count_orders = orders.groupby(["customer_number"]).size().reset_index(name="count")
    return count_orders[count_orders["count"] == count_orders["count"].max()][
        ["customer_number"]
    ]
