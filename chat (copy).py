#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to Telegram messages.
This is built on the API wrapper, see echobot2.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
"""
import logging
import read_lyrics
from telegram import Bot
from telegram.error import NetworkError, Unauthorized
from time import sleep
from pymongo import MongoClient

client = MongoClient('localhost',27017)
#client = MongoClient('mongodb://user:pass@localhost:27017/')


update_id = None


def main():
    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token
   

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def user_sexo(update):
    db = client.users
    posts = db.users 
    posts.update({"user_id":update.message.chat.id},{"$set":{"Sexo":update.message.text}})#update.message.text
    if update.message.text == "Chico":
       posts.update({"user_id":update.message.chat.id},{"$set":{"Codigo_sexo":0}})
    else:
       posts.update({"user_id":update.message.chat.id},{"$set":{"Codigo_sexo":1}})

def user_age(update):
  db = client.users
  posts = db.users
  if posts.find({"user_id": update.message.chat.id}).count() == 0:

    post = {"update_id": update.update_id,
            "user_id": update.message.chat.id,
            "user_age": update.message.text,
            "date": update.message.date

            }
    posts.insert_one(post).inserted_id





def has_age(update):
  db = client.users
  posts =db.users
  if posts.find({"user_id": update.message.chat.id}).count() > 0:
    #return posts.find_one({"user_id":update.message.chat.id})
    return True
  else:
    return False

#def insert_estro(update, estro):
#   estrofas = ''
#   letras, keys = read_lyrics.lyrics(update)
#   for i in estro:
#      #estrofas.append(letras[keys[i - 1]])
#      estrofas += "{}".format(i) + "\n" + letras[keys[i-1]] 
#   return estrofas


def genero_cancion(song_id):
  if song_id >= 10000 and song_id <= 20000:
    genero = "reguetón"
  if song_id >= 20000 and song_id <= 30000:
    genero = "pop"
  if song_id >= 30000 and song_id <= 40000:
    genero = "romántica"
  return genero

def estereotipo(update, song_name, estro = 0):
    db = client.users
    songdb = client.song
    tmp = songdb.tmp
    posts = db.users
    if estro != 0:
    
      posts.update({"user_id":  update.message.chat.id}, {"$push": {"analisis":{ "name":song_name,
                                                                   "genero":genero_cancion(tmp.find_one({'user_id':update.message.chat.id})["songId"]),
                                                                               "codigo_parrafo_estereotipo": estro,
                                                                               #"texto_parrafo_estereotipo":insert_estro(update,estro),
                                                                               "Grado_estereotipo":int(update.message.text),
                                                                          "Codigo_cancion": tmp.find_one({'user_id':update.message.chat.id})["songId"],
                                                                               "codigo_parrafo_roles":'',
                                                                               #"texto_parrafo_roles":'',
                                                                               "Grado_roles":'',
                                                                               "codigo_parrafo_poder":'',
                                                                               #"texto_parrafo_poder":'',
                                                                               "Grado_poder":'',
                                                                               "codigo_parrafo_cuerpo":'',
                                                                               #"texto_parrafo_cuerpo":'',  
                                                                               "Grado_cuerpo":'',
                                                                               "Pregunta_general":'',
                                                                               
                                                                               "Grado_general":''
                                                                                }
                                                                     }
                                                           })
     
    else:
     posts.update({"user_id":  update.message.chat.id}, {"$push": {"analisis":{ "name":song_name,
                                                                   "genero":genero_cancion(tmp.find_one({'user_id':update.message.chat.id})["songId"]),
                                                                               "codigo_parrafo_estereotipo":estro,
                                                                               #"texto_parrafo_estereotipo":update.message.text,
                                                                               "Grado_estereotipo":estro,
                                                                           "Codigo_cancion":tmp.find_one({'user_id':update.message.chat.id})["songId"],
                                                                               "codigo_parrafo_roles":'',
                                                                               #"texto_parrafo_roles":'',
                                                                               "Grado_roles":'',
                                                                               "codigo_parrafo_poder":'',
                                                                               #"texto_parrafo_poder":'',
                                                                               "Grado_poder":'',
                                                                               "codigo_parrafo_cuerpo":'',
                                                                               #"texto_parrafo_cuerpo":'',  
                                                                               "Grado_cuerpo":'',
                                                                               "Pregunta_general":'',
                                                                               "Grado_general":''
                                                                                }
                                                                     }
                                                           })

def roles(update,song_name,estro = 0):
    db = client.users
    posts = db.users
    if estro != 0:
      posts.update_one({"user_id":  update.message.chat.id},
                       {"$set": {"analisis.$[elemt].codigo_parrafo_roles": estro,
                                 #"analisis.$[elemt].texto_parrafo_roles":insert_estro(update,estro),
                                 "analisis.$[elemt].Grado_roles":int(update.message.text)
                                 }}, array_filters=[{"elemt.name":{"$eq":song_name}}]  )
    else:
      posts.update_one({"user_id":  update.message.chat.id},
                       {"$set": {"analisis.$[elemt].codigo_parrafo_roles": estro,
                                 #"analisis.$[elemt].texto_parrafo_roles":update.message.text,
                                 "analisis.$[elemt].Grado_roles":0
                                }}, array_filters=[{"elemt.name":{"$eq":song_name}}])




def poder(update, song_name, estro = 0):
    db = client.users
    posts = db.users
    if estro != 0:
       posts.update_one({"user_id":  update.message.chat.id},
                       {"$set": {"analisis.$[elemt].codigo_parrafo_poder":estro,
                                 #"analisis.$[elemt].texto_parrafo_poder":insert_estro(update,estro),
                                 "analisis.$[elemt].Grado_poder":int(update.message.text)
                                 }}, array_filters=[{"elemt.name":{"$eq":song_name}}])
    else:
      posts.update_one({"user_id":  update.message.chat.id},
                       {"$set": {"analisis.$[elemt].codigo_parrafo_poder":estro,
                                 #"analisis.$[elemt].texto_parrafo_poder":update.message.text,
                                 "analisis.$[elemt].Grado_poder":0
                                }}, array_filters=[{"elemt.name":{"$eq":song_name}}])

def cuerpo(update, song_name, estro = 0):
    db = client.users
    posts = db.users
    if estro != 0:
      posts.update_one({"user_id":  update.message.chat.id},
                       {"$set": {"analisis.$[elemt].codigo_parrafo_cuerpo":estro,
                                 #"analisis.$[elemt].texto_parrafo_cuerpo":insert_estro(update,estro),
                                 "analisis.$[elemt].Grado_cuerpo":int(update.message.text)
                                 }}, array_filters=[{"elemt.name":{"$eq":song_name}}])
    else:
      posts.update_one({"user_id":  update.message.chat.id},
                       {"$set": {"analisis.$[elemt].codigo_parrafo_cuerpo":estro,
                                 #"analisis.$[elemt].texto_parrafo_cuerpo":update.message.text,
                                 "analisis.$[elemt].Grado_cuerpo":0
                                }}, array_filters=[{"elemt.name":{"$eq":song_name}}])

def general(update, song_name,  estro = 0):
    db = client.users
    posts = db.users
    if estro != 0:
      posts.update_one({"user_id":  update.message.chat.id},
                       {"$set": {"analisis.$[elemt].Pregunta_general":estro,
                                 "analisis.$[elemt].Grado_general":int(update.message.text)
                                 }}, array_filters=[{"elemt.name":{"$eq":song_name}}])
    else:
      posts.update_one({"user_id":  update.message.chat.id},
                       {"$set": {"analisis.$[elemt].Pregunta_general": update.message.text,
                                 "analisis.$[elemt].Grado_general":0
                                }}, array_filters=[{"elemt.name":{"$eq":song_name}}])



if __name__ == '__main__':
  main()
