
# search internship 
# python
# data analyst
# data scientist


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Virat_Kohli.csv")
# print(df)
# --------------------------------

# number of matches he has played at different position
# print(df["Pos"].head(10))
positions = df["Pos"].unique()
# print(positions)
df["Pos"] = df["Pos"].map({
    3.0: "Batting at 3",
    4.0: "Batting at 4",
    2.0: "Batting at 2",
    1.0: "Batting at 1",
    5.0: "Batting at 5",
    6.0: "Batting at 6",
    7.0: "Batting at 7"
})
# print(df[["Runs","Pos"]])
pos_counts = df["Pos"].value_counts()
# print(pos_counts)
# print(type(pos_counts))
# ------------------------
# total runs scored in different position 
pos_counts_values = pos_counts.values
pos_counts_labels = pos_counts.index
fig = plt.figure(figsize=(8, 7))
plt.pie(pos_counts_values, labels=pos_counts_labels)

# plt.show()
# ---------------------------------------------------------



# number of matches he has played with different countries
def show_pie_plots(df, key):
    counts = df[key].value_counts()
    count_values = counts.values
    count_labels = counts.index
    fig = plt.figure(figsize=(8,7))
    plt.pie(count_values, labels = count_labels)
    # plt.show()
# show_pie_plots(df,"Opposition")

# number of matches he has played with different grounds

# show_pie_plots(df, "Ground")
# total sixes in different position

runs_at_pos = df.groupby("Pos")["6s"].sum()
print(runs_at_pos, type(runs_at_pos))
runs_at_pos_values = runs_at_pos.values
runs_at_pos_labels = runs_at_pos.index
fig = plt.figure(figsize=(10,7))
plt.bar(
    runs_at_pos_labels,
    runs_at_pos_values,
    color="green",
    width=0.3)

# plt.show()

# total runs scored with different countries
runs_at_pos = df.groupby("Opposition")["Runs"].sum()
print(runs_at_pos, type(runs_at_pos))
runs_at_pos_values = runs_at_pos.values
runs_at_pos_labels = runs_at_pos.index
fig = plt.figure(figsize=(16,7))
plt.bar(
    runs_at_pos_labels,
    runs_at_pos_values,
    color="green",
    width=0.3)

# plt.show()
# no. of centuries scored in 1st innings
centuries = df.query("Runs >=100")
# print(centuries)

innings = centuries["Inns"].value_counts
innings_values = innings.values
innings_labels = innings.index
fig = plt.figure(figsize=(14,7))

plt.pie(innings.values, labels= innings.index)
# tons = centuries["Runs"]
# plt.bar(innings, tons, width=0.4)
plt.show()


# calculate the dismissals of kohli


# against which team he scored most runs



# against which team he scored most centuries


# runs scored by him as sixes and fours

