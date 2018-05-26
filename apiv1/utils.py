import os
import tweepy


def resolve_user_icon_url(screen_name: str) -> str:
    consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
    consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth)

    try:
        user = api.get_user(screen_name=screen_name)
    except tweepy.TweepError:
        return None

    icon_img_url = user.profile_image_url_https.replace('_normal', '')
    return icon_img_url
