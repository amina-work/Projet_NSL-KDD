import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("KDDtrain.csv", header=None)
print(df.head())

# *********** CHECK IF DATA HAVE NULL VALUES ***********
print(df.isnull().any())

# *********** LES VALEURS ABBERANTS ***********
df.plot()