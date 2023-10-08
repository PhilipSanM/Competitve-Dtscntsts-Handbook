# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=- 2880. Select Data =-=-=-=-==-=-=-=-=-=-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# Introduction to Pandas
# Date: 08 - October - 2023
# Leetcode link = https://leetcode.com/problems/select-data/


import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students["student_id"] == 101][["name", "age"]]
