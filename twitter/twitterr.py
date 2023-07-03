import tweepy

# Twitter API erişim anahtarlarınızı buraya girin
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Tweepy ile kimlik doğrulama yapın
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Tweetleri alma fonksiyonu
def get_user_tweets(username, count):
    tweets = api.user_timeline(screen_name=username, count=count)
    for tweet in tweets:
        print(tweet.text)

# Kullanıcının tweetlerini al
get_user_tweets("kullanici_adi", 10)  # "kullanici_adi" yerine ilgili kullanıcı adını girin
