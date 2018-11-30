#!/usr/bin/env python3

"""
Usage: ./clusters.py expression_file
This code uses hierarchical clustering to generate a heatmap of differential expression, and a plot of clusters
based on kmeans.
"""

import sys
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans

df = pd.read_csv(sys.argv[1], sep="\t", index_col="gene")
df2 = df[['CFU', 'poly']]
df3 = np.array(df2)

fig = sns.clustermap(df)
fig.savefig("heatmap.png")
#plt.show()

kmeans = KMeans(n_clusters=4)
kmeans.fit(df3)
# print(kmeans.cluster_centers_)
y_km = kmeans.fit_predict(df3)
#gene in cluster 3
cluster = y_km[3]
genes = df.index[y_km == cluster]
similar_genes = genes.values.tolist()

for gene in similar_genes:
    print (gene)

fig, ax = plt.subplots()
ax.set_title("CFU vs poly gene expression")
plt.scatter(df3[y_km == 0,0], df3[y_km == 0,1], s=100, c='red')
plt.scatter(df3[y_km == 1,0], df3[y_km == 1,1], s=100, c='blue')
plt.scatter(df3[y_km == 2,0], df3[y_km == 2,1], s=100, c='black')
plt.scatter(df3[y_km == 3,0], df3[y_km == 3,1], s=100, c='green')
fig.savefig("kmeans_n4_1.png")
plt.close(fig)
