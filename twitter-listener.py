import argparse
import logging
import logging.config
import os
import tweepy
import yaml

from tinydb import TinyDB


def setup_logging(
    default_path='logging.yml',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration"""
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


setup_logging()
logger = logging.getLogger(__name__)


class StreamListener(tweepy.StreamListener):
    def __init__(self, db=TinyDB('db.json'), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = db

    def on_status(self, status):
        # ignore other users' tweets
        if status.retweeted:
            return
        logger.info(f"@{status.user.screen_name} twitted: {status.text}")
        self.db.insert({
            'created_at': str(status.created_at),
            'user': status.user.screen_name,
            'text': status.text
        })


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Follow and save Twitter users' feed.")
    parser.add_argument(
        'usernames', metavar='username', type=str, nargs='+',
        help='Twitter username of users to follow'
    )
    parser.add_argument('-f', '--file', type=str, default='db.json')

    args = parser.parse_args()
    screen_names = args.usernames
    db_file = args.file

    auth = tweepy.OAuthHandler(
        os.environ['TWITTER_CONSUMER_KEY'],
        os.environ['TWITTER_CONSUMER_SECRET']
    )
    auth.set_access_token(
        os.environ['TWITTER_TOKEN_KEY'],
        os.environ['TWITTER_TOKEN_SECRET']
    )
    api = tweepy.API(auth)

    user_ids = [api.get_user(name).id for name in screen_names]
    stream_listener = StreamListener(TinyDB(db_file))
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)

    for screen_name, user_id in zip(screen_names, user_ids):
        logger.info(f"starting streaming tweets from @{screen_name} (id {user_id})")
    stream.filter(follow=[f'{user_id}' for user_id in user_ids])
