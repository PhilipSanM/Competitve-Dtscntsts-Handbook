# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=- 1795. Rearrange Products Table =-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 15 - August - 2023
# Leetcode link = https://leetcode.com/problems/rearrange-products-table/description/

# Runtime: 263ms Beats 98.98%of users with Pandas; Memory: 60.06mb Beats 96.08%of users with Pandas


import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    rearrenged = []
    # Iterating in every row
    for a,row in products.iterrows():
        product_id = row['product_id']
        # Iteration in every store

        for store in ['store1', 'store2', 'store3']:
            price = row[store]
            if pd.notna(price):
                rearrenged.append([product_id, store, price])

        
        

    return pd.DataFrame(rearrenged, columns = ['product_id', 'store', 'price'])