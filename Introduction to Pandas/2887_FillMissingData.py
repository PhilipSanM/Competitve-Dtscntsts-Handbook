# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-2887. Fill Missing Data =-=-=-=-==-=-=-=-=-=-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# Introduction to Pandas
# Date: 29 - October - 2023
# Leetcode link = https://leetcode.com/problems/fill-missing-data/description/

import pandas as pd


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    # students['grade'] = students['grade'].astype(int)
    students = students.astype({"grade": int})

    return students
