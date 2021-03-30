import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

#Examine the first 5 rows and the last 5 rows of the of the dataframe
# print(df.head())
# print(df.tail())

#Check how many rows and how many columns there are. What are the dimensions of the dataframe?
# print(df.shape)

#Count the number of entries in each column of the dataframe
# print(df.isna)

#Calculate the total number of post per language.
# print(df.groupby('TAG').sum())

#How many months of data exist per language?
# print(df.groupby('TAG').count())

#fix the date format to make it more readable
df.DATE = pd.to_datetime(df.DATE)
# print(df.head())

#pivot the df DataFrame so that each row is a date and each column is a programming language
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df.fillna(0, inplace=True)
# print(reshaped_df.isna().values.any())

#How many rows and columns does it have? Print out the column names and print out the first 5 rows of the dataframe.
# print(reshaped_df.shape)
# print(reshaped_df.columns)
# print(reshaped_df.head())

#Use the matplotlib documentation to plot a single programming language (e.g., java) on a chart.
# .figure() - allows us to resize our chart
# .xticks() - configures our x-axis
# .yticks() - configures our y-axis
# .xlabel() - add text to the x-axis
# .ylabel() - add text to the y-axis
# .ylim() - allows us to set a lower and upper bound

# plt.figure(figsize=(16,10))
# plt.xticks(fontsize=14)
# plt.yticks(fontsize=14)
# plt.xlabel('Date', fontsize=14)
# plt.ylabel('Number of Posts', fontsize=14)
# plt.ylim(0, 35000)
# plt.plot(reshaped_df.index, reshaped_df.java)

#Show two line (e.g. for Java and Python) on the same chart.
# plt.plot(reshaped_df.index, reshaped_df.python)

# for column in reshaped_df.columns:
#     plt.plot(reshaped_df.index, reshaped_df[column], linewidth=3, label=reshaped_df[column].name)
#
# plt.legend(fontsize=16)

#Smoothing out Time Series Data
roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)

plt.show()
