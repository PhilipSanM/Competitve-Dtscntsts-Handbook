# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-= 1757. Recyclable and Low Fat Products =-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 05 - August - 2023
# Leetcode link = https://leetcode.com/problems/recyclable-and-low-fat-products/description

# 270ms Beats 66.33%of users with Pandas ; 60.2mb Beats 93.93% of users with Pandas

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products["low_fats"] == 'Y') & (products["recyclable"] == 'Y')][["product_id"]]