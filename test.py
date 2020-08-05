import pandas as pd 
import count
data = pd.read_csv("test.csv")

print(count.best_axis_cut(data,"age","coolness"))

