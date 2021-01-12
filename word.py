import random
  
class Word:

    def __init__(self, filename):
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.words = [line.rstrip() for line in lines]
        self.count = len(self.words)
        self.maxLength = len(max(self.words, key=len))
        print('%d words in DB' % self.count)

 
    def test(self):
        return 'default'

    def randFromDB(self, minLength):
        if minLength > self.maxLength: minLength = self.maxLength
        while(True):
            r = random.randrange(self.count)
            if len(self.words[r]) >= minLength:
                return self.words[r]