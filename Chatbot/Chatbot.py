# Knights to was "ni" video reference
# https://www.youtube.com/watch?v=zIV4poUZAQo

file = open("stop-words.txt")
stopwords = file.readlines()
#function to filter out stop words: and, if, where...
def filterOutStopwords(filteringString):
    #filteredstring = ""
    for word in stopwords:
        next = word.strip()
        #print(next)
        filteringString = filteringString.replace(" " + next + " ", " ")
    return filteringString
#meeting the chat bot
input = raw_input("Hi!, What is your name?: ")
filtered = filterOutStopwords(input)
filtered = filtered.replace(" name " , " ")
filtered = filtered.replace(" called " , " ")
filtered = filtered.replace("my " , " ")
print("Nice to meet you " + filtered)
#chatbot asks how your feeling
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
    print("Please type something")
else:
    print("I dont know that emotion")
#making section where chatbot asks why you feel this way.