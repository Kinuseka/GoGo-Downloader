import requests, re, sys
from bs4 import BeautifulSoup
import NineScraper
url_temp = 'http://gogoanime.so'
  
class Major:
  def __init__(self, keyword):
    self.key = keyword
  def Link_builder(self):
    var = (self.key.replace(" ", "%20"))
    url_fixed = (f'{url_temp}//search.html?keyword={var}')
    return(url_fixed)
def main():
  setter = 'not'
  print('\t -----------------------------')
  print('\t\tGoGo Downloader v1.0')
  print('\t -----------------------------')
  print("\tYou can do >h to see GoGo's home recommendations")
  keyword = input("\tEnter title name:")
  if keyword == ">h":
    setter = 'home'
    print('\tLoading (restart if it took >10s)')
    start_scraping = NineScraper.scrape_web(url_temp, setter)
  url = Major(keyword).Link_builder()
  print('\tLoading (restart if it took >10s)')
  start_scraping = NineScraper.scrape_web(url, setter)
  #commitment
main()