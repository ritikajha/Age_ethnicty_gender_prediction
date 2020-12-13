import numpy as np
import pandas as pd

df = pd.read_csv('../dataset/age_gender.csv')

print(df.pixels.nunique())
#Finding no. of null values
print(df.pixels.isnull().sum())
#Finding repaeted rows
df_repeated = df.groupby('pixels').filter(lambda x: len(x) > 1)
print(df_repeated.head())

#FInding the no of unique rows that are repeated
print(len(df_repeated.groupby(['pixels'])))
print(len(df_repeated.groupby(['pixels', 'age', 'ethnicity', 'gender'])))

#Since there is an abnormality & confusion n the data lebels as seen by printing the values, we choose to drop the repeated rows = 765 directly. So are choosing 22940 rows for our model.
df_final = df.groupby('pixels').filter(lambda x: len(x) == 1)

#Converting pixels to array of pixels
df_final['pixels'] = df_final['pixels'].apply(lambda x: np.array(x.split(), dtype="float32"))

#printing rows and colums
print(df.shape)

# normalizing pixels data
df_final['pixels'] = df_final['pixels'].apply(lambda x: x/255)

#COnverting to list
X = np.array(df_final['pixels'].tolist())

# Converting pixels from 1D to 3D
X = X.reshape(X.shape[0],48,48,1)
print(X[0])