import pandas as pd

data = {
    "apples":[4,3,6,1],
    "oranges":[3,7,4,1]
}
index_title = [
    "Arron", "james", "shaun", "stark"
]
df = pd.DataFrame(data, index = index_title)
print(df["oranges"].iloc[0:],"\n")
print(df,"\n")
print(df.loc["Arron"])