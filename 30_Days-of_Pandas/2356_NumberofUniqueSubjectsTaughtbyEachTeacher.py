# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-2356. Number of Unique Subjects Taught by Each Teacher =-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 21 - August - 2023
# Leetcode link = https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/description

# Runtime: 243ms Beats 96.78%of users with Pandas; Memory: 61.6mb Beats 64.95%of users with Pandas

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    unique_teachers = teacher.groupby(['teacher_id'])['subject_id'].nunique().reset_index()
    unique_teachers.rename(columns = {'subject_id': 'cnt'}, inplace = True)
    return unique_teachers