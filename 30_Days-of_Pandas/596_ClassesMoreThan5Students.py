# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=- 596. Classes More Than 5 Students =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 23 - August - 2023
# Leetcode link = https://leetcode.com/problems/classes-more-than-5-students/description/

# 395ms Beats 5.14%of users with Pandas ; 60.6mb Beats 99.32%of users with Pandas

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    number_students = courses.groupby(['class']).size().reset_index(name = 'count')
    return number_students[number_students['count'] >= 5][['class']]