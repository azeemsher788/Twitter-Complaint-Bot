from scripts.net_speed_complain import InternetSpeedTwitterBot
# Debugging: Print the path to the extension

with InternetSpeedTwitterBot(teardown=False) as bot:
    bot.get_internet_speed()
    bot.on_browsec_vpn()
    bot.tweet_at_provider()