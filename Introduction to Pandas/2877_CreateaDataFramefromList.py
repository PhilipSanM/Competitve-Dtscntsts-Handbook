# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=- 2877. Create a DataFrame from List =-=-=-=-==-=-=-=-=-=-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# Introduction to Pandas
# Date: 04 - October - 2023
# Leetcode link = https://leetcode.com/problems/create-a-dataframe-from-list/


import pandas as pd


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=["student_id", "age"])
