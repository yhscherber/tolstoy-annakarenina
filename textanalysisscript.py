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
def characterCountFunction(text):
    # eachCharacterNames/empty string has to be inside the function because I am adding to it (not just reading)
    eachCharacterNames = ''
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
            eachCharacterNames = ''
            allCharactersList.append(firstCharacterList)
    #print(allCharactersList)

#lexicalRichnessFunction(annaKareninaText)

characterCountFunction(characterList)