#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#from HTMLParser import HTMLParser
import gmplot
import re
from tkinter.constants import END

#code for tweepy from: http://adilmoujahid.com/posts/2014/07/twitter-analytics/
#code for pulling geotags: http://stackoverflow.com/questions/25224692/getting-the-location-using-tweepy

#Variables that contains the user credentials to access Twitter API 
access_token = "acctoken"
access_token_secret = "acctokens"
consumer_key = "ckey"
consumer_secret = "ckeys"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
       
    def on_status(self, status):
        #print(status.text)
        if status.coordinates:
            result = re.search('\[(.*),', str(status.coordinates))
            lat = float(result.group(1))
            result2 = re.search('[0-9], (.*)]', str(status.coordinates))
            long = float(result2.group(1))
            
            print("point plotted")
            gmap.scatter((long,), (lat,), 'k', marker=True)
            gmap.draw("mymap.html")
        #if status.place:
            #print('place:', status.place.full_name)
            #gmap.plot(status.place)
            #gmap.draw("mymap.html")

        #return True

    #on_event = on_status   

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    
    gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 2.5)
    gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
    
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['trump'])
    #stream.filter()
