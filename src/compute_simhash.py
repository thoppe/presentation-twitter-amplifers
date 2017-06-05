import simhash
from tqdm import tqdm
import pandas as pd
import os
import random
import joblib
import itertools
import collections, glob
from src.parse import parse_tweet, singlefile_iterator
from simhash import Simhash

f_dim = 100
THREADS = -1

save_dest = "tweet_simhash"
os.system('mkdir -p '+save_dest)

def get_features(s):
    width = 3
    s = s.replace(' ','')
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]

F = sorted(glob.glob("tweet_archive/*"))
random.shuffle(F)

def compute(item):
    item['name'] = item.pop('tags')[0][1:-1]

    tweet = parse_tweet(item['tweet'])
    item['tweet'] = tweet
    features = get_features(tweet)

    item['hash'] = Simhash(tweet,f=f_dim).value
    return item

known_items = set(glob.glob(save_dest+'/*'))

print "Scanning for completes"
F = [f for f in tqdm(F) if
     os.path.join(save_dest, os.path.basename(f)) not in known_items]

with joblib.Parallel(THREADS) as MP:

    for f in tqdm(F):
        name = os.path.basename(f)

        f_out = os.path.join(save_dest, os.path.basename(f))
        if os.path.exists(f_out): continue

        if not os.path.getsize(f):
            continue        
        
        INPUT_ITR = singlefile_iterator(f)

        ITR = MP(joblib.delayed(compute)(x) for x in INPUT_ITR)

        data = []
        
        for item in ITR:
            tweet = item['tweet']

            # Skip if more than 4 emoji
            if len([x for x in tweet if x=='E'])>=4:
                continue

            # Skip if not at least 4 text tokens
            if len([x for x in tweet.split() if x==x.lower()]) < 4:
                continue

            data.append(item)

        df = pd.DataFrame(data)
        df['name'] = name
        
        df.to_csv(f_out,index=False)

        print name, len(df)
