
import requests
from bs4 import BeautifulSoup



base_url = "http://api.genius.com"

headers = {'Authorization':'Bearer Cxf0lIhRCZxR6YEo3VFuy0_bjiPOstPH0UP9RObaOoCdYLI6svWyrOz7OlnCFj5y'}

#song_title = "q=Lake Song"
song_title ="q=Despacito"
#artist_name = "The Decemberists"
artist_name = "Luis Fonsi"
def lyrics_from_song_api_path(song_api_path):
  song_url = base_url + song_api_path
  response = requests.get(song_url, headers=headers)
  json = response.json()
  path = json["response"]["song"]["path"]
  #gotta go regular html scraping... come on Genius
  page_url = "http://genius.com" + path
  page = requests.get(page_url)
  html = BeautifulSoup(page.text, "html.parser")
  #remove script tags that they put in the middle of the lyrics
  [h.extract() for h in html('script')]
  #at least Genius is nice and has a tag called 'lyrics'!
  lyrics = html.find("div", class_="lyrics").get_text() #updated css where the lyrics are based in HTML
  return lyrics
#data=data

def lyrics(song_title, artist_name):
  search_url = base_url + "/search?"
  data = {'q': song_title}
  response = requests.get(search_url , data , headers=headers)

  json = response.json()
  song_info = None

  for hit in json["response"]["hits"]:
    if hit["result"]["primary_artist"]["name"] == artist_name:
      song_info = hit
      break
  if song_info:
    song_api_path = song_info["result"]["api_path"]
    return lyrics_from_song_api_path(song_api_path)
  else:
    print("lyrics not found {}".format(song_title))

