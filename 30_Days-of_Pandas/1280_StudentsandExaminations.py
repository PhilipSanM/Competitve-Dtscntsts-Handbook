# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=-1280. Students and Examinations -=-=-=-=-=-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 23 - August - 2023
# Leetcode link = https://leetcode.com/problems/students-and-examinations/description/

# There are some bugs on leetcode right now and my RUNTIME is wrong ; Memory 61.05MB Beats 98.53%of users with Pandas


import pandas as pd


def students_and_examinations(
    students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame
) -> pd.DataFrame:
    attendes = (
        examinations.groupby(["student_id", "subject_name"])
        .size()
        .reset_index(name="attended_exams")
    )
    classmates = pd.merge(students, subjects, how="cross")

    attendes_students = pd.merge(
        classmates, attendes, on=["student_id", "subject_name"], how="left"
    )

    # Cleaning data
    attendes_students["attended_exams"] = (
        attendes_students["attended_exams"].fillna(0).astype(int)
    )

    # reordering
    attendes_students = attendes_students.sort_values(by=["student_id", "subject_name"])

    return attendes_students[
        ["student_id", "student_name", "subject_name", "attended_exams"]
    ]
