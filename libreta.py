import numpy as np
import pandas as pd
data = np.random.rand(5, 5)
dataframe = pd.DataFrame(data)
print(dataframe)
new_dataframe = dataframe.copy()
years = [2022]
new_dataframe.insert(0, "Year", years)
print(new_dataframe)