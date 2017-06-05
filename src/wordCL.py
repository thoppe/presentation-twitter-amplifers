import pandas as pd
from tqdm import tqdm
import numpy as np
import collections, glob,itertools
from wordcloud import WordCloud, STOPWORDS

import seaborn as sns
import pylab as plt

new_words=["amp","nt","re","will","I"]
STOPWORDS.update(new_words)

new_words="U de e di en che la att il u de la die en que le les un via et der m und des pas je du y na ve "
#STOPWORDS.update(new_words.split())

F_CSV = glob.glob("results/qtext_*")
DF = {}
for f in sorted(F_CSV):
    print f
    df = pd.read_csv(f).set_index('word')   
    df = df.drop(STOPWORDS)
    df.n /= df.n.sum()*1.0


    #words = (df.delta*100000).astype(int)
    #words = words[words>2]

    DF[f] = df
    #C = collections.Counter(dict(zip(df.index,df.n)))
    #DF[f] = C

    '''
    # Generate a word cloud image
    wordcloud = WordCloud(background_color="white",
                          stopwords=STOPWORDS,
                          max_words=500)
    WC = wordcloud.generate_from_frequencies(C)

    # Display the generated image:
    # the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(WC, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    '''

#print DF['results/qtext_5.csv'].most_common(20)
#print DF['results/qtext_3.csv'].most_common(20)
#exit()
keys = sorted(DF.keys())

#delta = (DF[keys[-1]].n-DF[keys[-2]].n).dropna().sort_values()
#print delta
#exit()
k = 400
C0 = collections.Counter(dict(zip(DF[keys[-1]].index,DF[keys[-1]].n)))
C1 = collections.Counter(dict(zip(DF[keys[4]].index,DF[keys[4]].n)))
wordlist = set(zip(*C0.most_common(k))[0]+zip(*C1.most_common(k))[0])
wordlist = [x for x in wordlist if x==x.upper() or len(x)>2]
dist = np.array([[DF[f].ix[w].n for f in keys] for w in tqdm(wordlist)])

from scipy.stats import pearsonr,spearmanr

N = len(dist)
delta = np.zeros((N,N))

for i,j in tqdm(itertools.combinations(range(N),r=2)):
    r,p = spearmanr(dist[i],dist[j])
    if p>0.05: r = 0
    delta[i,j] = delta[j,i] = r

delta = pd.DataFrame(data=delta, index=wordlist, columns=wordlist)
sns.set(style='white',font_scale=.7)

g=sns.clustermap(delta,vmax=1,vmin=-1,mask=delta==0)

plt.setp(g.ax_heatmap.get_yticklabels(), rotation=0)
plt.setp(g.ax_heatmap.get_xticklabels(), rotation=90)

plt.show()

exit()

for word in ['obama','white','trump','jew','jewish','CNN','israel']:
    print word, word in zip(*C0.most_common(400))[0]
    print word, word in zip(*C1.most_common(400))[0]
exit()

for word in ['obama','white','trump','jew','jewish','CNN','israel']:

    Y = [DF[f].ix[word].n  for f in keys]
    Y = np.array(Y)
    Y /= Y[0]
    plt.plot(Y,label=word)
    
    print word, Y
plt.legend()
plt.show()

