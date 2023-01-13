import pandas as pd
df = pd.read_csv("Virat_Kohli.csv")
# print(df.head(10))
# print(df.tail(10))
# df.info()
# print(df.shape)
# print(df.describe())
# print(df["Opposition"].describe())
# run_frequency = df["Opposition"].value_counts()
# print(run_frequency)
# new_df = df[["Runs", "SR", "Opposition"]]
# print(new_df)

# vs_aussie = df[df["Opposition"] == "v Australia"]
# print(vs_aussie)
# -----------
#find all the matches where virat scored century

# century = df[df["Runs"] >= 100]
# print(century)
# --------------
# find all the matches where virat strike rate was >100

# strike_rate = df[df["SR"] > 100]
# print(strike_rate)
# ------------
# find all the matches where virat played with srilanka and scored century

# vs_srilanka = df[(df["Opposition"] == "v Sri Lanka") & (df["Runs"] >= 100)]
# print(vs_srilanka)

def find_centuries(x):
    if x>=100:
        return "OG"
    else:
        return "NOOB"
        
df["Centuries"] = df["Runs"].apply(find_centuries)

print(df.tail(10))