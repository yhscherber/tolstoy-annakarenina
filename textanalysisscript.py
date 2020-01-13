# what characters are named the most? (create list of all character names)
#      must consider common names like Levin or Oblonsky (can be more than one person)
#      make consideration for collocates..?
#      also consider can have 's or s at the end (& do .islower)
#       Prince or Princess not considered - refer to diff characters at diff times
#       replace new lines w/ spaces or figure out how to do regex .. ?
#       Vronsky + Karenin same name - maybe just search for either last name or first + middle? (not only first)
#       Don't double count (e.g. *Alexey Alexandrovitch* Karenin should only be one, not two occurrences "AA" + "Karenin" = 2)
# most common words?

# Anna Karenina text downloaded from Project Gutenberg

import nltk
from nltk.tokenize import TweetTokenizer

tokenizer = TweetTokenizer()

# lexical richness
def lexicalRichnessFunction(file):
    openAnnaKarenina = open(file)
    readTxt = openAnnaKarenina.read()
    text = tokenizer.tokenize(readTxt)
    lexMath = len(set(text)) / len(text)
    print('Lexical Richness: ' + str(lexMath))

annaKareninaText = "/Users/yanisa/GoogleDrive/Personal_Projects/Tolstoy/AnnaKarenina_TextAnalysis/AnnaKarenina.txt"
lexicalRichnessFunction(annaKareninaText)