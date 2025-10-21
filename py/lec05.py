"""
Lecture 5: Data Manipulation with Tables (Pandas)
"""

import numpy as np
import pandas as pd


nba = pd.read_csv("data/nba_salaries.csv")
nba.info()
print("\n")

print("NBA DataFrame:\n", nba.head(5))
print("\n")

nba = nba.rename(columns={"'15-'16 SALARY": "SALARY"})
nba.columns = nba.columns.str.strip().str.lower()
print("NBA DataFrame columns:\n", nba.columns)
print("\n")


nba_sort_by_team = nba.sort_values("team")
print("NBA DataFrame sorted by team:\n", nba_sort_by_team.head(5))
print("\n")

# * rename columns
nba_renamed = nba.rename(columns={"player": "name", "team": "club"})
print("NBA DataFrame with renamed columns:\n", nba_renamed.head(5))
print("\n")

# * Specified Rows
nba_selected = nba.loc[np.arange(20, 25)]
print("NBA DataFrame selected rows:\n", nba_selected)
print("\n")

# * Rows Corresponding to a Specified Feature
condition = nba["salary"] > 10
nba_selected_by_salary = nba[condition]
print("NBA DataFrame selected by salary:\n", nba_selected_by_salary)
print("\n")

condition = nba["team"] == "Golden State Warriors"
nba_selected_by_team = nba[condition]
print("NBA DataFrame selected by team:\n", nba_selected_by_team)
print("\n")

# Fuzzy matching
condition = nba["team"].str.contains("Warriors")
nba_selected_by_team_fuzzy = nba[condition]
print("NBA DataFrame selected by team (fuzzy):\n", nba_selected_by_team_fuzzy)
print("\n")

# Multiple Features
condition = (nba["salary"] > 10) & (nba["team"] == "Golden State Warriors")
nba_selected_multiple = nba[condition]
print("NBA DataFrame selected by multiple conditions:\n", nba_selected_multiple)
print("\n")

condition = (nba["salary"] >= 10) & (nba["salary"] < 10.3)
nba_general = nba[condition]
print("NBA DataFrame selected by general condition:\n", nba_general)
print("\n")

condition = nba["salary"].between(10, 10.3)  # includes the boundaries(10 and 10.3)
nba_between = nba[condition]
print("NBA DataFrame selected by between condition:\n", nba_between)
print("\n")
