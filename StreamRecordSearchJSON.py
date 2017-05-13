from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import date
today = str(date.today())
print(today)

access_token="740635692359950336-4rgBW9g1baTzcvX8rVzBBRbS08KIN39"
access_token_secret="KgJ0LlsMeKvEIdJblamLN411HNGo3N3FezBHpJvgmu0Xa"
consumer_key="GT3xrIN0V85UdqPqUZ4E28egE"
consumer_secret="oBzZvyTApKHxP0GSqo9lbRJ1K93CJRIovRN8zdBaic5oANGRvN"

class StdoutListener(StreamListener):
    def on_data(self,data):
            #print(data)
            l=StdoutListener()
            filename='TwitterGetStream_v1_Output_'+ today +'_NewsSources.json'
            savefile=open(filename,'a')
            savefile.write(data)
            savefile.close()
authentication = OAuthHandler(consumer_key,consumer_secret)
authentication.set_access_token(access_token,access_token_secret)
stream = Stream(authentication,StdoutListener())
#stream.filter(track=['USA Today','Los Angeles Times','U.S. News','Newsweek','MSNBC','HuffPost','CBS News','ABC News','NPR','Washington Post','The Economist','The Associated Press','Wall Street Journal','BBC News (World)','TIME','Fox News','The New York Times','CNN'])
stream.filter(track=['USAToday','LATimes','USNews','Newsweek','MSNBC','HuffPost','CBSNews','ABC','NPR','WashingtonPost','TheEconomist','AP','WSJ','BBCWorld','TIME','Fox News','NyTimes','CNN'])