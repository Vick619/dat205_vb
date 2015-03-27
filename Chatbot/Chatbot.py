import urllib2


#learnWords = {}
file = open("stop-words.txt")
stopwords = file.readlines()
#####################################################################################
def filterOutStopwords(filteringString): #function to filter out stop words: and, if, where...
    #filteredstring = ""
    for word in stopwords:
        next = word.lower().strip()
        #print(next)
        filteringString = filteringString.replace(" " + next + " ", " ").lower()
    return filteringString
#####################################################################################
def wiki(wikiword):
    gotUrl = urllib2.urlopen("http://en.wikipedia.org/wiki/"+wikiword) #pull in wiki search, then read the file.
    #gotUrl = urllib2.urlopen("http://www.urbandictionary.com/define.php?term="+wikiword)
    html = gotUrl.read()

    startOfPTag = html.find("<p")
    endOfPTag = html.find(">",startOfPTag)
    endP = html.find("</p>", endOfPTag) #Find the p tag in html, both beggining and end, then store the inbetween in a p variable.
    description = html[endOfPTag:endP]
    return description #return everything between the p tags.

#####################################################################################
def feelings(): #Feelings function, analyses what your mood is.
    input = raw_input("How are you feeling?: ")
    filtered = filterOutStopwords(input)
    #if statement to see what the user is feeling.
    if filtered == 'sad':
        print("Im sorry to hear that " + name)
        chatbotMemory()
    elif filtered == 'happy':
        print("Im glad to hear! :)")
        chatbotMemory()
    elif filtered == 'bored':
        print("Thats why im here. " + name)
        chatbotMemory()
    elif filtered == 'meh':
        print("Well, meh is a valid response.")
        chatbotMemory()
    elif filtered == 'ok':
        print("It's good to be ok! " + name)
        chatbotMemory()
    elif filtered == 'great':
        print("Wow, I havn't talked to someone so positive in a while.")
        chatbotMemory()
    elif filtered == 'good':
        print("That's good.")
        chatbotMemory()
    elif filtered == 'shit':
        print("Must be bad if you'r swearing!")
        chatbotMemory()
    elif filtered == 'fucked':
        print("Well that is a bad way to feel :[")
        chatbotMemory()
    elif filtered == 'nervous':
        print("Why so nervous? " + name)
        nervous()
    elif len(filtered) == 0:
        print("Come on, you can talk to me :)")
        feelings()
    else:
        print("I dont know that emotion")
        feelings()
#####################################################################################
def nervous(): #nervous section, lets the user vent...
    input = raw_input("Tell me what your nervous about?: ")
    filtered = filterOutStopwords(input)
    if len(filtered) > 0:
        print("Tell me more...")
        startwiki()
    elif len(filtered) == 0:
        print("you can talk to me :)")
        nervous()

def startwiki():
    if len(filtered) > 0:
        chatbotMemory()
    elif len(filtered) == 0:
        print("you can talk to me :)")
#####################################################################################
def chatbotMemory():
    input = raw_input("With one word, describe why you feel like this: ")#chatbot asks why you feel this way, stores info in a dictionary.
    for word in input:
        filtered = filterOutStopwords(input)
        filtered = filtered.replace("because " , " ")
        filtered = filtered.replace(" because " , " ")
        filtered = filtered.replace("well " , " ")
        filtered = filtered.replace(" well " , " ")
        description = wiki(filtered)
        #description = description.replace(">" , " ")
        #description = description.replace(">" , " ")
        description = description.replace("<b>" , " ")
        description = description.replace("</b>" , " ")
    print("From your word: " + filtered + ". I found: " + description)
        
#####################################################################################
input = raw_input("Hi!, What is your name?: ")#meeting the chat bot
filtered = filterOutStopwords(input)
filtered = filtered.replace(" name " , " ")
filtered = filtered.replace(" called " , " ")
name = filtered.replace("my " , " ")
print("Nice to meet you " + name)
feelings() #chatbot asks how your feeling
#####################################################################################
#chatbotMemory()
