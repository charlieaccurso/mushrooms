import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# import codecademylib3

print("In this project, I analyze an extensive mushroom dataset from UCI using bar charts.")
print('\n')

# load in the data
df = pd.read_csv("mushroom_data.csv")
print("Below is the data head:")
print(df.head())

print("The file mushroom_data.csv contains 23 categorical variables; all the variables can be effectively represented using bar charts.")
print('\n')

# list of all column headers
columns = df.columns.tolist()

for column in columns:
  # print(column)
  sns.countplot(
    df[column],
    order=df[column].value_counts().index)
  # rotate value labels and increase font size
  plt.xticks(rotation=30, fontsize=10)
  # increase variable label font size
  plt.xlabel(column, fontsize=12)
  plt.title("{} Value Counts".format(column))
  plt.show()
  plt.clf()

print("Some variables have an obvious mode, such as Odor (None), Gill Attachment (Free), Gill Spacing (Close), Gill Size (Broad), Stalk Shape (Tapering), etc.")
print("Some variables have a diverse array of values, such as Cap Color (9 values), Odor (9 values), Gill Color (12 values), Stalk Color Above Ring (9 values), etc.")
print("The habitat in which mushrooms are most likely found is Woods.")
print('\n')
print("Additional notable observations include:")
print("There is a roughly equal split between mushrooms that are edible vs. poisonous.")
print("The vast majority of Cap Shapes are convex or flat. Other shapes such as knobbed or bell are uncommon.")
print("Uncommon Cap Colors include buff, pink, cinnamon, purple, and green.")
print("A majority of mushrooms in the dataset do not bruise.")
print("Gill Color is most often buff, pink, white, or brown. Rarer colors include red, yellow, orange, and green.")
print("All mushrooms in the dataset are partially veiled. Veil Color is almost entirely white.")
print("Most mushrooms have one ring, very few have two, and almost none have no rings.")
print("The vast majority of Spore Print Colors are white, brown, black, or chocolate. All other colors, such as green, buff, and purple, are rare.")
print("The least common mushroom Habitats are urban, meadows, and waste.")
