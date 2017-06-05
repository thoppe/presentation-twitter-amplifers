import sys, os, subprocess
from tqdm import tqdm 
#username = sys.argv[1]
username = 'RichardBSpencer'

# Grab the users following 
os.system('mkdir -p following')
f_following = os.path.join('following',username)
if not os.path.exists(f_following):
    cmd = "twitter-follow -gio {name} > following/{name}"
    os.system(cmd.format(name=username))

# Grab the users followers
os.system('mkdir -p followers')
f_followers = os.path.join('followers',username)
if not os.path.exists(f_followers):
    cmd = "twitter-follow -rio {name} > followers/{name}"
    os.system(cmd.format(name=username))

    
#proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#while proc.poll() is None:
#      print proc.stdout.readline() #give output from your execution/your own message
# self.commandResult = proc.wait() #catch return code
 
os.system('mkdir -p tweet_archive')
def archive(name):
    print "Starting", name
    
    f = os.path.join('tweet_archive',name)
    if os.path.exists(f):
        #print "Already archvied {}".format(name)
        return False
    
    cmd = 'twitter-archiver -o -s tweet_archive {name}'
    cmd = cmd.format(name=name)
    proc = subprocess.Popen(cmd, shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
    proc.wait()
    result = '\n'.join([line for line in proc.stdout])
    if "Fail: 401 Unauthorized" in result:
        print "401 Unauthorized", name
        os.system("touch tweet_archive/{}".format(name))
        return False
    if "Total: 0 tweets" in result:
        print "No tweets found for", name
        os.system("touch tweet_archive/{}".format(name))
        return False
    
    print "Completed", name
    print result
    return True

# Start first with the username   
archive(username)

# Load up the following
#with open(f_following) as FIN:
#    fusers = [line.split()[-1] for line in FIN]
#for name in tqdm(fusers):
#    archive(name)

# Load up the followers
with open(f_followers) as FIN:
    fusers = [line.split()[-1] for line in FIN]
    for name in tqdm(fusers):
        archive(name)



