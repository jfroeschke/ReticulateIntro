

### select rows by value
import pandas

frame_data = {'name': ['James', 'Jason', 'Rogers'], 'age': [18, 20, 22], 'job': ['Assistant', 'Manager', 'Clerk']}

df = pandas.DataFrame(frame_data)

## Select a row based on the value of a variable
df2 = df.loc[df['name'] == 'Jason']

## Select rows by index

dfLoc = df.loc[0]

# Change column type
# The Data type of a column can be changed by using astype() attribute of DataFrame.
# To check the data type of columns, we use the dtypes attribute of DataFrame.

dfType = df.dtypes


# Apply a function to columns/rows

frame_data = {'A': [1, 2, 3], 'B': [18, 20, 22], 'C': [54, 12, 13]}
df = pandas.DataFrame(frame_data)

import numpy as np
dfSQRT = df.apply(np.sqrt)

# Delete a column

dfDrop = df.drop(['A'], axis=1)

#  Delete rows

dfDropRow = df.drop([0])

# You can also delete a range of row as:
dfDropRowS = df.drop(df.index[[0, 1]])

# write to csv
df.to_csv("pandasCSV.csv")
