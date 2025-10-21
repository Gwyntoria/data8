import pandas as pd


cones = pd.DataFrame(
    {
        "Flavor": [
            "strawberry",
            "chocolate",
            "chocolate",
            "strawberry",
            "chocolate",
            "bubblegum",
        ],
        "Color": [
            "pink",
            "light brown",
            "light brown",
            "pink",
            "dark brown",
            "pink",
        ],
        "Price": [
            3.55,
            4.75,
            5.25,
            5.25,
            5.25,
            4.75,
        ],
    }
)

print("Cones DataFrame:\n", cones.head())  # Display the first 5 rows of the DataFrame
print("\n")

# column selection
print("Columns:\n", cones.columns)
print("\n")
print("Flavor column:\n", cones["Flavor"])
print("\n")
print(
    "Flavor and Color columns:\n", cones[["Flavor", "Color"]]
)  # double brackets returns a DataFrame
print("\n")

droped = cones.drop(columns=["Price"])
print("DataFrame after dropping Price column:\n", droped)
print("\n")

print("Original DataFrame remains unchanged:\n", cones)

sorted_by_price = cones.sort_values(by="Price")
print("\nDataFrame sorted by Price:\n", sorted_by_price)
print("\n")

sorted_by_price = cones.sort_values(by="Price", ascending=False)
print("\nDataFrame sorted by Price:\n", sorted_by_price)
print("\n")

# row selection
print("First row using iloc:\n", cones.iloc[0])
print("\n")
print("First three rows using iloc:\n", cones.iloc[0:3])
print("\n")
print("Rows where Flavor is 'chocolate':\n", cones[cones["Flavor"] == "chocolate"])
print("\n")
print("Rows where Price > 5:\n", cones[cones["Price"] > 5])  # boolean indexing
print("\n")
print(
    "Rows where Flavor is 'chocolate' and Price > 5:\n",
    cones[(cones["Flavor"] == "chocolate") & (cones["Price"] > 5)],
)
print("\n")

# * Example: Salaries in the NBA

nba = pd.read_csv("data/nba_salaries.csv")
nba.info()
print("\n")

nba = nba.rename(columns={"'15-'16 SALARY": "SALARY"})
nba.columns = nba.columns.str.strip().str.lower()
print("NBA columns after converting to lowercase:\n", nba.columns)
print("\n")

# Multiple rows and columns selection
salary_20 = nba.loc[nba["salary"] > 20]
print("Players with salary > 20 million:\n", salary_20)
print("\n")

# Multiple conditions
high_salary_sf = nba.loc[(nba["salary"] > 20) & (nba["position"] == "SF")]
print("Small Forwards with salary > 20 million:\n", high_salary_sf)
print("\n")

# Selecting specific columns
high_salary_sf_names = nba.loc[
    (nba["salary"] > 20) & (nba["position"] == "SF"), "player"
]
print("Names of Small Forwards with salary > 20 million:\n", high_salary_sf_names)
print("\n")

warriors = nba.loc[nba["team"] == "Golden State Warriors"]
print("Golden State Warriors players:\n", warriors)
print("\n")

warriors.sort_values(by="salary", ascending=True, inplace=True)
print("Warriors sorted by salary (ascending):\n", warriors)
print("\n")
