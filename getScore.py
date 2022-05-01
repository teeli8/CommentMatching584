class KeyWordsDict:

    def __init__(self, lines):
        self.wordDict = self.__getWordDict(lines)

    #strs: list of string of patterns
    def getScore(self, strs) -> int:
        dictMap = self.wordDict
        stringScore = 0
        for s in strs:
            stringScore += int(dictMap[s])

        return stringScore

    def getAllPatterns(self) -> list:
        commentKeys = self.wordDict.getKeys()
        return commentKeys


    def __getWordDict(self, string):
        dictMap = {}
        for line in string:
            line = line.strip().split(" ")
            word = line[0]
            score = line[1]
            dictMap[word] = score
        #commentKeys = dictMap.keys()

        return dictMap

'''
if __name__ == '__main__':
    file1 = open('comments.data', 'r')
    Lines = file1.readlines()

    string = "excellent game, very good"
    string2 = "poor game it sucks"
    strs = [string, string2]
'''




