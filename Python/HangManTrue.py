import random
#Abecedario
abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#Generador de palabra random.
gameW = ['ESTONIA', 'MEXICO', 'IRAK', 'CUBA', 'EGIPTO', 'SUIZA', 'JAPON', 'CHINA', 'RUSIA', 'CHILE', 'KUWAIT', 'NEPAL', 'PORTUGAL', 'VIETNAM', 'ISRAEL', 'CHAD', 'ECUADOR', 'GRECIA', 'IRAN', 'BRASIL']
w = random.randint(0,19)
chosenW = gameW[w]
#print (chosenW)

#Divide la palabra en letras para seleccionar.
chosenW = list(chosenW)
#print (chosenW)

#Crea el campo de juego.
campo = '_' * len(chosenW)
campo = list(campo)
print (campo)

#Agarrar el numero de letras en la palabra
largoP = len(chosenW)
print (largoP)

#Da el numero de oportunidades
numOp = 10
print("")
print(" Numero de oportunidades ", numOp)
print(" El numero de letras en la palabra ", largoP, "\n")
      
#Ocupamos un ciclo para los intentos
intento = True
contBuena = 0
index = 0

while intento == True:
    #Mete el intento del jugador en dos listas diferentes
    #Una lista para intentos fallados y una para acertados
    intentoJ = input("\n Adivina una letra ")
    intentoJ = intentoJ.upper()

    #El jugador no puede introducir mas de una letra
    if len(intentoJ) != 1:
        print(" Porfavor introduzca una sola letra.")

    #Si el jugador no introduce una letra
    elif intentoJ not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(" Porfavor introduzca solo LETRAS")

    #Si el jugador se equivoca
    elif intentoJ not in chosenW:
        #Remover la letra del abecedario
        if intentoJ in abc:
            abc.remove(intentoJ)
            print (abc)
        for index in range(0):
            if chosenW[index] != intentoJ:
                malIntento[index] = intentoJ
                index = index + 1

    
        print(" Adivinaste mal")
        print(campo)

        numOp = numOp - 1
        print(" Te quedan", numOp, "intentos restantes.")

        if numOp == 0:
            intento = False
            print("Perdiste!")
        else:
            intento = True

    #Si el jugador adivina
    elif intentoJ in chosenW:
        #Remover la letra del abecedario
        if intentoJ in abc:
            abc.remove(intentoJ)
            print (abc)
        for index2 in range(largoP):
            if chosenW[index2] == intentoJ:
                 campo[index2] = intentoJ
                 
        print("\n Letras que has acertado ", campo, end = "")
        print("Correcto")
        contBuena = contBuena + 1

        if contBuena >= largoP:
            intento = False
            print (" Ganaste!")
        else:
            intento = True

    
        
