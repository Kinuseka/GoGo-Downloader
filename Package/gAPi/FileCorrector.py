class Getname:
  def __init__(self, name):
    self.name = name
    self.prohibit = ['/',"\\"]
  def correct(self):
    d = False
    if (self.prohibit[0] in self.name):
        new = (self.name.replace("/","_"))
        d = True
    if (self.prohibit[1] in self.name):
        new = (self.name.replace("\\","_"))
        d = True
    if not d:
      new = self.name
    return(new)