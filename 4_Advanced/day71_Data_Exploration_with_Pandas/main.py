import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')
clean_df = df.dropna()

#Some testing / cleaning
# print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.isna)
# print(df.tail())
# print(clean_df.tail())

#Find College Major with Highest Starting Salaries
# max_salary_value = clean_df['Starting Median Salary'].max()
# print(max_salary_value)
#
# max_salary_idx = clean_df['Starting Median Salary'].idxmax()
# print(max_salary_idx)
#
# max_salary_major = clean_df['Undergraduate Major'].loc[max_salary_idx]
# max_salary_major_2 = clean_df['Undergraduate Major'][max_salary_idx]
# print(max_salary_major)
# print(max_salary_major_2)

#What college major has the highest mid-career salary?
# max_salary_value = clean_df['Mid-Career Median Salary'].max()
# print(max_salary_value)

# max_salary_idx = clean_df['Mid-Career Median Salary'].idxmax()
# print(max_salary_idx)

# max_salary_major = clean_df['Undergraduate Major'][max_salary_idx]
# print(max_salary_major)

#Which college major has the lowest starting salary and how much do graduates earn after university?
# min_salary_value = clean_df['Starting Median Salary'].min()
# print(min_salary_value)
#
# min_salary_idx = clean_df['Starting Median Salary'].idxmin()
# print(min_salary_idx)
#
# min_salary_major = clean_df['Undergraduate Major'][min_salary_idx]
# print(min_salary_major)

#Which college major has the lowest mid-career salary?
# min_salary_value = clean_df['Mid-Career Median Salary'].min()
# print(min_salary_value)
#
# min_salary_idx = clean_df['Mid-Career Median Salary'].idxmin()
# print(min_salary_idx)
#
# min_salary_major = clean_df['Undergraduate Major'][min_salary_idx]
# print(min_salary_major)

#Lowest Risk Majors
# spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
# clean_df.insert(1, 'Spread', spread_col)
# # print(clean_df.head())
# low_risk = clean_df.sort_values('Spread')
# print(low_risk[['Undergraduate Major', 'Spread']].head())

#find the degrees with the highest potential?
# high_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary')
# print(high_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].tail())

# highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
# print(highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())

#degrees with the greatest spread in salaries
# spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
# clean_df.insert(1, 'Spread', spread_col)
#
# high_risk = clean_df.sort_values('Spread')
# print(high_risk[['Undergraduate Major', 'Spread']].tail())

#Grouping and Pivoting Data with Pandas
print(clean_df.groupby('Group').count())
pd.options.display.float_format = '{:,.2f}'.format
print(clean_df.groupby('Group').mean())




