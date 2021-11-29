import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def readFile(filename):
    with open(filename,'r') as file:
        fileContent = file.read()
        return fileContent

def createSummary(filename):
    with open(filename,'w') as file:
        pass
        

if __name__ == '__main__':
    userFile = input("Enter complete file name for the .txt file: ")
    userFileData = readFile(userFile)

    #handling words in the text
    #creating set of all the stopwords
    stopWords = set(stopwords.words("english"))

    words = word_tokenize(userFileData)
    wordFrequency = dict()

    #creating frequency dictionary for score of each word
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in wordFrequency:
            wordFrequency[word] += 1
        else:
            wordFrequency[word] = 1

    #handling sentences in the text
    sentences = sent_tokenize(userFileData)
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in wordFrequency.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

    sumValue = 0
    for sentence in sentenceValue:
        sumValue += sentenceValue[sentence]

    #average value of the sentence from the text
    average = int(sumValue / len(sentenceValue))

    summary = ""
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > 1.2 * average):
            summary += " " + sentence
    
    with open("summary.txt","w") as newf:
        newf.write(summary)
















