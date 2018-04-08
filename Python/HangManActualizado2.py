import random
#Generador de palabra random.
gameW = ['ALEMANIA', 'MEXICO', 'INDIA', 'CUBA', 'EGIPTO', 'SUIZA', 'JAPON', 'CHINA', 'RUSIA', 'CHILE', 'FRANCIA', 'GHANA', 'HAITI', 'INDONESIA', 'ISRAEL', 'ITALIA', 'JAMAICA', 'YEMEN', 'UCRANIA', 'INGLATERRA']
w = random.randint(0,19)
chosenW = gameW[w]


#Divide la palabra en letras para seleccionar.
chosenW = list(chosenW)


#Crea el campo de juego.
campo = '_' * len(chosenW)
campo = list(campo)
print (campo)

#Agarrar el numero de letras en la palabra
largoP = len(chosenW)


#Da dos veces el numero de letras
numOp = 10
print("")
print("\n Numero de oportunidades ", numOp)
print("\n El numero de letras en la palabra ", largoP, "\n")
      
#Ocupamos un loop para los intentos
intento = True
contBuena = 0
index = 0
malIntento = 0
fallidas = 0 




while intento == True:
    #Mete el intento del jugador en dos arrays diferentes
    #Un array para intentos fallados y uno para acertados
    intentoJ = input("\n Adivina una letra ")
    intentoJ = intentoJ.upper()

    #El jugador no puede introducir mas de una letra
    if len(intentoJ) != 1:
        print("Porfavor introduzca una sola letra.")

    #Si el jugador no introduce una letra
    elif intentoJ not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print("Porfavor introduzca solo LETRAS")

    #Si el jugador se equivoca
    elif intentoJ not in chosenW:
        for index in range(0):
            if chosenW[index] != intentoJ:
                malIntento = intentoJ[index]
                                              
        print("Adivinaste mal")

        index = index + 1
        print("Esto es malo" ,index)

        fallidas = fallidas + 1
        print("Letras que fallaste" ,fallidas)

        numOp = numOp - 1
        print("Te quedan", numOp, "restantes.")

        if numOp == 0:
            intento = False
            print("*****************Perdiste!*****************")
            print("La palabra secreta era: ", chosenW)
        else:
            intento = True


    #Si el jugador adivina
    elif intentoJ in chosenW:
        for i in range(largoP):
            if chosenW[i] == intentoJ:
                 campo[i] = intentoJ
        print("\n Letras que le has atinado ", campo, end = "")
        print("Correcto")
        contBuena = contBuena + 1

        if contBuena >= largoP:
            intento = False
            print ("*****************Ganaste!*****************")
        else:
            intento = True
