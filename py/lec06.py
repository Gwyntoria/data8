"""
Lecture 6: More examples of Table Manipulation with Pandas
"""

import pandas as pd
import matplotlib.pyplot as plt


# * Example: US Population Trends

# As of August 2021, this census file is online here:
# data = "http://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2010-2019/nc-est2019-agesex-res.csv"

# The whole description of the table is online here:
# https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2010-2019/nc-est2019-agesex-res.pdf

# Some important information about the table:
# Data fields (in order of appearance):
# VARIABLE                  DESCRIPTION
# SEX                       Sex
# AGE                       Age
# CENSUS2010POP             4/1/2010 resident Census 2010 population
# ESTIMATESBASE2010         4/1/2010 resident population estimates base
# POPESTIMATE2010           7/1/2010 resident population estimate
# POPESTIMATE2011           7/1/2011 resident population estimate
# POPESTIMATE2012           7/1/2012 resident population estimate
# POPESTIMATE2013           7/1/2013 resident population estimate
# POPESTIMATE2014           7/1/2014 resident population estimate
# POPESTIMATE2015           7/1/2015 resident population estimate
# POPESTIMATE2016           7/1/2016 resident population estimate
# POPESTIMATE2017           7/1/2017 resident population estimate
# POPESTIMATE2018           7/1/2018 resident population estimate
# POPESTIMATE2019           7/1/2019 resident population estimate


# The key for SEX is as follows:
# 0 = Total
# 1 = Male
# 2 = Female

# A local copy can be accessed here in case census.gov moves the file:
data = "data/nc-est2019-agesex-res.csv"

full_census_table = pd.read_csv(data)
full_census_table.info()
print("\n")

print("Census DataFrame columns:\n", full_census_table.columns)
print("\n")

print("Census DataFrame:\n", full_census_table.head(5))
print("\n")

# * Data Cleaning

# Remove possible spaces in columns index
full_census_table.columns = full_census_table.columns.str.strip()

# Select a subset of columns to build a new Table(DataFrame)
partial_census_table = full_census_table[
    ["SEX", "AGE", "POPESTIMATE2014", "POPESTIMATE2019"]
]

us_pop = partial_census_table.rename(
    columns={"POPESTIMATE2014": "2014", "POPESTIMATE2019": "2019"}
)
print("US Population DataFrame:\n", us_pop.head(5))
print("\n")

# * Ages 97-100

us_pop_by_age = us_pop[us_pop["SEX"] == 0].drop(columns=["SEX"])
us_pop_97_100 = us_pop_by_age[us_pop_by_age["AGE"].between(97, 100)]
print("US Population DataFrame for ages 97-100:\n", us_pop_97_100)
print("\n")

# * Percent Change

change = us_pop_by_age["2019"] - us_pop_by_age["2014"]
change_percent = (change / us_pop_by_age["2014"]) * 100
us_pop_by_age["CHANGE"] = change
us_pop_by_age["PERCENT_CHANGE"] = change_percent.round(2)
print("US Population DataFrame with Percent Change:\n", us_pop_by_age.head(10))
print("\n")

whole_us_pop_change = us_pop_by_age[us_pop_by_age["AGE"] == 999]
print("Whole US Population Change from 2014 to 2019:\n", whole_us_pop_change)
print("\n")

condition = us_pop_by_age["AGE"] < 999
us_pop_by_change = us_pop_by_age[condition].sort_values(by="CHANGE", ascending=False)
print("US Population DataFrame sorted by Change:\n", us_pop_by_change.head(10))
print("\n")

us_pop_by_percent_change = us_pop_by_age[condition].sort_values(
    by="PERCENT_CHANGE", ascending=False
)
print(
    "US Population DataFrame sorted by Percent Change:\n",
    us_pop_by_percent_change.head(10),
)
print("\n")


# * Example: Sex Ratios

us_pop_2019 = us_pop.drop(columns=["2014"])
all_ages_2019 = us_pop_2019[us_pop_2019["AGE"] == 999]
print("US Population DataFrame for all ages in 2019:\n", all_ages_2019)
print("\n")

pop_2019 = all_ages_2019.loc[all_ages_2019["SEX"] == 0, "2019"].values[0]
all_ages_2019["PROPORTION"] = all_ages_2019["2019"] / pop_2019 * 100
print("US Population DataFrame with Proportion in 2019:\n", all_ages_2019)
print("\n")

# * Proportions Among Infants

infants = us_pop_2019[us_pop_2019["AGE"] == 0]
print("US Population DataFrame for infants in 2019:\n", infants)
print("\n")

infants_2019 = infants["2019"].values[0]
infants["PROPORTION"] = infants["2019"] / infants_2019 * 100
print("US Population DataFrame for infants with Proportion in 2019:\n", infants)
print("\n")

# * Sex Ratio at Each Age

females_all_rows = us_pop_2019[us_pop_2019["SEX"] == 2]
females = females_all_rows[females_all_rows["AGE"] != 999]
print("US Population DataFrame for females in 2019:\n", females)
print("\n")

males_all_rows = us_pop_2019[us_pop_2019["SEX"] == 1]
males = males_all_rows[males_all_rows["AGE"] != 999]
print("US Population DataFrame for males in 2019:\n", males)
print("\n")

ratios = pd.DataFrame(
    {
        "AGE": females["AGE"],
        "2019_F:M_RATIO": females["2019"].values / males["2019"].values,
    }
)
print("US Population DataFrame for Sex Ratios in 2019:\n", ratios)
print("\n")

print(
    "US Population DataFrame for Sex Ratios in 2019 (Ages 76+):\n",
    ratios[ratios["AGE"] > 75],
)
print("\n")

print("Male population (ages 92, 93,99):\n", males[males["AGE"].isin([92, 93, 99])])
print("\n")

print(
    "Female population (ages 92, 93,99):\n", females[females["AGE"].isin([92, 93, 99])]
)
print("\n")

# * Plotting
plt.plot(ratios["AGE"], ratios["2019_F:M_RATIO"], color="blue")
plt.title("Female to Male Ratios by Age in US (2019)")
plt.xlabel("Age")
plt.ylabel("Female to Male Ratio")
plt.ylim(0, 3.5)
plt.xlim(0, 100)
plt.grid(True)
plt.tight_layout()
plt.ion()
plt.show()
plt.pause(5)  # Pause to view the plot for 5 seconds
plt.close()  # Close the plot
