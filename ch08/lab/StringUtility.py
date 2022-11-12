vowel = [ "a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

class StringUtility:
  def __init__(self, test_strings):
    def vowels(self, vowel):
      bx = (len(each for each in test_strings if each in vowel))
      if bx < 5:
        return(bx)

      if bx >= 5:
        return("many")
    def bothEnds(self):
      return(test_strings[0] + test_strings[1] + test_strings[-2] + test_strings[-1])
    def fixStart(self):
      return(test_strings[0] + test_strings[1:].replace(test_strings[0], "*"))
    def assiiSum(self):
      return(sum(ord(ch) for ch in test_strings))
    def cipher(self):
       return((chr(ord(test_strings)+len(test_strings))
def __str__(self):          
  return (test_strings)
