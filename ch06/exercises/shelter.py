class Str:
  def __init__(self, chars):
    self.string_nums = []
    for ch in chars:
      self.string_nums.append(ord(ch))
  def get_str(self):
    mystr = ""
    self.string_nums = []
    for ch in self.string_nums:
      mystr += chr(ch)
      return (mystr)

myobj = Str("Hello")
print(myobj.string_nums)