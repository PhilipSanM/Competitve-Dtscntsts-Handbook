# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-=-=- 1527. Patients With a Condition =-=-=-=-=-=-=-=-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Easy


# 30 Days of Pandas Challenge
# Date: 09 - August - 2023
# Leetcode link = https://leetcode.com/problems/patients-with-a-condition/description/

# 220ms Beats 95.89%of users with Pandas ; 60.35mb Beats 95.89%of users with Pandas

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    patiens_with_IDiabetes = patients[patients['conditions'].str.contains(r'\bDIAB1')]
    return patiens_with_IDiabetes