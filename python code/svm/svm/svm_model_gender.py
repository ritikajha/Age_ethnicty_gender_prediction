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
df_g1 = df[df['gender'] == 0]
df_g2 = df[df['gender'] == 1]

print('The shape for G1 is {}'.format(df_g1.shape))
print('The shape for G2 is {}'.format(df_g2.shape))

#SVM works great with 2000 records, so we will extract random 1000 records for each gender
df_g1_sampled = df_g1.sample(n=1000, random_state=30)
df_g2_sampled = df_g2.sample(n=1000, random_state=30)

df_sampled = pd.concat([df_g1_sampled, df_g2_sampled])

print('The shape is {}'.format(df_sampled.shape))

#Now beaking the data into dependent and independent parts
X = np.array(df_sampled['pixels'].tolist())
y = df_sampled['gender']

X_train, X_test, y_train, y_test = train_test_split(X, y)

#classifier
classifier = svm.SVC(gamma=0.01)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print(metrics.classification_report(y_test, y_pred))