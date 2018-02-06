import re
import sys
from pymongo import MongoClient
from random import randint
#client = MongoClient('localhost',27017)
client = MongoClient('mongodb://user:pass@localhost:27017/')

db = client.song

init = 0

def musical_genre(select):
  global  db, init
  if select == 'pop':
    genero = db.pop
    init = 20000
  if select == 'reguetón':
    genero = db.regueton
    init = 10000
  if select == 'romántica':
    genero = db.romantica
    init = 30000
  return genero


def song_name(update):
  tmp = db.tmp
  song_id = tmp.find_one({"user_id":update.message.chat.id})["songId"]
  genero = musical_genre(tmp.find_one({"user_id":update.message.chat.id})["genero"])
  name = genero.find_one({"_id":song_id})["Name_song"]

  return name


def new_song(update): #make sure that the user is analysing a song never analyzed before
  global init
  anterior_songId = 0
  analyzed = 1
  tmp = db.tmp
  if tmp.find({"user_id":update.message.chat.id}).count()>0:
     anterior_songId = tmp.find_one({"user_id":update.message.chat.id})["songId"]
  drop(update)
  tmp.insert({"user_id":update.message.chat.id,
              "genero":update.message.text})
  
  genero = musical_genre(update.message.text)
  i=0
  while  analyzed: #mientras este analizada la cancion buscara otra
    
    song_id = randint(init,init + genero.find().count() - 1)
    print(init, genero.find().count())
    i+=1
    if i == 40:
      song_id = ''
      return 1, ''

    ####song test #### cambiar
    print(song_id)
    users_id = genero.find_one({'_id':song_id})["user_id"]
    valid = genero.find_one({'_id':song_id})["valid"]
    analyzed=0
    if valid !=1:
      for user_id in users_id:
        if user_id == update.message.chat.id or song_id == anterior_songId:
           analyzed = 1  
      if analyzed == 0:
        tmp.update({"user_id":update.message.chat.id},{"$set":{"songId":song_id}})
        return 0 




def analyzed(update):
  #### song test cambiar
  
  posts = client.users.users
  tmp = client.song.tmp
  song_id = tmp.find_one({"user_id":update.message.chat.id})["songId"]
  genero = musical_genre(tmp.find_one({"user_id":update.message.chat.id})["genero"])
  age = posts.find_one({"user_id":update.message.chat.id})["user_age"]

  genero.update({"_id":song_id},{"$addToSet":{"user_id":update.message.chat.id}})
  genero.update({"_id":song_id},{"$push":{"user_age":{"$each":[int(age)]}}})
  genero.update({"_id":song_id},{"$inc":{"analisis":1}})
  data = genero.find_one({"_id":song_id})["analisis"]
  if data > 4:
    genero.update({"_id":song_id},{"$addToSet":{"valid":1}})

def drop(update):
   db.tmp.remove({"user_id":update.message.chat.id})

def reader(update):
   tmp = db.tmp
   song_id = tmp.find_one({"user_id":update.message.chat.id})["songId"]
   genero = musical_genre(tmp.find_one({"user_id":update.message.chat.id})["genero"])
   data = genero.find_one({"_id":song_id})["Lyrics"]

   return data

def sanity(update):
    tmp = db.tmp
    if tmp.find({"user_id":update.message.chat.id}).count() > 0:
        return True
    else:
        return False 

#esta funcion devuelve la letra de de coro estrofa precoro y outro y su valor clave.
def lyrics(update):
   
   letra = {}
   keys = list()
   #lyrica = open("./lyrica_daddy.txt",'r')
   #data=lyrica.read().replace('\n', ' ')

   data = reader(update)
   #data = reader(update,song_id)
   lista = re.findall(r"(?<=])[ê!-?'¡¿\s,a-zA-Z()áéíóúÁÉÍÓÚñÑçã]*",data)
   titulos = re.findall(r"\[[çã!-?'¡¿\s,a-zA-Z()áéíóúÁÉÍÓÚñÑ]+\]",data)
   for i in range(len(lista)):
      if not titulos[i] in letra:
         letra[titulos[i]] = lista[i]
      #print("\n%s"%titulos[i])
      #print("%s\n"%lista[i])
   for key in letra:
    tag=re.findall(r"(outro|intro|Translation|instrumental|(\[en\]))",key, flags = re.I)
    
    
    if tag == []:
      #print ('%s\n%s' %(key,letra[key]))
      
      #if len(letra[key].split()) > 11:
      
      #[Coro: Instrumental] outro intro translation
      keys.append(key)
   
   #lyrica.close()
   return letra , keys




if __name__=='__main__':
  #for i in range(0, )
  lyrics('pop',6)
