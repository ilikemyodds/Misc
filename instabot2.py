from getpass import getpass
from os import times
from instapy import InstaPy
from instapy import smart_run
import random
import emoji

# Login to Instagram
my_username = "ilikemyodds"

my_password = 'Icu4whoyouare$4'


session = InstaPy(username = my_username,
                  password = my_password,
                  headless_browser = True)

#starting our session

with smart_run(session):
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=3000,
                                    min_followers=50,
                                    max_following=2000,
                                    min_following=50)

    influencers = ['1glaive', 'brakence', 'ssgkobe', 'jasiah',
                   'lildvrkie', 'dr_stink', 'lilrxspy', 'garzi', 'sofaygo',
                   'majinmaj', 'kill.zero_', 'steele11x', '1davidshawty',
                   'tracyminajj', 'yungpinch', 'yvngxchris', 'liltecca',
                   '1youngnef', 'liluzivert', 'juicewrld999', 'pow.fu',
                   'mrsadchill', 'xanxiety', 'girlfriends', 'lilpeep',]

    random.shuffle(influencers)
    
    artist = influencers[:10]
    
    session.follow_user_followers(artist, amount=10, randomize=True, sleep_delay=120)

    


    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", 'follows'],
                                 sleepyhead=True, stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes_hourly=200,
                                 peak_likes_daily=585,
                                 peak_comments_hourly=80,
                                 peak_comments_daily=182,
                                 peak_follows_hourly=48,
                                 peak_follows_daily=None,
                                 peak_unfollows_hourly=35,
                                 peak_unfollows_daily=402,
                                 peak_server_calls_hourly=None,
                                 peak_server_calls_daily=4700)

    session.unfollow_users(amount=60, instapy_followed_enabled=True, instapy_followed_param="nonfollowers", style="FIFO", unfollow_after=90*60*60, sleep_delay=501)
    