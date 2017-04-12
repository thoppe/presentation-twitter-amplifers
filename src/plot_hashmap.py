import itertools
import numpy as np
import pandas as pd
import collections, os
from tqdm import tqdm

f_sim = "results/simdupe_paircounts.csv"

df = pd.read_csv(f_sim)
cols = {"name1":"name2","name2":"name1"}
df = df.append(df.rename(columns=cols)).reset_index(drop=True)
df = pd.pivot_table(df, "n", "name1","name2",aggfunc='sum').fillna(0)
dist = df.values

dist = np.exp(-1.5*np.log(dist+1))
dist[dist>.75] = 100
np.fill_diagonal(dist,0)


'''
from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import linkage, leaves_list

Z = linkage(squareform(dist),method='ward')
sort_index = leaves_list(Z)

new_names = df.index[sort_index
]dist = dist[sort_index,:][:,sort_index]
M = pd.DataFrame(data=dist, index=new_names, columns=new_names)
'''

#degree = dist.mean(axis=0)
#print degree
#sort_index = np.argsort(degree)[::-1]
#dist = dist[sort_index,:][:,sort_index]

# The no change op
M = pd.DataFrame(data=dist,index=df.index,columns=df.columns)
print M.mean().mean()

import pylab as plt
import seaborn as sns

# Convert back to a similarity
M[M>0.75] = 1.0
M = 1-M

M.to_csv("results/sim_matrix.csv",index=False)


g = sns.heatmap(M,vmin=0,vmax=1,cmap="Blues",cbar=False,
                mask=np.isclose(M,0),
                xticklabels=False,yticklabels=False)
plt.xlabel("")
plt.ylabel("")
plt.tight_layout()
plt.savefig("figures/SG_unorg.png")
plt.show()

exit()



#sns.distplot(degree)
#plt.show()
#print

#mask = np.zeros(M.shape)
# Keep only the highly connected componet
degree = M.sum(axis=0)/M.shape[0]
idx = degree > .2
names = M.columns
M = M.ix[names[idx],names[idx]]

connected_names = pd.DataFrame()
connected_names["is_connected"] = idx
connected_names.to_csv("results/connected_names.csv",index_label="username")
degree = M.sum(axis=0)/M.shape[0]


import pylab as plt
import seaborn as sns
sns.set(style="white", font_scale=0.75)

sns.distplot(degree)

plt.figure(figsize=(10,10))
g = sns.heatmap(M,vmin=0,vmax=1,cmap="Blues",
                    cbar=False,
                    #mask=mask,
)

plt.axis('off')
plt.tight_layout()
#g.xaxis.set_ticks_position('none')
#plt.setp(g.get_yticklabels(), rotation=0)
#plt.setp(g.get_xticklabels(), rotation=90)
plt.show()
