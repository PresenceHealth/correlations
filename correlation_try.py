import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline


xls = pd.ExcelFile('HealthViz County Dataset 6.19.17.xlsx')
df = xls.parse('HealthViz County Dataset 6.19.1', skiprows=1, index_col=0, na_values=['NA'])
corr = df.corr()
sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values)

def m(x, w):
    """Weighted Mean"""
    return np.sum(x * w) / np.sum(w)

def cov(x, y, w):
    """Weighted Covariance"""
    return np.sum(w * (x - m(x, w)) * (y - m(y, w))) / np.sum(w)

def corr(x, y, w):
    """Weighted Correlation"""
    return cov(x, y, w) / np.sqrt(cov(x, x, w) * cov(y, y, w))

xs = list(df.columns)[2:28]
ys = list(df.columns)[28:-1]

l = []
d = {}
for y in ys:
    for x in xs:
        c = corr(df[x], df[y], df['w'])
        l.append(c)
    d[y] = l
    l = []

ddf = pd.DataFrame.from_dict(d)
sns.heatmap(ddf)