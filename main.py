from sklearn import datasets         # To create dummy dataset
from sklearn.cluster import KMeans
from sklearn_extra.cluster import KMedoids
from sklearn.mixture import GaussianMixture
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')    # To get rid of warning messages


# Remove scientific notations and display numbers with 2 decimal points instead
pd.options.display.float_format = '{:,.2f}'.format

# Update default background style of plots
sns.set_style(style='darkgrid')

np.random.seed(1)   # Setting the seed to get reproducible results

conc_circles = datasets.make_circles(n_samples=2000, factor=.5, noise=.05)
X, y = conc_circles         # Separating the features and the labels
df = pd.DataFrame(X)

df.columns = ['X1', 'X2']

df['Y'] = y
df
# Scatter plot of original lables
sns.scatterplot(x='X1', y='X2', data=df, hue='Y')

plt.show()

X = StandardScaler().fit_transform(X)

kmeans = KMeans(n_clusters=2, random_state=12)

kmeans.fit(X)

df['KmeansLabels'] = kmeans.predict(X)

sns.scatterplot(x='X1', y='X2', data=df, hue='KmeansLabels')

plt.show()