debug = False
import requests, re, sys, os
from gAPi import UCnfg, gogo
from bs4 import BeautifulSoup
import NineScraper
version_id = ['GoGo Downloader v1.34', 'V1.34']
select_option =''
def check_config():
  config = UCnfg.Config()
  start = config.checker()
check_config()

url_temp= UCnfg.Config().Domain()
class Major:
  def __init__(self, keyword):
    self.key = keyword
  def Link_builder(self):
    var = (self.key.replace(" ", "%20"))
    return(f'{url_temp}//search.html?keyword={var}')
def Genre_select():
  go = gogo.Anime(url_temp)
  genre = go.Genre_list()
  while True:
    select_option = input('\tSelect genre:')
    try:
      genre_link = go.Genre_link(select_option,genre)
      genrefied_link = (f'{url_temp}{genre_link}')
      return(genrefied_link)
      break
    except BaseException as error:
      if debug == True:
        print(error)
      continue
  
    
def main():
  print(f'\t>>Server:{url_temp}')
  print('\t  -----------------------------')
  print(f'\t\t{version_id[0]}')
  print('\t  -----------------------------')
  print("\tType '>h' to see GoGo's latest releases")
  print("\tType '>g' to select genre")
  keyword = input("\tEnter title/command:")
  if keyword == ">h":
    print('\tLoading (restart if it took >10s)')
    url_c = url_temp
    start_scraping = NineScraper.scrape_web(url_temp, url_c,setter="home")
    sys.exit()
  elif keyword == ">g":
    print('\tGetting genre list..')
    start_genre = Genre_select()
    start_scraping = NineScraper.scrape_web(start_genre, start_genre)
    sys.exit()
  url = Major(keyword).Link_builder()
  url_c = url
  print('\tLoading (restart if it took >10s)')
  start_scraping = NineScraper.scrape_web(url, url_c)
def check_update():
  label = ''
  prelabel = ''
  ident = ''
  try:
    version = requests.get('http://Kinuseka.github.io/goupdate', timeout=4)
    soup = BeautifulSoup(version.content, 'html.parser')
    vers = soup.find('div', class_="latest_version").text.strip()
    pre = soup.find('div', class_="pre_version").text.strip()
  except Exception as ree:
    print('Something went wrong while checking the version\n'
    '----------Error log-----------\n'
    f'{ree}'
    '\n-----------------------------')
    return
  #---parse data ^ v
  if pre == version_id[1]:
    ident = 'prerelease'
    print(f'Prerelease version\nVerson: {pre}')
  if vers == version_id[1]:
    ident = 'latest'
    print(f'Latest version\nVersion: {vers}')
  if re.search('prerelease', pre):
    vers_pre = float(pre.replace('V', '').replace('-prerelease', ''))
  vers_num = float(vers.replace('V', ''))
  if re.search('prerelease', version_id[1]):
    id_num = float(version_id[1].replace('V', '').replace('-prerelease', ''))
  else:
    id_num = float(version_id[1].replace('V', ''))
  if vers_num < id_num:
    label = 'unr'
  if vers_pre > id_num:
    prelabel = 'down'
  #---
  #---Use data
  if re.search('prerelease', pre):
    if prelabel == 'down':
        print('\t==NEW BETA VERSION FOUND==\n'
        f'\tVersion: {pre}\n'
        '\t===================================='
        )
  if label == 'unr':
    if ident != 'prerelease':
      print('\t====Unreleased version====\n'
        f'\tCurrent version on github: {vers}')
  else:
    if vers != version_id[1]:
      print('\t==NEW VERSION FOUND PLEASE UPDATE!==\n'
      f'\tVersion: {vers}\n'
      '\t====================================')
  try:
    message = soup.find('div', class_='alert_mass').text.strip()
    print(f'''[Announcements]:
{message}''')
  except BaseException as E:
    if (debug == True):
      print(E)
    pass
check_update()
main()