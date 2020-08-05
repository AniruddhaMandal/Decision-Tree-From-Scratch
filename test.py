import pandas as pd 
import count

data = pd.read_csv("churn.csv")
print(count.best_axis_cut(data,"MonthlyCharges","Churn"))