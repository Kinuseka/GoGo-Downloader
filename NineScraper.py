from bs4 import BeautifulSoup
import requests, re, sys
import goEmbed
avail_link = ""
user_agent = 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'
class Download:
  def __init__(self, avail_link, title):
    self.link = avail_link
    self.t = title
  def scrape_ep(self):
    print("Episodes loading...")
    ep_link = (f'https://gogoanime.so{self.link}')
    r_2 = requests.get(ep_link)
    soup2 = BeautifulSoup(r_2.content, 'html5lib')
    checker_ep = soup2.find('a', class_='active')
    episode_total = checker_ep['ep_end']
    ep_sodeint = int(episode_total)
    print('\t---------------------------------')
    print('\tFound', episode_total, 'episodes in total!')
    print('\t---------------------------------')
    full_link = self.link.replace('/category', '')
    print("=== Bulk download setup ===")
    while True:
      dl_bulkst = 0
      dl_bulken = 0
      dl_bulkst = int(input("Start from episode:"))
      dl_bulken = int(input("Stop to episode:"))
      if int(dl_bulkst) < 1:
        print('Episode too small!')
      elif dl_bulkst > ep_sodeint:
        print(f'Episode is too far! limit: {episode_total}')
      elif dl_bulken > ep_sodeint:
        print(f'Episode is too far! limit: {episode_total}')
      elif dl_bulken < dl_bulkst:
        print('Start should not be bigger than the end')
      else:
        break
    print(f"Downloading EP{dl_bulkst} to EP{dl_bulken}")
    print('do ^C to pause download during the process')
    d = dl_bulkst
    while True:
      if d > dl_bulken:
        print('\t-Process finished-')
        break
      dl_ep_fulllink = (f'{full_link}-episode-{d}')
      print('\t---------------------------------')
      print(f'\t\tDownloading EP{d}')
      print('\t---------------------------------')
      goEmbed.anime_linkscrape(dl_ep_fulllink, d,self.t)
      d = d + 1 
  def home_scrape(self):
    if re.findall('\d[0-9][0-9]$', self.link):
      d = re.findall('\d[0-9][0-9]$', self.link)
    elif re.findall('\d[0-9]$', self.link):
      d = re.findall('\d[0-9]$', self.link)[0]
    else:
      d = re.findall('\d$', self.link)[0]
    print('\t---------------------------------')
    print(f'\t\tDownloading EP{d}')
    print('\t---------------------------------')
    goEmbed.anime_linkscrape(self.link, d, self.t)
    print('\t-Process finished-')
    sys.exit()
def scrape_web(url, setter):
  list = ''
  r = requests.get(url, user_agent)
  soup = BeautifulSoup(r.content, 'html5lib')
  checker_title = soup.find_all('p', class_='name')
  if setter == 'home':
    checker_episodes = soup.find_all('p', class_='episode')
  def link_scrape(value):
    z = 0
    for link in soup.find_all('p', class_="name"):
      a_link = link.find_all('a')
      z = z + 1
      if z > value:
        for link in a_link:
          temp_link = link['href']
          if z > value:
            return(temp_link)
            break
          z = z + 1
  def title_name(number):
    return(checker_title[int(number)].text.strip())
  def show_list(max_an, val1, val2):
    x = 0
    y = 4
    maxi = max_an - 1
    if val1 != 0:
      y = y + val1
    if val2 != 0:
      x = x + val2
    if max_an < 5:
      y = max_an-1
    if y > maxi:
      d = y - maxi
      y = y-d
      #if y > 29: #only for 9anime, not supported
        #print('Max reached')
    while True: 
      if x > y:
        break
      print(f'\t{x+1}.) {checker_title[int(x)].text.strip()}')
      if setter == 'home':
        print(f'\t>{checker_episodes[int(x)].text.strip()}')
      print('\t---------------------------------')
      x = x + 1
  max_an = (len(checker_title))
  var1 = 0
  var2 = 0 
  perm = 'yes'
  print('\t************RESULTS************')
  show_list(max_an, var1, var2)
  print('There are', max_an,'anime/s found')
  if max_an == 0:
    print('Try making your keywords more specific')
    sys.exit()
  if max_an > 5:
    print('do ">n" to see the next list')
  xintmax_an = int(max_an)
  while True:
    choice_anime = input("Select anime:")
    try:
      xchoice = int(choice_anime)
    except:
      pass
    if choice_anime == ">n":
      var1 = var1+5
      var2 = var2+5
      show_list(max_an, var1, var2)
    elif xchoice > xintmax_an:
      print('Input exceeds limit!')
    elif xchoice <= 0:
      print('Too small')
    else:
      title_anime = title_name(int(choice_anime)-1)
      choice_anime = (int(choice_anime))
      choice_anime = choice_anime - 1
      break
  avail_link = link_scrape(choice_anime)
  if setter == 'home':
    print('Page Link already found! skipping process')
    Download(avail_link,title_anime).home_scrape()
  else:
    Download(avail_link,title_anime).scrape_ep()