from bs4 import BeautifulSoup
from bs4 import NavigableString
from bs4 import Tag
import requests

def parse_g1_new(new):
  try:
    new_image = new.findChildren("img")[0].get("src")
    content_index = 1
  except:
    new_image = "https://www.salonlfc.com/wp-content/uploads/2018/01/image-not-found-scaled.png" 
    content_index = 0
    
  new_content = new.findChildren("a")[content_index]
  url = new_content.get("href")
  titulo = new_content.findChildren("div")[0].text
  
  return (titulo.strip(), url, new_image, new)

def get_search_url(text):
  url = "https://g1.globo.com/busca/?q=" + text.replace(" ", "+")
  return url

def get_search_tree(url):
  html = requests.get(url).content
  soup = BeautifulSoup(html, 'html.parser')
  return soup

def get_next(res: (NavigableString | BeautifulSoup)):
  if (isinstance(res, BeautifulSoup)): 
    noticia = res.find("li", class_="widget--info")
  elif (isinstance(res, NavigableString) or isinstance(res, Tag)):
    noticia = res.find_next("li", class_="widget--info")
  if (noticia != None):
    return parse_g1_new(noticia)
  return None