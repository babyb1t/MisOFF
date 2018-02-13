from pymongo import MongoClient
import genius_scrapping

client = MongoClient('localhost',27017)
#client = MongoClient('mongodb://user:pass@localhost:27017/')

def getNextSequence(name,select):
    db = client.song
    if select == 1:
        ret = db.counters.find_and_modify(

            query={"_id":name},
            update={"$inc":{"seq":1}}


        )
    if select == 2:
        ret = db.counters2.find_and_modify(

            query={"_id":name},
            update={"$inc":{"seq":1}}


        )
    if select == 3:
        ret = db.counters3.find_and_modify(

            query={"_id":name},
            update={"$inc":{"seq":1}}


        )
    if select == 8:
        ret =db.counters8.find_and_modify( 
             query={"_id":name},
             update={"$inc":{"seq":1}}
        )
    return ret["seq"]



def dbs(select,song_name,artista,lyrics):
    db = client.song
    if select == 1:
        genero = db.regueton
        gen = 'regueton'
    if select == 2:
        genero = db.pop_es
        gen = 'pop en español'
    if select == 3:
        genero = db.romantica
        gen = 'romantica'
    if select == 8:
        genero = db.pop
        gen = 'pop'
    if lyrics != None:
        genero.insert({"_id": getNextSequence("songId",select),
                  "Name_song":song_name,
                  "Genero":gen,
                  "Artista":artista,
                  "user_id":[],
                  "user_age":[],
                  "analisis":0,
                  "valid":0,
                  "Lyrics":lyrics
                   })




if __name__ == '__main__':
    #song_name = "q=Despacito"
    #artista = "Luis Fonsi"
    regueton = [("Échame La Culpa","Luis Fonsi & Demi Lovato"),("Perro Fiel","Shakira"), ("Criminal","Natti Natasha"),
                ("Corazón","Maluma"), ("Mi Gente (feat. Beyoncé)","J Balvin & Willy William"),("Mayores","Becky G"),
                 ("Déjate Llevar","Juan Magán"),("Despacito","Luis Fonsi"),("Súbeme La Radio","Enrique Iglesias")]

    romantica = [("Deja Que Te Bese","Alejandro Sanz"),("Espectacular","Fangoria"),("Yo Contigo, Tú Conmigo (The Gong Gong Song)","Morat"),            
                ("Míranos","Álex Ubago"),("La Llamada","Leiva")]
     
    #pop_es = [("Guerrera","C. Tangana"),("El Patio","Pablo López"),("No Vaya A Ser","Pablo Alborán"),("Saturno","Pablo Alborán"),
    pop_es =[("Invisible","Malu"),("Cómo Te Atreves","Morat"),("Espectacular","Fangoria")]
   
    #pop = [("Perfect Duet" ,"Ed Sheeran & Beyonce"), ("Havana","Camila Cabello"), ("What Lovers Do","Maroon 5"),
    #       ("Wolves","Selena Gomez & Marshmello"), ("How Long","Charlie Puth"),("New Rules","Dua Lipa"),
    #       ("Dusk Till Dawn","ZAYN"), ("Tip Toe","Jason Derulo"), ("Anywhere","Rita Ora"),("All Falls Down - K-391 Remix","Alan Walker"),
    pop =[("24K Magic","Bruno Mars"),("Rockabye","Clean Bandit"),("Don't Wanna Know","Maroon 5"),("Lost on You","LP"),("Come","Jain"),
         ("Perfect Strangers","Jonas Blue")]




   

    #regueton = [("Despacito","Luis Fonsi"), ("La Modelo","Ozuna"),
    #            ("Krippy Kush (Remix)","Farruko, Nicki Minaj & Bad Bunny"),,
    #            ("Bella y Sensual","Romeo Santos"), ("Escápate Conmigo","Wisin"), ("Sensualidad","Bad Bunny"),
    #            ("El Farsante","Ozuna"), ("Downtown","Anitta"), ("Se Preparó","Ozuna"), ("Síguelo Bailando","Ozuna"),
    #            ("Como Antes","Yandel"), ("Que Va", "Alex Sensation + Ozuna "), ("Loco Enamorado","Abraham Mateo"),
    #            ("Vuelve","Daddy Yankee"), ("Todo Comienza En La Disco","Wisin"), ("Quiero Repetir","Ozuna"),
    #            ("Amor, Amor, Amor","Jennifer Lopez"), ("La Formula","De La Ghetto"), ("Chambea","Bad Bunny"),
    #            ("3 A.M.","Jesse y Joy & Gente de Zona"), ("Explícale","Yandel"), ("Choka Choka","Ozuna"),
    #            ,("EL BAÑO","Enrique Iglesias"),("Mentira","Ana Mena")]
   # pop = [("Perfect","Ed Sheeran"),("Feel It Still","Portugal. The Man"),
   #        ("Shape of You","Ed Sheeran"),("La Bicicleta","Carlos Vives"),
   #        rap ("​​rockstar","Post Malone"), ("All Falls Down", "Kanye West" )]
   # romantica = [("Robarte Un Beso (Remix)","Carlos Vives"),("No Me Hubiera Enamorado","Cornelio Vega & Su Dinastía"),
   #              ("3 A.M.","Jesse y Joy & Gente de Zona"), ("No Vaya A Ser","Pablo Alborán"),
   #
   #              ("Too Good at Goodbyes","Sam Smith"),("Stargazing","Kygo")
   #              ("Yo Contigo, Tú Conmigo (The Gong Gong Song)","Morat"),("Versace on the Floor","Bruno Mars")]



    #for song_name, artista in regueton:
    #    dbs(1,song_name,artista,genius_scrapping.lyrics(song_name,artista))
    for song_name, artista in pop_es:
        dbs(2,song_name,artista,genius_scrapping.lyrics(song_name,artista))
    #for song_name, artista in romantica:
    #    dbs(3,song_name,artista,genius_scrapping.lyrics(song_name,artista))
    for song_name, artista in pop:
        dbs(8,song_name,artista,genius_scrapping.lyrics(song_name,artista))
