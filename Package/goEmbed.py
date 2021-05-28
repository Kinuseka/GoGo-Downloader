debug = False
import re, sys, requests, os
from bs4 import BeautifulSoup
from gAPi import Qselect, UCnfg, FileCorrector

config = UCnfg.Config()

def download_video(downloadofficial):
  processed_qual = qual_name.replace("-mp4", "")
  dine = "{0:0=3d}".format(int(di))
  Name = f"{title}-EP{dine}{processed_qual}.mp4"
  root_directory = (os.path.join(os.getcwd(), 'Downloaded'))
  if not os.path.isdir(root_directory): os.mkdir(root_directory)
  file_directory = (root_directory+'/'+title)
  if not os.path.isdir(f'{root_directory}/{title}'): os.mkdir(f'{root_directory}/{title}')
  value = 1
  trigger = False
  while os.path.isfile(f'{file_directory}/{Name}') and not os.path.isfile(f'{file_directory}/{Name}.aria2'):
    Name = f'{title}-EP{dine}{processed_qual}.{value}.mp4'
    value +=1
    trigger = True
  if trigger:
    print("File already exists, will be renaming to:")
  options = f"-x 15 --dir='{file_directory}' --check-certificate=false --max-tries=7 --out='{Name}'"
  keys = f"aria2c {options} '{downloadofficial}'"
  print(f'FILE: {Name}')
  while True:
    try:
      exit = os.system(keys)
      if os.path.isfile(f'{file_directory}/{Name}') and exit == 0:
        print('\t---------------------------------')
        print(f'\t\tDownloaded EP{di} ')
        print('\t---------------------------------')
        break
      else:
        print('\t---------------------------------')
        print('\t\tAn error has occured')
        print('\t---------------------------------')
        print(f'Exit code status: {exit}')
        print("Could be a false positive, please check the downloaded file.")
        break
    except KeyboardInterrupt: 
      try:
        input('--Download paused, click enter to continue--\n[or do ctrl+c again to cancel]')
      except KeyboardInterrupt:
        while True:
          chose=input('Would you like to delete the partially downloaded file? (y/n)').lower().strip()
          if chose == "y":
            delete = True
            break
          elif chose == "n":
            delete = False
            break
          else:
            continue
        if delete:
          print('cancelling download..')
          if os.path.isfile(f'{file_directory}/{Name}'):
            os.remove(f'{file_directory}/{Name}')
            print('√ removed unfinished file')
            os.remove(f'{file_directory}/{Name}.aria2')
            print('√ removed cache file')
          else: 
            print('No file to delete')
          if not os.listdir(file_directory): 
            print('Folder empty, will delete')
            os.rmdir(file_directory)
        print('--Process Killed--')
        sys.exit()
        

def get_video_link(site_full): 
  global qual_name
  r2 = requests.get(site_full)
  soup2 = BeautifulSoup(r2.content, 'html.parser')
  link_found = soup2.find_all('div', class_='dowload')
  linklen = len(link_found)
  qualityfind = config.return_data
  if qualityfind(3) == 'on':
    quality1 = qualityfind(1).upper()
    link_class, qual_name = Qselect.Quality.quality(quality1,link_found,qualityfind(2))
  else:
    qual_name = "-mp4"
    link_class = link_found[0]
  try:
    download_link = link_class.find('a')
  except AttributeError as error:
    if debug == True:
      print(error)
    download_link = link_class
  try:
    downloadofficial = download_link['href']
    download_video(downloadofficial)
  except KeyError as error:
    if debug == True:
      print(error)
    print("Error has occurred on goEmbed.py! Report it to me ASAP :'(\nSorry for the inconvenience")

def anime_linkscrape(link, d, t):
  global di, title
  file_correct = FileCorrector.Getname(t)
  corrected = file_correct.correct()
  title = corrected
  di = d 
  
  r = requests.get(link)
  soup = BeautifulSoup(r.content, 'html.parser')
  site_target = soup.find('li', class_='dowloads')
  site_link = site_target.find('a')
  if site_link.has_attr('href'):
    site_full = site_link['href']
    get_video_link(site_full)
  else:
    print("No link found! Report it to me ASAP :'(\nSorry for the inconvenience")
    
if __name__ == "__main__":
  global di
  global title
  di = 'test'
  title = 'test'
  site_full=input('Enter link:')
  try:
    get_video_link(site_full)
  except Exception as error:
    print(error)
    print('Invalid')
    