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

def parse_fsp_new(new):
  try:
    new_image = new.findChildren("img")[0].get("src")
    content_index = 1
  except:
    new_image = "https://www.salonlfc.com/wp-content/uploads/2018/01/image-not-found-scaled.png" 
    content_index = 0
    
  new_content = new.findChildren("a")[content_index]
  url = new_content.get("href")
  titulo = new_content.findChildren("h2")[0].text
  
  return (titulo.strip(), url, new_image, new)

def get_search_url(text):
  url = "https://g1.globo.com/busca/?q=" + text.replace(" ", "+")
  url2 = "https://search.folha.uol.com.br/?q=" + text.replace(" ", "+") + "&site=todos"
  return url,url2

def get_search_tree(url):
  html = requests.get(url).content
  soup = BeautifulSoup(html, 'html.parser')
  return soup

def get_next_g1(res: (NavigableString | BeautifulSoup)):
  if (isinstance(res, BeautifulSoup)): 
    noticia = res.find("li", class_="widget--info")
  elif (isinstance(res, NavigableString) or isinstance(res, Tag)):
    noticia = res.find_next("li", class_="widget--info")
  if (noticia != None):
    return parse_g1_new(noticia)
  return None

def get_next_fsp(res: (NavigableString | BeautifulSoup)):
  if (isinstance(res, BeautifulSoup)): 
    noticia = res.find("li", class_="c-headline")
  elif (isinstance(res, NavigableString) or isinstance(res, Tag)):
    noticia = res.find_next("li", class_="c-headline")
  if (noticia != None):
    return parse_fsp_new(noticia)
  return None


