import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import datasets, svm, metrics
from matplotlib import pyplot as plt
df = pd.read_csv('./age_gender_preprocessed.csv')

print('The shape is {}'.format(df.shape))
df['pixels'] = df['pixels'].apply(lambda x: np.array(x.split(), dtype='float32')/255)

'''
For Gender
'''

#Now downsampling the data. First we will store two dfs, each for different gender
df_e1 = df[df['ethnicity'] == 0]
df_e2 = df[df['ethnicity'] == 1]
df_e3 = df[df['ethnicity'] == 2]
df_e4 = df[df['ethnicity'] == 3]
df_e5 = df[df['ethnicity'] == 4]

print('The shape for E1 is {}'.format(df_e1.shape))
print('The shape for E2 is {}'.format(df_e2.shape))
print('The shape for E3 is {}'.format(df_e3.shape))
print('The shape for E4 is {}'.format(df_e4.shape))
print('The shape for E5 is {}'.format(df_e5.shape))

#SVM works great with 2000 records, so we will extract random 1000 records for each gender
df_e1_sampled = df_e1.sample(n=400, random_state=30)
df_e2_sampled = df_e2.sample(n=400, random_state=30)
df_e3_sampled = df_e3.sample(n=400, random_state=30)
df_e4_sampled = df_e4.sample(n=400, random_state=30)
df_e5_sampled = df_e5.sample(n=400, random_state=30)

df_sampled = pd.concat([df_e1_sampled, df_e2_sampled, df_e3_sampled, df_e4_sampled, df_e5_sampled])

print('The shape is {}'.format(df_sampled.shape))

#Now beaking the data into dependent and independent parts
X = np.array(df_sampled['pixels'].tolist())
y = df_sampled['ethnicity']

X_train, X_test, y_train, y_test = train_test_split(X, y)

#classifier
classifier = svm.SVC(gamma=0.01)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print(metrics.classification_report(y_test, y_pred))