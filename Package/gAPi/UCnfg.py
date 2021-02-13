from configparser import ConfigParser 
import os 
debug = True
class Config:
  config = ConfigParser(allow_no_value=True, comment_prefixes='/')
  def __init__(self):
    pass
  def checker(self):
    value = 0
    try:
      self.config.read('options.ini')
      Option = self.config['Video']['enable']
      if Option not in ('on','off'):
        value = 1
        print(f"[WARNING] Option: {Option} is invalid on 'options.ini'\nAdjusted to select: on")
        self.config.set('Video','enable','on')
      if self.config['Video']['enable'] == 'off':
        pass
      else:
        preferredq= ('1080p','720p','480p','360p','best')
        se = ('auto','manual')
        quality = self.config['Video']['quality']
        selector = self.config['Video']['selection']
        if quality not in preferredq:
          value = 1
          print(f"[WARNING] Quality: '{quality}' is invalid on 'options.ini'\n"
          "Adjusted to select: best")
          self.config.set('Video','quality', 'best')
        if selector not in se: 
          value = 1
          print(f"[WARNING] Selection: '{selector}' is invalid on 'options.ini'\nAdjusted to select: auto")
          self.config.set('Video','selection', 'auto')
      if value == 1:
        with open('options.ini', 'w') as cor:
          self.config.write(cor)
    except BaseException as error:
      if os.path.isfile('options.ini') == False:
        print("file 'options.ini' not found")
      else:
        print('[FATAL ERROR] options.ini is broken, program will fail if not fixed')
        print(error)
        
  def return_data(self,x):
    preferredq= ('1080p','720p','480p','360p','best')
    se = ('auto','manual')
    self.config.read('options.ini')
    if x == 1:
      c1 = self.config['Video']['quality']
      if c1 in preferredq:
        return(c1)
      else:
        print('code:1')
        return('best')
    if x == 2:
      c2 = self.config['Video']['selection']
      if c2 in se:
        return(c2)
      else:
        print('code:1')
        return('auto')
    if x == 3:
      c3 = self.config['Video']['enable']
      if c3 == 'off':
        return('off')
      else:
        return('on')
    if x == 4:
      c4 = self.config['Video']['source']
      if c4 == "embed":
        return(True)
      else:
        return(False)
  def Domain(self, b=False):
    if b:
      b == True
    try:
      self.config.read('options.ini')
      if self.config['Network']['domain'] == "so":
        if b:
          return("so")
        return('https://gogoanime.so')
      elif self.config['Network']['domain'] == "vc":
        if b:
          return("vc")
        return('https://gogoanime.vc')
      else:
        print('Invalid input automatic set to "https://gogoanime.so"')
        return('https://gogoanime.so')
    except BaseException as e:
      if debug == True:
        print(e)
      print('options.ini not found/error occured')
    
  