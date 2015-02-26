
learnWords = {}
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
def feelings(): #Feelings function, analyses what your mood is.
    input = raw_input("How are you feeling?: ")
    filtered = filterOutStopwords(input)
    #if statement to see what the user is feeling.
    if filtered == 'sad':
        print("Im sorry to hear that.")
    elif filtered == 'happy':
        print("Im glad to hear! :)")
    elif filtered == 'bored':
        print("Thats why im here.")
    elif len(filtered) == 0:
        print("Come on, you can talk to me :)")
        feelings()
    else:
        print("I dont know that emotion")
        feelings()
#####################################################################################
def chatbotMemory():
    input = raw_input("Why do you feel this way? Explain with its name then Description: ")#chatbot asks why you feel this way, stores info in a dictionary.
    for words in input:
        mem = input.split().lower()
        
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
