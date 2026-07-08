import pandas as pd
pd.read_csv(
    "movie_titles_metadata.tsv",
    sep="\t",
    names=['sno', 'name', 'release_year', 'rating', 'votes', 'genres']
)

# code for reading a CSV file from a URL with custom headers

# import requests
from io import StringIO

url = "https://example.com/data.csv"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# response = requests.get(url, headers=headers)

# df = pd.read_csv(StringIO(response.text))


# removes the default pandas index column when reading a CSV filea and sets the first column as the index
# Make a column the DataFrame index
df = pd.read_csv("file.csv", index_col="id")

# Using column position
df = pd.read_csv("file.csv", index_col=0)

# for headers
# First row is header (default)
pd.read_csv("file.csv")

# Second row is header
pd.read_csv("file.csv", header=1)

# No header in file
pd.read_csv("file.csv", header=None)


# reading sleectedc olumn an importing htem only
# By column names
pd.read_csv("file.csv",
            usecols=["name", "age"])

# By column positions
pd.read_csv("file.csv",
            usecols=[0, 2])


# skippign rows
# Skip first 5 rows
pd.read_csv("file.csv", skiprows=5)

# Skip specific rows
pd.read_csv("file.csv", skiprows=[0, 3, 5])

# Skip rows using a condition (advanced)
pd.read_csv("file.csv", skiprows=lambda x: x % 2 == 0)


# skip bad rows
import pandas as pd

df = pd.read_csv(
    "students.csv",
    on_bad_lines="skip"
)


# changing  th data type of a column while reading a CSV file
df = pd.read_csv(
    "users.csv",
    dtype={"phone": str}
)

# handling dates which are by default strings
df = pd.read_csv(
    "sales.csv",
    parse_dates=["Date"]
)


# changing  th data type of a column while reading a CSV file
df = pd.read_csv(
    "users.csv",
    dtype={"phone": str}
)

# handling dates which are by default strings
df = pd.read_csv(
    "sales.csv",
    parse_dates=["Date"]
)

# renaming
df["team1"] = df["team1"].replace({
    "Royal Challengers Bangalore": "RCB"
})


# nan values
df = pd.read_csv(
    "students.csv",
    na_values=["?", "Missing"]
) 
# where there is ? and missing it will be replaced by NaN values

# chunk size
for chunk in pd.read_csv(
    "sales.csv",
    chunksize=50000
):
    print(chunk["Sales"].sum())
