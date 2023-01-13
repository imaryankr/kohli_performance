import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Virat_Kohli.csv")

# Total no. of runs kohli has scored

score = np.sum(df["Runs"])
print(score)

# find out the total no. of balls has faced by kohli

balls = df["BF"].sum()
print(balls)
# find out the avg sr of kohli

sr = df["SR"].mean()
print(sr)