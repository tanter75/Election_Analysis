import pandas as pd
import numpy as np
df = pd.read_csv("Resources/election_results_new.csv")
print(df.info())
print(df["County"].value_counts())
