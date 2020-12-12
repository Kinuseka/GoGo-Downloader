import re, sys, requests, os
from bs4 import BeautifulSoup

def download_video(downloadofficial, d, t):
  Name = f'{t}-EP{d}.mp4'
  if os.path.isdir('Downloaded'):
    pass
  else:
    os.system("mkdir 'Downloaded'")
  options = f'-x 15 --check-certificate=false --dir=Downloaded --max-tries=7 -o "{Name}"'
  keys = f'aria2c {options} {downloadofficial}'
  print(f'FILE: {Name}')
  while True:
    try:
      os.system(keys)
      print('\t---------------------------------')
      print(f'\t\tDownloaded EP{d} ')
      print('\t---------------------------------')
      break
    except KeyboardInterrupt: 
      input('--Download paused, press any key to continue--')
  
def get_video_link(site_full, d, t): 
  r2 = requests.get(site_full)
  soup2 = BeautifulSoup(r2.content, 'html5lib')
  link_class = soup2.find('div', class_='dowload')
  download_link = link_class.find('a')
  if download_link.has_attr('href'):
    downloadofficial = download_link['href']
    download_video(downloadofficial, d, t)
  else:
    print("No link found! Report it to me ASAP :'(\nSorry for the inconvenience")

def anime_linkscrape(unlink, d, t):
  url = 'https://gogoanime.so'
  link = (f'{url}{unlink}')
  r = requests.get(link)
  soup = BeautifulSoup(r.content, 'html5lib')
  site_target = soup.find('li', class_='dowloads')
  site_link = site_target.find('a')
  if site_link.has_attr('href'):
    site_full = site_link['href']
    print(site_full)
    get_video_link(site_full, d, t)
  else:
    print("No link found! Report it to me ASAP :'(\nSorry for the inconvenience")