from simhash import Simhash, SimhashIndex
import collections, glob, itertools, random
import random
import pandas as pd
from tqdm import tqdm
import os

min_tweets = 30

f_dim = 100
cutoff_users = 5000
save_dest = 'results'

F = sorted(glob.glob("tweet_simhash/*"))
objs = []
names = collections.defaultdict(itertools.count)
data = {}

time_delta = pd.Timedelta(days=60)
lastdayfrom = pd.to_datetime('4/1/2017')

def read_file(f):

    df = pd.read_csv(f,parse_dates=True)
    if not len(df):
        return None
    
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df= df.set_index('timestamp')
    df.index = df.index.sort_values()
    
    df = df.loc[lastdayfrom - time_delta:]#.reset_index()

    # Must have at least 30 tweets in last 60 days
    if len(df) < min_tweets:
        return None
    
    name = os.path.basename(f)
    
    # Remove duplicate tweet/hashes
    df = df.drop_duplicates(subset='hash')

    objs = []
    data = {}
    
    for _,row in df.iterrows():
        n_tokens = row.tweet.split()
        if n_tokens < 5: continue
        
        hx = Simhash(long(row.hash),f=f_dim)
        key = "{}_{}".format(name, names[name].next())
        objs.append((key,hx))
        data[key] = row.tweet

    return objs, data
        
    #if len(objs)>cutoff: break
    #print f, len(objs), cutoff

from joblib import delayed, Parallel
func = delayed(read_file)

F = F[:cutoff_users]

with Parallel(-1) as MP:
    for res in MP(func(x) for x in tqdm(F)):
        if res is None: continue
        ox,dx = res

        objs.extend(ox)
        data.update(dx)


print "OBJS SIZE", len(objs)
index = SimhashIndex(objs, f=f_dim, k=3)
print "Bucket size", index.bucket_size()

accounted_keys = set()
dataset = []
C = collections.Counter()

for key,val in tqdm(objs):
    # Skip if we've seen this pattern before
    if key in accounted_keys:
        continue

    dupes = index.get_near_dups(val)
    tweet = data[key]
    
    # Don't report self-matches
    if len(dupes)<=1:
        continue

    # Don't report if person repeats only themself
    unique_names = set(['_'.join(x.split('_')[:-1]) for x in dupes])
    if len(unique_names) <= 1:
        continue

    accounted_keys.update(dupes)

    for k1,k2 in itertools.combinations(unique_names,r=2):
        #dataset.append({"name1":k1,"name2":k2,"tweet":tweet})
        C[(k1,k2)] += 1
    
    #print key, dupes, tweet
    
os.system('mkdir -p '+save_dest)
df = pd.DataFrame(dataset)
f_csv = os.path.join(save_dest, "simdupe_paircounts.csv")
import csv

with open(f_csv, 'w') as FOUT:
    header = ["name1","name2","n"]
    CSV = csv.DictWriter(FOUT,header)
    CSV.writeheader()
    for key,val in C.most_common():
        CSV.writerow({
            "name1":key[0],
            "name2":key[1],
            "n":val})

