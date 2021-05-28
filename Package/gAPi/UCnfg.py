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
      ##--SET VALUE
      Video_tupQual= ('1080p','720p','480p','360p','best')
      Video_tupMode = ('auto','manual')
      Video_tupOption = ("on","off")
      Global_tupMode= ("download", "archive")
      ##--end
      ###--Define Config set
      
      #Global config 
      #--Mother
      Global = self.config["Global"]
      #--Child
      Global_mode = Global["mode"]
      #-END 
      
      #Video Config
      #--Mother
      Video = self.config['Video']
      #--Child
      Video_option = Video["enable"]
      Video_qual = Video["quality"]
      Video_mode = Video["selection"]
      #-END
      
      #Domain Config
      #--Mother
      Dom = self.config["Network"]
      #--Child
      Dom_option = Dom["domain"]
      ##--end
      if Video_option not in Video_tupOption:
        value = 1
        print(f"[WARNING] Option: {Video_option} is invalid on 'options.ini'\nAdjusted to select: on")
        self.config.set('Video','enable','on')
        
      if Video_option != 'off':
        if Video_qual not in Video_tupQual:
          value = 1
          print(f"[WARNING] Quality: '{Video_qual}' is invalid on 'options.ini'\n"
          "Adjusted to select: best")
          self.config.set('Video','quality', 'best')
        elif Video_qual != "best":
          print(f"[WARNING] IT IS RECOMMENDED TO USE THE 'BEST' QUALITY SETTING DUE TO NEW GOGOANIME'S CLOUDFLARE VERIFICATION\n")
          
        if Video_mode not in Video_tupMode: 
          value = 1
          print(f"[WARNING] Selection: '{Video_mode}' is invalid on 'options.ini'\nAdjusted to select: auto")
          self.config.set('Video','selection', 'auto')
          
      if Global_mode not in Global_tupMode:
        value = 1
        print(f"[WARNING] Selection: '{Global_mode}' is invalid on 'options.ini', reseting")
        self.config.set('Global','mode', 'download')
        
      if value == 1:
        with open('options.ini', 'w') as cor:
          self.config.write(cor)
    except KeyError as error:
      if os.path.isfile('options.ini') == False:
        print("[FATAL ERROR] file 'options.ini' not found")
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
      if self.config['Network']['domain'] == "ai":
        if b:
          return("ai")
        return('https://gogoanime.ai')
      elif self.config['Network']['domain'] == "vc":
        if b:
          return("vc")
        return('https://gogoanime.vc')
      else:
        print('[CONFIG] Invalid input automatic set to "https://gogoanime.vc"')
        if b:
          return("vc")
        return('https://gogoanime.vc')
    except KeyError as e:
      if debug == True:
        print(e)
      print('[FATAL ERROR] options.ini is broken, program will fail if not fixed')
    
  