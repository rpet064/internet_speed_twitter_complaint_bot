from get_internet_speed import GetInternetSpeed
from internet_speed_twitter_bot import InternetSpeedTwitterBot

promised_down = 150
promised_up = 10
gis = GetInternetSpeed()

bot = InternetSpeedTwitterBot()
bot.send_tweet(tweet_text=f'''Dear (insert Internet Provider here),
I was promised {promised_down} download speed & {promised_up} upload speed.
But I'm only getting {gis.down} download speed and {gis.up} upload speed.''')



