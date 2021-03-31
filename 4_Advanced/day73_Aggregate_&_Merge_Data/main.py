import pandas as pd
import matplotlib.pyplot as plt

colors = pd.read_csv('data/colors.csv')

# print(colors.name.nunique())
# print(colors.groupby('is_trans').count())
# print(colors.is_trans.value_counts())

sets = pd.read_csv('data/sets.csv')

# print(sets.head())
# print(sets.tail())
# print(sets.year.min())
# print(sets[sets['year'] == 1949])
# print(sets[sets['year'] == 1949].set_num.nunique())
# print(sets.sort_values('num_parts', ascending=False).head())

sets_by_year = sets.groupby('year').count()
# print(sets_by_year.set_num.head())
# print(sets_by_year.set_num.tail())

# plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
# plt.show()

themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})
themes_by_year.rename(columns={'theme_id':'nr_themes'}, inplace=True)
# print(themes_by_year.head())
# plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])
# plt.show()

# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='g')
# ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color='b')
#
# ax1.set_xlabel('Year')
# ax1.set_ylabel('Number of Sets', color='green')
# ax2.set_ylabel('Number of Themes', color='blue')
#
# plt.show()

parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})
#
# plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])
# plt.show()

themes = pd.read_csv('data/themes.csv')
# print(themes.head())
# print(themes[themes.name == 'Star Wars'])
# print(sets[sets.theme_id == 209])

set_theme_count = sets['theme_id'].value_counts()
# print(set_theme_count[:5])

set_theme_count = pd.DataFrame({'id': set_theme_count.index, 'set_count': set_theme_count.values})
# print(set_theme_count.head())

merged_df = pd.merge(set_theme_count, themes, on='id')
# print(merged_df[:3])

plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)

plt.bar(merged_df.name[:10], merged_df.set_count[:10])
plt.show()

