class Guess:
 
    def __init__(self, word):
        self.secretWord = word
        self.currentStatus = '_' * len(word)
        self.guessedChars = set()

    def displayCurrent(self):
        return ' '.join(self.currentStatus)
    
    def displayGuessed(self):
        return ' '.join(sorted(list(self.guessedChars)))
        
    def guess(self, character):
        self.guessedChars.add(character)
        if character not in self.secretWord:
            return False
        
        for index, value in enumerate(self.secretWord):
            if value == character:
                self.currentStatus = self.currentStatus[:index] + character + self.currentStatus[index+1:]
        
        return True
    
    def finished(self):
        return self.currentStatus == self.secretWord