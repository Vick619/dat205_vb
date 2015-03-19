import twitter, datetime, urllib2 #import Libraries.

currentSession = open("/Users/vfbrelsford/Library/Application Support/Google/Chrome/Default/Current Session")
lastSession = currentSession.read() #Pull in cache of browser history and store in lastSession.

user = 108733490 #My unique twitter ID.

startindex = lastSession.rfind("http")
endindex = lastSession.find(chr(0), startindex) #Look through lastSession, find where http if and look for the Null at the end of the url string.

lastUrl = lastSession[startindex:endindex] #Get the inbetween of the two index points and print it out.
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>" + lastUrl)

gotUrl = urllib2.urlopen(lastUrl) #pull in lastUrl, then read the file.
html = gotUrl.read()

startOfTitleTag = html.find("<title")
endOfTitleTag = html.find(">",startOfTitleTag)
endTitle = html.find("</title>", endOfTitleTag) #Find the title tag in html, both beggining and end, then store the inbetween in a title variable.
Title = html[endOfTitleTag:endTitle]
print(">>>>>>>>>>>>>>>>>>>>>>>" + Title)

file = open("apikey.txt")
cred = file.readline().strip().split(',') #open ApiKey file and read in the passwords/secret.

api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1],
access_token_key=cred[2],access_token_secret=cred[3])  #structure the passwords/secrets in a specific way.

timestamp = datetime.datetime.utcnow()
response = api.PostUpdate("Tweeted at: " + str(timestamp)+ " Went to: " + str(lastUrl) + " Title is: " + str(Title))
print("Status updated to: " + response.text)
statuses = api.GetUserTimeline(user)    #get Date and time, 

print (statuses[0].text)