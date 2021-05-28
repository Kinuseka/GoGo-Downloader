import re, sys
import goEmbed
from gAPi import gogo
goScrape = gogo
avail_link = ""
usera = {'User-Agent':'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'}
class Download:
  def __init__(self, avail_link, title):
    self.link = avail_link
    self.t = title
  def scrape_ep(self):
    print("Episodes loading...")
    proc = goScrape.Process(self.link)
    link = proc.full_link()
    episode_total = goScrape.Episode(link).episode()
    ep_sodeint = int(episode_total)
    episode_header = 'episodes'
    if ep_sodeint < 2:
      episode_header = 'episode'
    if ep_sodeint == 0:
      print('\t---------------------------------')
      print('\tFound no episodes AT ALL!')
      print('\t---------------------------------')
      print("The anime might be still upcoming or has not been uploaded to the site")
      sys.exit()
    print('\t---------------------------------')
    print('\tFound', episode_total, episode_header, 'in total!')
    print('\t---------------------------------')
    print("=== Bulk download setup ===")
    while True:
      dl_bulkst = 0
      dl_bulken = 0
      dl_bulkst = int(input("Start from episode:"))
      dl_bulken = int(input("Stop to episode:"))
      if dl_bulkst < 1:
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
    for d in range(dl_bulkst,(dl_bulken+1)):
      dl_ep_fulllink = proc.full_link(command=True,val=d)
      print('\t---------------------------------')
      print(f'\t\tDownloading EP{d}')
      print('\t---------------------------------')
      goEmbed.anime_linkscrape(dl_ep_fulllink, d,self.t)
      if d == dl_bulken:
        print('\t-Process finished-')
        sys.exit()
  def home_scrape(self):
    Prolink = goScrape.Process(self.link)
    link = Prolink.full_link()
    d = Prolink.Home_ep(content=link)
    print('\t---------------------------------')
    print(f'\t\tDownloading EP{d}')
    print('\t---------------------------------')
    goEmbed.anime_linkscrape(link, d, self.t)
    print('\t-Process finished-')
    sys.exit()
def scrape_web(url, u_copy,**d):
  goapi = goScrape.Anime(url)
  checker_title = goapi.List()
  if d:
    if d["setter"] == "home":
      setter = "home"
    else:
      setter = "not"
  else:
    setter = "not"
  #-------page searcher-----------v#
  try:
    page_a = goapi.Page_total(val='total')
    page_s = goapi.Page_total(val='selected')
    page_len = (int(page_a) - 1)
  except BaseException as e: 
    page_a = 1
    page_s = 1
    page_len = 'no'
  if page_len == 'no':
    page_last = page_a
    page_on = page_s
  else:
    page_on = int(page_s)
    page_last = int(page_a)
  #-------page searcher-----------^#
  if setter == 'home':
    checker_episodes = goapi.List(command=True)
  def link_scrape(value):
    v = goapi.Link()
    proc = v[value]
    return(proc)
  def title_name(number):
    return(checker_title[int(number)].text.strip())
  def show_list(max_an, val1, val2):
    x = 0
    y = 5
    maxi = max_an
    if val1 != 0:
      y += val1
    if val2 != 0:
      x += val2
    if max_an < 5:
      y = max_an
    if y > maxi:
      d = y - max_an
      y -= d
      #if y > 29: #(only for 9anime, not supported)
        #print('Max reached')
    for x in range(x,y):
      print(f'\t{x+1}.) {checker_title[int(x)].text.strip()}')
      if setter == 'home':
        print(f'\t>{checker_episodes[int(x)].text.strip()}')
      print('\t---------------------------------')
  max_an = goapi.Len_list()
  var1 = 0
  var2 = 0 
  perm = 'yes'
  if re.search('(search)', url):
    perset = '&'
  else:
    perset = '?'
  if max_an == 0:
    page_on = 'N'
    page_last = 'A'
  print('\t*************RESULTS*************')
  print(f'\tPage: {page_on}/{page_last}')
  print('\t=================================')
  show_list(max_an, var1, var2)
  print('There are', max_an,'anime/s found')
  if max_an == 0:
    print('Try making your keywords more specific')
    sys.exit()
  if max_an > 5:
    print('do ">" to see more list')
  if page_last > 1:
    print('do >> or << to switch pages')
    
  xintmax_an = int(max_an)
  while True:
    choice_anime = input("Select anime:")
    try:
      xchoice = int(choice_anime)
    except:
      pass
    if choice_anime == ">":
      var1 += 5
      var2 += 5
      show_list(max_an, var1, var2)
    elif choice_anime == ">>":
      if page_on == page_last:
        continue
      else:
        paged = page_on + 1
        url = (f'{u_copy}{perset}page={paged}')
        print('Changing page..')
        scrape_web(url, u_copy, setter=setter)
    elif choice_anime == "<<":
      if page_on == 1:
        continue
      else:
        paged = page_on - 1
        url = (f'{u_copy}{perset}page={paged}')
        print('Changing page..')
        scrape_web(url, u_copy, setter=setter)
    try:
      if xchoice > xintmax_an:
        print('Input exceeds limit!')
      elif xchoice <= 0:
        print('Too small')
      else:
        title_anime = title_name(int(choice_anime)-1)
        choice_anime = (int(choice_anime))
        choice_anime = choice_anime - 1
        break
    except:
      continue
  avail_link = link_scrape(choice_anime)
  if setter == 'home':
    print('Page Link already found! skipping process')
    Download(avail_link,title_anime).home_scrape()
  else:
    Download(avail_link,title_anime).scrape_ep()