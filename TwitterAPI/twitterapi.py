import twitter, datetime

file = open("/Users/vfbrelsford/Library/Application Support/Google/Chrome/Default/Current Session")
lastSession = file.read()

startindex = lastSession.rfind("http")
endindex = lastSession.find(chr(0), startindex)

print(lastSession[startindex:endindex])

user = 108733490

file = open("apikey.txt")
cred = file.readline().strip().split(',')

api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1],
access_token_key=cred[2],access_token_secret=cred[3])

timestamp = datetime.datetime.utcnow()
response = api.PostUpdate("Tweeted at " + str(timestamp))
print("Status updated to: " + response.text)
statuses = api.GetUserTimeline(user)

print (statuses[0].text)