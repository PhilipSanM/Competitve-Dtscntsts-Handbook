# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-2886. Change Data Type\ =-=-=-=-==-=-=-=-=-=-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# Introduction to Pandas
# Date: 29 - October - 2023
# Leetcode link = https://leetcode.com/problems/change-data-type/description/

import pandas as pd


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    # students['grade'] = students['grade'].astype(int)
    students = students.astype({"grade": int})

    return students
