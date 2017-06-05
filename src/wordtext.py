import pandas as pd
from tqdm import tqdm
import numpy as np
import collections
from wordcloud import WordCloud, STOPWORDS

import seaborn as sns
import pylab as plt
df = pd.read_csv("results/sim_matrix.csv")
degree = df.mean(axis=0).values

q_bins = 8
bin_idx = pd.qcut(degree, q=q_bins, labels=False)
names = df.columns

'''
sns.set(style='white')
degree = np.sort(degree)
plt.plot(degree)
plt.ylabel("Average degree connectivity")
plt.xlabel("rank index")
sns.despine(trim=True,offset=2)
plt.savefig("figures/degree_rank.png")
#plt.show()
'''

def read_text(name):

    time_delta = pd.Timedelta(days=60)
    lastdayfrom = pd.to_datetime('4/1/2017')
    
    f_sim = "tweet_simhash/{}".format(name)
    dfx = pd.read_csv(f_sim)

    dfx['timestamp'] = pd.to_datetime(dfx['timestamp'])
    dfx= dfx.set_index('timestamp')
    dfx.index = dfx.index.sort_values()

    dfx = dfx.loc[lastdayfrom - time_delta:]#.reset_index()
    return dfx.tweet.tolist()


from joblib import delayed, Parallel
func = delayed(read_text)

with Parallel(-1) as MP:

    for k in range(q_bins):
        C = collections.Counter()

        ITR = tqdm(names[bin_idx==k])
        print k, degree[bin_idx==k].mean()

        for res in MP(func(name) for name in ITR):
            CX = collections.Counter()

            for n_lines,line in enumerate(res):
                CX.update(line.split())

            n_lines = float(n_lines)
            if CX['que'] / n_lines > 0.1:  continue
            if CX['les'] / n_lines > 0.1:  continue
            if CX['pas'] / n_lines > 0.1:  continue
            if CX['und'] / n_lines > 0.1:  continue
            if CX['der'] / n_lines > 0.1:  continue
                
            C.update(CX)
        
        df = pd.DataFrame()
        df['word'] = C.keys()
        df['n'] = C.values()
        df = df.set_index('word').sort_values('n')
        df.to_csv('results/qtext_{}.csv'.format(k))

exit()

