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
    
    session.unfollow_users(amount=200, nonFollowers=True,
                           style="RANDOM",
                           unfollow_after=12 * 60 * 60, sleep_delay=501)
    
    session.unfollow_users()