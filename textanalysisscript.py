# what characters are named the most? (create list of all character names)
#      must consider common names like Levin (can be more than one person)
#      make consideration for collocates..?
#      also consider can have 's or s at the end (& do .islower)
#       Prince or Princess not considered - refer to diff characters at diff times
#       replace new lines w/ spaces or figure out how to do regex .. ?
#       Vronsky + Karenin same name - maybe just search for either last name or first + middle? (not only first)
#       Don't double count (e.g. *Alexey Alexandrovitch* Karenin should only be one, not two occurrences "AA" + "Karenin" = 2)
#       Put each character into a list, and put those lists into another list, then make sure to delete each character name from text as you go along to not double count
#       Put ' ' or '.' after to make sure not in the mid of word e.g. Lvova vs Lvov
#       How many times does "Alexey" come up w/o the mid name after it? (differentiate between karenin and vronsky)
# most common words?
# how similar between two texts?

# Anna Karenina text downloaded from Project Gutenberg

import nltk
from nltk.tokenize import TweetTokenizer

import re

tokenizer = TweetTokenizer()

annaKareninaText = "/Users/yanisa/GoogleDrive/Personal_Projects/Tolstoy/AnnaKarenina_TextAnalysis/AnnaKarenina.txt"

# lexical richness
def lexicalRichnessFunction(file):
    openAnnaKarenina = open(file)
    readTxt = openAnnaKarenina.read()
    text = tokenizer.tokenize(readTxt)
    lexMath = len(set(text)) / len(text)
    print('Lexical Richness: ' + str(lexMath))

allCharactersList = []
openCharacterList = open("/Users/yanisa/GoogleDrive/Personal_Projects/Tolstoy/AnnaKarenina_TextAnalysis/characterlist.txt")
characterList = openCharacterList.read()
def characterMakeListOfListsFunction(text):
    # eachCharacterNames/empty string has to be inside the function because I am adding to it (not just reading)
    eachCharacterNames = ''
    eachCharacterNamesAgain = []
    # Remove brackets and text in between the brackets and empty left and right whitespace
    cleanText = re.sub('\[.*\]', '', text)
    noWhiteSpace = str.strip(cleanText)
    for characters in noWhiteSpace: 
        # copy everything until '\n'
        if characters != '\n':
            eachCharacterNames = eachCharacterNames + characters
        # once you hit '\n', split @ commas (to separate names & output as list), add those to the list of lists, and empty the small list
        if characters == '\n':
            firstCharacterList = eachCharacterNames.split(',')
            # empty the list to start the next tolstoy character
            eachCharacterNames = ''
            for eachCharacter in firstCharacterList:
                # strip white space from each name, then add them to the list (must assign to list so I don't keep overwriting them)
                eachCharacterNamesAgain.append(eachCharacter.rstrip())
            # add each character list to create list of lists
            allCharactersList.append(eachCharacterNamesAgain)
            # empty the character list to go back up and start the next character (so it doesn't keep adding them)
            eachCharacterNamesAgain = []
    #print(allCharactersList)

def characterCountFunction(characters):
    annaKareninaOpen = open(annaKareninaText)
    annaKarenina = annaKareninaOpen.read().lower().replace('\n', ' ')
    characterCountDict = {}
    for eachList in characters:
        # assigning variable to use as key in dict later
        keyInDict = eachList[0]
        # assign key to 0 for each new character (list in list of lists)
        characterCountDict[keyInDict] = 0
        # this part is for each list in the list of lists (e.g. only looking at Stiva's names, etc...)
        for element in eachList:
            # make everything lowercase to match the cleaned AK text
            allLowerCase = element.lower()
            if allLowerCase in annaKarenina:
                # have to make numOfInstances variable to count each instance (time a name appears), not just whether or not it shows up in the text
                numOfInstances = annaKarenina.count(allLowerCase)
                # remove the element from the AK text so it doesn't double-count each time it goes around (changing it to puff because it's cute<3)
                annaKarenina = annaKarenina.replace(allLowerCase, "puff!")
                # if the character name is found, add it to the dictionary within its key
                characterCountDict[keyInDict] = characterCountDict[keyInDict] + numOfInstances
    #print(characterCountDict)
    # v = values, reverse = True so it prints in descending (not ascending) order
    sortedCharacterCountDict = sorted(characterCountDict.items(), key=lambda v: v[1], reverse = True)
    print(sortedCharacterCountDict)


#lexicalRichnessFunction(annaKareninaText)

characterMakeListOfListsFunction(characterList)

characterCountFunction(allCharactersList)