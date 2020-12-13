import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import datasets, svm, metrics
from matplotlib import pyplot as plt
from sklearn.svm import SVR
from sklearn.utils import shuffle

df = pd.read_csv('./age_gender_preprocessed.csv')

print('The shape is {}'.format(df.shape))
df['pixels'] = df['pixels'].apply(lambda x: np.array(x.split(), dtype='float32')/255)

'''
For Age
'''
df_a1 = df[df['age'] < 10]
df_a2 = df[(df['age'] >= 10) & (df['age'] < 25)]
df_a3 = df[(df['age'] >= 25) & (df['age'] < 40)]
df_a4 = df[(df['age'] >= 40) & (df['age'] < 55)]
df_a5 = df[(df['age'] >= 55)]

print(df_a1.shape)
print(df_a2.shape)
print(df_a3.shape)
print(df_a4.shape)
print(df_a5.shape)

#SVM works great with 2000 records,
df_a1_sampled = df_a1.sample(n=400, random_state=30)
df_a2_sampled = df_a2.sample(n=400, random_state=30)
df_a3_sampled = df_a3.sample(n=400, random_state=30)
df_a4_sampled = df_a4.sample(n=400, random_state=30)
df_a5_sampled = df_a5.sample(n=400, random_state=30)


df_sampled = pd.concat([df_a1_sampled, df_a2_sampled, df_a3_sampled, df_a4_sampled, df_a5_sampled])
df_sampled = shuffle(df_sampled)

print('The shape is {}'.format(df_sampled.shape))

#Now beaking the data into dependent and independent parts
X = np.array(df_sampled['pixels'].tolist())
y = df_sampled['age']

X_train, X_test, y_train, y_test = train_test_split(X, y)

#classifier
classifier = SVR(gamma=0.01)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

print(y_pred)
print(metrics.mean_absolute_error(y_test, y_pred))