#se importa la funcion random
import random
#se importa la funcion randint
from random import randint
#Se crea un dicionario con las categorias y las preguntas en listas dentro del dicionario 
categorias = { "cetys":["¿Qué significa cetys?", "¿Donde puedes pedir asesorías?","¿Cuántas veces puedes intentar pasar una materia?","¿Cuál es el promedio mínimo aprobatorio ?","¿Cuántas salas de computadoras tiene cetys?","¿En qué edificio haces los pagos de colegiatura ?", "¿Cuál es el primer nombre  del coordinador de ingenierías en cetys ?","¿Cuántas veces puedes hacer un extraordinario?","¿ Primer nombre del Coordinador de ICC?","¿Cuantos modulos tiene el programa de ingles?"],
               "python":["¿Se puede modificar un tuple?", "Menciona una condicional", "¿Quien invento python?","¿Se puede modificar string?","¿Se puede modificar una lista?","¿Con qué número empiezan el posicionamiento en las listas en python?","Simbolo para multiplicar en python","Simbolo para restar en python","Simbolo para dividir en python","En qué año fue creado python"],
               "geografia":["¿Capital de Alemania?", "¿Capital de Belgica?", "¿Capital de Austria?","¿Capital de Francia?","¿Capital de Irlanda?","¿Capital de Afganistan?","¿Capital de Banglades?","¿Capital de China?","¿Capital de Corea del sur?","¿Capital de Japon?"],
               "musica":["Instrumento musical popular que tiene seis cuerdas y se toca rasgueando las cuerdas","Instrumento principal que tocaba Vivaldi","Instrumento principal que tocaba Beethoven","En qué año nació Beethoven","Nombre de la banda que formaba John Lennon","El video de más visto en youtube 18 de Noviembre","¿Quien gano la voz México 2014?","¿Cual es el álbum más vendido en la historia?","¿Que artista tiene más grammys?","¿Año en que murió John Lennon?"],
               "cine":["Primer nombre de la persona que ha ganado más oscars", "Actriz que salió con un presidente de estados unidos, que después fue asesinado.","Compositor que hace la música de star wars.","Pelicula más taquillera.","Compositor de la música del señor de los anillos.","Director de la trilogía del caballero de la noche.","Director mexicano de una pelicula de harry potter."," El protagonista de esta pelicula es Neo un hacker.","El protagonista de esta pelicula es un policía llamado John McClane.","La pelicula animada más taquillera."],
               "ingenieria en ciencias computacionales": ["¿Quien es el padre de las ciencias computacionales?", "¿En qué año nació Alan Turing?", "¿Cual es producto de la ingeniería  ciencias computacionales?","Es el cerebro de la computadora.","¿Cual fue la primera computadora?","El sistema binario usa elevaciones de:"," ¿En que año salio eniac?","¿Que significa IBM?","Fundador de Windows","¿Qué significa ASCII?"],
               "video juegos":["Nombre del protagonista de “The Legend of Zelda Ocarina of Time”","Creador de la saga de Metal Gear Solid.","Estudio que hizo Call of duty 4 Modern Warfare.","Creador de la franquicia de “The Legend of Zelda”","Personaje más roto en Smash bros brawl."," Serie de videojuegos donde los All-Stars de nintendo pelean por mandar al oponente fuera del campo de batalla.","Erizo azul que viaja a la velocidad del sonido.","Es el personaje más icónico de los videojuegos, la mascota de Nintendo.","Ex-Presidente de Nintendo, recientemente fallecido.","Caza recompensas espacial con ADN chozo"],
               "breaking bad":["¿Como se llamaba la novia de Jesse?","¿Como se llama el dueño de pollos hermanos?","¿Como se llama la compañía que utilizan para elaborar metanfetaminas?","¿Como se llama la primera persona que mata Walter White?","¿Como se llama la bebita de Walter White?","¿Que coleciona Hank?"," El primer compañero de laboratorio de walter white","En la última temporada sobre que discute skinny pete, Bayer.","Con que planta envena walter white a bruck.","Como se llama el abogado walter white, Jesse."],
               "animales":["Animal domesticado que tiene cuatro patas y ladra.","Animal que puede ser domesticado y es felino.","Animal más inteligente acuático.","Animal con gran cuello largo.","Animal grande, blanco y negro, que come bambú.","Animal que comé hormigas.","Cual es el animal más rápido?"," Animal que mato a Steve Irwin."," Animal que han hecho una trilogía del este.","¿Cual es el rey de la selva?"],
               "superheroes":["¿Cual la identidad secreta de superman?","¿Cual es la identidad secreta de Flash?","¿Cual es el antagonista de batman que está pintado como un payaso?","¿Quien entrena a bruce wayne?","¿Cual es la debilidad de superman?","¿Cual es la identidad secreta de Batman?","¿Cual es el nombre del principal interes romantico de Peter Parker?","Enemigo del hombre araña que tiene 4 brazos roboticos.", "Enemigo de batman que dice acertijos.","Asistente no humano de Iron Man"] }
#se crea una lista con las respuestas en la posicion 0 esta las respuestas de cetys y esta en orden de el dicionario. 
respuestas = [["centro de ensenanza tecnica y superior" ,"cede", "3", "7","6","administrativo","fabian","3","adan","5"],
              ["no","if","guido van rossum","no","si","0","*","-","/","1991"],
              ["berlin","bruselas","viena","paris","dublin","kabul","daca","pekin","seul","tokio"],
              ["guitarra","violin","piano","1770","the beatles","gangnam style","guido","thriller","georg solti","1980"],
              ["walt","marilyn monroe","john williams","avatar","howard shore","christopher nolan","alfonso cuaron","matrix","die hard","frozen"],
              ["alan turing","1912","la tecnologia", "procesador", "eniac", "2", "1946","international business machines", "bill gates", "american standard code for information interchange"],
              ["link","hideo kojima","activision","shigeru miyamoto","metal knight","super smash bros","sonic","mario","satoru iwata","samus"],
              ["jane","gus fringe","vamonos pest","domingo","holly","minerales","gale","teletransportacion", "lily of the valley", "saul goodman"],
              ["perro","gato","delfin","jirafa","panda","oso hormiguero","halcon peregrino","mantaraya","tiburon","leon"],
              ["clark kent","barry allen", "joker","ras al ghul", "kryptonita", "bruce wayne", "mary jane", "doctor octopus", "el acertijo", "jarvis"]]
#Se crea dos listas con las categorias. cAtegoriasMostrar de esa lista se sacan y se insertan en listado 2 y listado 3
cAtegoriasMostrar = ["cetys", "python", "geografia" , "musica", "cine", "ingenieria en ciencias computacionales", "video juegos", "breaking bad", "animales", "superheroes"]
#Con esta lista se compara la posicion de la pregunta para sacar la respuesta. Esta lista no se modifica
categoriasS = ["cetys", "python", "geografia" , "musica", "cine", "ingenieria en ciencias computacionales", "video juegos", "breaking bad", "animales", "superheroes"]
#Esta lista es de las cantidades dependiendo en que lugar este es las posibles cantidades que tendra. Se ira quitando cuando el usuario ingrese una.
Lista = [["200", "400", "600", "800", "1000"],["200","400","600","800","1000"],["200","400","600","800","1000"],["200","400","600","800","1000"],["200","400","600","800","1000"],["200","400","600","800","1000"]]
#La primera lista2 es para que el usuario la vea que salio en el random
listado2 = []
#esta lista "listado3" es para saber la posicion en la cual las cantidades se pondran. Cuando una categoria este terminda, la "listado2" se mueve es por eso que el "listado3" es para que cuando se acabe una categoria pueda seguir mostrando las demas cantidades y no te imprima una posicion que esta en blanco. 
listado3 = []
#el i es para contar seis veces para el random de las categorias
i=0
#la x es para contar los turnos del usuario, cuando el usuairo ingresa la respeusta no importa si es correcta o incorrecta se tomara como un turno.
x= 0
#es para sumar el puntaje
Puntaje = 0
#cada vez que el usuario eliga una categoria se agregara a esta lista cuando el mismo nombre salga 5 veces en la lista la categoria sera removida.
lista23=[]
lista55=["rafa"]
afirmacion1 = False
afirmacion2 = False
#el for del random de categorias
for i in  range(6):
    cat = random.randint(0,len(cAtegoriasMostrar)-1)
    listado = cAtegoriasMostrar [cat] #random
    listado2.append(listado)#se agrega en esta lista el random 
    listado3.append(listado)#al igual que en esta.
    cAtegoriasMostrar.remove(listado)# se remueve de esa lista lo del radom para que no salga repetida
    i+=1
#el while de los 30 turnos
while x < 30:
    #se imprime la que salio el random y la cual cuando se acabe los puntos se ira quitando las categorias
    print("  |  ".join(listado2))
    print("Tu puntaje es: ",Puntaje)# se imprime el puntaje
    afirmacion1 = False
    afirmacion2 = False
# el while para elegir la categoria y que este en el listado2    
    if i == 6:
        while afirmacion1 == False:
            usuario = input("\nElige la categoria \n")
            usuario = usuario.lower()
            if usuario in listado2:
                afirmacion1 = True
#el siguiente paso                
    if len(cAtegoriasMostrar) and len(Lista):
        indice2 = listado3.index(usuario)#saber la posicion en numero de lo que el usuario ingreso y con eso se imprimira los numeros de la lista que son las catidades para eso sirve la listado3 del listado3 no se quitan las categorias que se van terminando
        print("\n".join(Lista[indice2]))#se imprime las cantidades en la posicion que se eligio el usuario'

#se verifica en este while que el usuario halla escrito una cantidad que este en esa posicion
    while afirmacion2 == False:
        Elecion = str(input("Escribe la cantidad "))#pregunta
        Elecion = str(input("Estas seguro "))#te vuelve a pregiuntar
        if Elecion in Lista[indice2]: #se compara lo que eligio el usuario con la lista de cantidades en el indice que anterior habiamos comentado
            afirmacion2 = True#cuando se cumple con la condicio sigue con el codigo
    Lista[indice2].remove(Elecion)#se remueve la cantidad que eligio el usuario
    lista23.append(usuario)#se agrega la categoria para el contador de 5 para cuando la puedas quitar ,
            
      #este if es cuando la lista 23 una misma palabra este 5 vecese se remueva de la listado2 que es la lista que se imprime al principio del codigo.
    if lista23.count(usuario) == 5:
       listado2.remove(usuario)#se remueve la categoria
    if usuario or len(categorias):
        Elecion = int(Elecion) #se convierte el str del numero en int
        ram = random.randint(0,len(categorias[usuario])-1) #se hace un random con las preguntas del dicionario dependiendo su categoria se actualiza -1 es para que vuelva a leer la longitud de la lista de las preguntas
        print(categorias[usuario][ram])#se imprime la pregunta de la categoria dependiendo del random
        categorias[usuario].pop(ram)#se saca la pregunta de la lista de los dicionario para que no se repita
        respuesta = input("")#variable para que el usuario ingresa la respuesta
        respuesta = respuesta.lower()# se convierte en minusculas por que las respeustas estan en minusculas
        indice = categoriasS.index(usuario)# se saca el indice de la lista que no se modifica para que este en concordancia con las repuestas de la categorias.
    if respuestas[indice][ram] == respuesta or respuesta in lista55:#se compara la respuesta del usuario con la lista de respuestas
        print("\nCorrect\n")# se imprime correcto si son iguales
        respuestas[indice].pop(ram)#se saca la respuesta de la lista de respuestas para no tener problemas con otras preguntas
        Puntaje = Puntaje + Elecion# se suma el puntaje que es 0 con la elecion del jugador
        x+=1#se suma un turno
    else:
        print("\nIncorrect\n")#si se equivoca sale incorrect
        print(respuestas[indice][ram])#se imprime la respuesta de la pregunta
        Puntaje = Puntaje - Elecion#se quita puntos dependiendo de la elecion del usuario
        respuestas[indice].pop(ram)#se quita la respuesta de la lista de respuestas
        x+=1#se suma un turno
print("Fin de Juego Tu puntaje",Puntaje)#cuando pasan los 30 turnos se imprime fin del juego y tu puntaje. 


        


                                           



