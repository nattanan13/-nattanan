

import pandas as pd
df = pd.read_csv('Salaries.csv')
df.head()
df.columns


#Quiz 1
# try to read the first 10,10,50 record:
df.head(10)
df.head(20)
df.head(50)

# How to view the last few record:
df.tail(5)

# 1.Group data using rank:
df_rank = df.groupby(['rank'])  

# 2. Calculate mean value for each numeric column per each group:
df_rank.mean()

# 3. Calculate mean salary for each professor rank:
df.groupby('rank')[['salary']].mean()

# 4.Calculate mean salary for each professor rank, sorting:
df.groupby(['rank'], sort = False)[['salary']].mean()

# 5.Create new df as salary >120000:
df_sub = df[ df['salary'] > 120000 ]
df_sub

# 6. Create new df as sex = Female:
df_f = df[ df['sex'] == 'Female']
df_f

# 7. Select column salary
df['salary']

# 8.Select column rank, salary:
df[['rank', 'salary']]

# 9. Select row by their position:
df[10:20]

# 10.Select row by their position[10:20] in colmn rank, sex, and salary:
df_sub.loc[10:20, ['rank', 'sex', 'salary']]

# 11.Select row by their position[10:20] in colmn 0,3, 4, 5:
df_sub.iloc[10:20, [0, 3, 4, 5]]

# 12.Create a new dataframe from the original sorted by the column salary:
df_sorted = df.sort_values( by ='salary')
df_sorted.head()

# 13. Sort the data uing 2 or more column:
df_sorted = df.sort_values( by = ['service', 'salary'], ascending = [True, False])
df_sorted.head(10)


