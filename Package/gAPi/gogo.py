import requests, re
from bs4 import BeautifulSoup

debug=True
usera = {'User-Agent':'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'}

class Episode:
  
  def __init__(self, link):
    try:
      site = requests.get(link, headers=usera)
      self.ep = BeautifulSoup(site.content, 'html.parser')
    except BaseException as e:
      if debug == True:
        print(f'--\n{e}\n--')
      print('Error occured during process')
      
      
  def episode(self):
    return (self.ep.find('a',class_='active')['ep_end'])
    
    
class Anime:
  
  def __init__(self, link):
    try:
      site = requests.get(link, headers=usera)
      self.parsed = BeautifulSoup(site.content, 'html.parser')
    except BaseException as e:
      if debug == True:
        print ('--\n',e,'\n--')
      print('Link did not load')
      return
    
    
  def List(self, **a):
    if a:
      return(self.parsed.find_all('p', class_='episode'))
    else:
      return(self.parsed.find_all('p',class_='name'))
    
    
  def Len_list(self):
    return(len(self.parsed.find_all('p',class_='name')))
    
    
  def Link(self):
    a = []
    for n in self.parsed.find_all('p',class_='name'):
      a.append(n)
    return(a)
    
    
  def Page_total(self, **a):
    v=(self.parsed.find('ul',class_='pagination-list'))
    if a['val'] == 'selected':
      return(v.find('li', class_ ="selected").text.strip())
    elif a['val'] == 'total':
      return(len(v.find_all('a')))
    else:
      if debug == True:
        print('Page Error')
      return('Error')
     
  
  def Genre_list(self):
    top_genre = self.parsed.find('li', class_='movie genre hide')
    x = 0
    for genre in top_genre.find_all('ul'):
      a_genre = genre.find_all('a')
      lenned = int(len(a_genre))
      for genre in a_genre:
        x += 1
        temp_genre = genre.text.strip()
        print(f'\t{x}.) {temp_genre}')
        if x == lenned:
          break
      break
    print('\t----------------------------------')
    return(top_genre)
    
      
  def Genre_link(self,x,txt):
    d = 0
    lmt = int(x)
    genre_linkhead = txt.find('ul')
    ax_genre = genre_linkhead.find_all('a')
    for genre_2 in ax_genre:
      d += 1
      link_genre = genre_2['href']
      if d == lmt:
        return(link_genre)
        break
  
class Process:
  
  def __init__(self,v):
    self.content = v
    
    
  def full_link(self, **b):
    opt=False
    dom = Config().Domain(True)
    if b:
      if 'val' in b:
        ep=b['val']
      cmd = b['command']
      if cmd == True:
        opt = True
    b = self.content.find('a')['href']
    if opt==True:
      a=b.replace('/category','')
      return(f'https://gogoanime.{dom}{a}-episode-{ep}')
    else:
      return(f'https://gogoanime.{dom}{b}')
      
  
  def Home_ep(self, **a):
    a = a['content']
    if re.search('\d+$', a):
      return(re.search('\d+$', a)[0])
    else:
      raise KeyError('Search not found')
      
      
if __name__ == '__main__':
  link = input('link:')
  if link == '':
    link = 'https://gogoanime.so'
  print(Episode(link).episode())
else:
  from .UCnfg import Config