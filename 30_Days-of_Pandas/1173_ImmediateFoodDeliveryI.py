# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=- 1173. Immediate Food Delivery I -=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 16 - August - 2023
# Leetcode link = https://leetcode.com/problems/immediate-food-delivery-i/description/

# Runtime 252 ms Beats 95.77% ; Memory 61.14 MB Beats 88.87%

import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    # immediate_orders = delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']]
    # total_orders = len(delivery['order_date'])
    immediate_orders = delivery['order_date'] == delivery['customer_pref_delivery_date'] # True/False series
    total_orders = len(delivery)
    total_immeadite = immediate_orders.sum()
    porcentage = round(total_immeadite/total_orders * 100, 2)
    return pd.DataFrame({'immediate_percentage': [porcentage]})