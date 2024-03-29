import time
import sys
import random
from time import sleep

def abrirpuerta():
    global I
    global VIDA
    global SAVE
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nPara abrir la puerta es necesario que adivines el número entre 1-2. Sólo tienes una oportunidad.\n")
    PUZ=random.randint(1,2)
    while True:
        SIG=str(input())
        if SIG == str(PUZ):
            exitopuerta()
            break
        elif SIG == "GUARDAR":
            SAVE = 1
            APSAVE = AP
            HPSAVE = VIDA
            time.sleep(1)
            guardar()
        elif SIG == "REGRESAR":
            if SAVE == 0:
                time.sleep(1)
                print("\nNo hay juego guardado.\n")
            else:
                time.sleep(1)
                regresar()
                break
        elif SIG == "VIDA":
            if VIDA == 1:
                time.sleep(1)
                print("\nTienes "+str(VIDA)+" vida.\n")
            else:
                time.sleep(1)
                print("\nTienes "+str(VIDA)+" vidas.\n")
        elif SIG == "AP":
            time.sleep(1)
            print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        elif SIG == "INVENTARIO":
            inventario()
        else:
            fracasopuerta()
            break

def armory():
    global I
    global SAVE
    global VIDA
    global AP
    global PATIO
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nEntran a la puerta gruesa de metal y se sorprenden con lo que ven dentro.")
    time.sleep(4)
    print("\nEs la armería del castillo.")
    time.sleep(3)
    print("\nCada miembro del grupo escoge algo para su arsenal y tus ojos recaen en dos objetos.")
    time.sleep(4)
    print("\nUn escudo enorme y una espada con un pomo dorado y con un rubí incrustado en el centro.")
    time.sleep(4)
    print("\nAl agregarlas a tu inventario, te sientes empoderado y listo para pelear.")
    time.sleep(3)
    print("\nTu Poder de Ataque (AP) y Vida (HP) suben por 1.")
    AP = AP + 1
    VIDA = VIDA + 1
    if I == 2:
        I = 10
    elif I == 3:
        I = 11
    elif I == 4:
        I = 12
    elif I == 5:
        I = 13
    elif I == 6:
        I = 14
    elif I == 7:
        I = 15
    elif I == 8:
        I = 16
    elif I == 9:
        I = 17
    time.sleep(3)
    print("\nGuardando sus nuevas armas, salen del cuarto.")
    if PATIO == 1:
        time.sleep(3)
        print("\nAhora puedes elegir entre la puerta negra o la puerta corrediza.")
        time.sleep(3)
        print("\nPUERTA NEGRA = N\nPUERTA CORREDIZA = C\n")
        while True:
            SIG=str(input())
            if SIG == "N":
                bossbattle()
                break
            elif SIG == "C":
                guardbattle()
                break
            elif SIG == "INVENTARIO":
                inventario()
            elif SIG == "GUARDAR":
                time.sleep(1)
                print("\nEstás en la misión final. No puedes guardar el juego.")
            elif SIG == "REGRESAR":
                if SAVE == 0:
                    time.sleep(1)
                    print("\nNo hay juego guardado.\n")
                else:
                    time.sleep(1)
                    regresar()
                    break
            elif SIG == "VIDA":
                if VIDA == 1:
                    time.sleep(1)
                    print("\nTienes "+str(VIDA)+" vida.\n")
                else:
                    time.sleep(1)
                    print("\nTienes "+str(VIDA)+" vidas.\n")    
            elif SIG == "AP":
                time.sleep(1)
                print("\nTienes "+str(AP)+" Poder de Ataque.\n")
            else:
                time.sleep(0.5)
                print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")
    elif PATIO == 1:
        time.sleep(3)
        print("\nYa hiciste todo lo que había por hacer en el patio.")
        time.sleep(3)
        print("\nSe reúnen y se preparan para la última puerta.")
        bossbattle()

def atacarguardia():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nPara atacar al guardia es necesario que adivines el número entre 1-4. Sólo tienes una oportunidad.\n")
    PUZ=random.randint(1,4)
    while True:
        SIG=str(input())
        if SIG == str(PUZ):
            time.sleep(1)
            exitoatacarguardia()
            break
        elif SIG == "GUARDAR":
            time.sleep(1)
            SAVE = 2
            APSAVE = AP
            HPSAVE = VIDA
            guardar()
        elif SIG == "REGRESAR":
            if SAVE == 0:
                time.sleep(1)
                print("\nNo hay juego guardado.\n")
            else:
                time.sleep(1)
                regresar()
                break
        elif SIG == "VIDA":
            if VIDA == 1:
                time.sleep(1)
                print("\nTienes "+str(VIDA)+" vida.\n")
            else:
                time.sleep(1)
                print("\nTienes "+str(VIDA)+" vidas.\n")
        elif SIG == "AP":
            time.sleep(1)
            print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        elif SIG == "INVENTARIO":
            inventario()
        else:
            time.sleep(1)
            fracasoatacarguardia()
            break

def base():
    global I
    global SAVE
    global VIDA
    global AP
    global BASE
    global APSAVE
    global HPSAVE
    BASE=0
    time.sleep(2.5)
    print("\nAl finalizar tu elección, te dan un recorrido de la base y encuentras muchas diferentes cosas que hacer.")
    time.sleep(6)
    print("\nFarion te explica que van a montar un contraataque el día siguiente.")
    time.sleep(4)
    print("\n¿Qué quieres hacer?")
    time.sleep(3)
    print("\nENTRENAR = E\nCOMER = C\nDORMIR = D (seguirá la historia)\n")
    while True:
        SIG=str(input())
        if SIG == "E":
            time.sleep(1)
            BASE = 1
            entrenar()
            break
        elif SIG == "C":
            time.sleep(1)
            BASE = 2
            comer()
            break
        elif SIG == "D":
            time.sleep(1)
            dormir()
            break
        elif SIG == "INVENTARIO":
            inventario()
        elif SIG == "GUARDAR":
            time.sleep(1)
            APSAVE = AP
            HPSAVE = VIDA
            SAVE = 3
            guardar()
        elif SIG == "REGRESAR":
            if SAVE == 0:
                time.sleep(1)
                print("\nNo hay juego guardado.\n")
            else:
                time.sleep(1)
                regresar()
                break
        elif SIG == "VIDA":
                if VIDA == 1:
                    time.sleep(1)
                    print("\nTienes "+str(VIDA)+" vida.\n")
                else:
                    time.sleep(1)
                    print("\nTienes "+str(VIDA)+" vidas.\n")    
        elif SIG == "AP":
                time.sleep(1)
                print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        else:
            time.sleep(1)
            print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")

def begin():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(4)
    print("\nUn ruido fuerte te despierta. Abres los ojos y te das cuenta que estás encerrado en una prisión. Un guardia esta parado a unos metros de ti, dándote la espalda.")
    time.sleep(5)
    print("\nEn la celda frente a ti está un prisionero con una cara que parece loco. Dentro de tu celda no hay más que una simple cama de paja y una ventana que se ve frágil.")
    time.sleep(5)
    print("\n¿Que quieres hacer?")
    time.sleep(2)
    print("\nHABLAR CON PRISIONERO = P\nHABLAR CON GUARDIA = G\nEMPUJAR VENTANA = V\n")
    global VECES
    VECES=0
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == "P":
            hablarprisionero()
            break
        elif SIG == "G":
            VECES+=1
            if VECES==3:
                guardiaenojado()
                break
            else:
                hablarguardia()
        elif SIG == "V":
            empujarventana()
            break
        elif SIG == "INVENTARIO":
            inventario()
        elif SIG == "GUARDAR":
            SAVE = 4
            APSAVE = AP
            HPSAVE = VIDA
            guardar()
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "AP":
            print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        elif SIG == "VIDA":
            if VIDA == 1:
                print("\nTienes "+str(VIDA)+" vida.\n")
            else:
                print("\nTienes "+str(VIDA)+" vidas.\n")
        else:
            print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")

def bossbattle():
    global I
    global SAVE
    global VIDA
    global AP
    global NOM
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nAbren la puerta negra y entran a la obscuridad.")
    time.sleep(3)
    print("\nTodo el grupo permanece junto, caminando hacia adelante.")
    time.sleep(3)
    print("\nDespués de unos metros de caminar, se encienden antorchas alrededor de la habitación.")
    time.sleep(4)
    print("\nEn el centro hay un enorme trono de piedra negra.")
    time.sleep(3)
    print("\nSe escucha una voz grave que viene de la obscuridad al final de la habitación.")
    time.sleep(3)
    words = "\n\"Bienvenidos a mi gran castillo. "+str(NOM)+", ¿cómo te trataron tus amiguitos nuevos?\n¿Igual o mejor que yo?\"\n"
    for char in words:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    MIO = "\n\"¡Cállate! ¡Te vas a arrepentir!\"\n"
    for char in MIO:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(2)
    print("\nCorres hacia la voz pero, antes de que llegues, sale tu enemigo.")
    time.sleep(3)
    print("\nLo que salió de la obscuridad no era humano.")
    time.sleep(2)
    print("\nEra la creatura más grande que habías visto en tu vida y tenía un sólo ojo.")
    time.sleep(2)
    SUYO = "\n\"¿Qué tan valiente eres ahora?\"\n"
    for char in SUYO:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    print("\nFarion grita:")
    time.sleep(1)
    EL = "\n\"¡A PELEAAAR!\"\n"
    for char in EL:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    MALO = 12
    time.sleep(1)
    print("\nSe acerca contigo el CÍCLOPE ("+str(MALO)+" HP). Adivina el número entre 1-2.\n")
    while True:
        if VIDA <= 0:
            time.sleep(3)
            print("\nCon el último golpe del cíclope, caes al piso y sueltas tu último respiro.\n")
            gameover()
            break
        ATT=random.randint(1,2)
        SIG=str(input())
        if SIG == str(ATT):
            MALO = MALO - AP
            time.sleep(2)
            print("\nLogras sorprender al cíclope y le quitas "+str(AP)+" vidas. Ahora tiene "+str(MALO)+" HP.") 
            if MALO <= 0:
                time.sleep(2)
                ciclopemuerto()
                break
            else:
                time.sleep(2)
                print("\nSe vuelve a acercar contra ti el cíclope. Adivina el número entre 1-2.\n")
        elif SIG == "REGRESAR":
            time.sleep(1)
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "GUARDAR":
            time.sleep(2)
            print("\nEstás en la misión final. No puedes guardar el juego.\n")
        elif SIG == "VIDA":
            time.sleep(2)
            if VIDA == 1:
                print("\nTienes "+str(VIDA)+" vida.\n")
            else:
                print("\nTienes "+str(VIDA)+" vidas.\n")
        elif SIG == "AP":
            time.sleep(1)
            print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        elif SIG == "INVENTARIO":
            inventario()
        else:
            time.sleep(1)
            print("\nLe fallas a tu enemigo y él aprovecha para atacarte a ti.")
            RAN=random.randint(1,2)
            ATA=random.randint(1,2)
            time.sleep(1)
            if RAN == ATA:
                print("\nEl cíclope te pega fuertemente y te quita una vida.\n")
                VIDA = VIDA-1
            else:
                print("\nEl cíclope te falla y regresa a su lugar.")
            time.sleep(2)
            print("\nSe vuelve a acercar contigo el CÍCLOPE ("+str(MALO)+" HP). Adivina el número entre 1-2.\n")

def caminando():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nDecides seguir tu camino. Comienzas a caminar en paralelo a la luz que viste hace poco.")
    time.sleep(4)
    print("\nPasa una hora.")
    time.sleep(2)
    print("\nPasan dos horas.")
    time.sleep(2)
    print("\nPasan tres horas.")
    time.sleep(2)
    print("\nTu estómago exige alimento.")
    time.sleep(3)
    print("\nPasan cuatro horas.")
    time.sleep(2)
    print("\nPasan cinco horas.")
    time.sleep(3)
    print("\nTu visión se empieza a cerrar.")
    time.sleep(3)
    print("\nNo tienes la suficiente energía como para seguir. Te acuestas en el piso y aceptas tu destino.")
    time.sleep(4)
    gameover()

def campamento():
    global I
    global SAVE
    global VIDA
    global AP
    global NOM
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nA lo lejos, puedes observar un bosque. Una columna de humo se eleva desde su interior.")
    time.sleep(4)
    print("\nEmpiezas a caminar hacia el bosque.")
    time.sleep(2)
    print("\nConforme te vas acercando, te das cuenta de que hay un campamento dentro del bosque.")
    time.sleep(4)
    print("\nLa gente te vio venir desde lejos y estaba preparada para tu llegada.")
    time.sleep(4)
    print("\nUno de ellos te preguntó:")
    time.sleep(2)
    words = "\n\"¿Quién eres y qué buscas?\"\n"
    for char in words:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(2)
    print("\nTu le respondes:")
    time.sleep(2)
    MIO = "\n\"Hola. Mi nombre es "+str(NOM)+". Me acabo de escapar de la prisión y ocupo ayuda.\"\n"
    for char in MIO:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(2)
    print("\nUno de ellos te explica que estaban apunto de ir a rescatarte porque quieren que los apoyes.\n")
    time.sleep(4)
    DIAL = "\"Somos los Guardianes del Bosque. Mi nombre es Farion. Venimos a rescatarte.\nLos Jefes del Vacío te secuestraron y están destruyendo nuestro hogar.\nVen con nosotros a nuestra base. Ahí puedes descansar y entrenar para cobrar tu venganza.\""
    for char in DIAL:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(2)
    print("\n\n¿Qué quieres hacer?")
    time.sleep(2)
    print("\nSEGUIRLOS = S\nDEJARLOS = D\n")
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == "S":
            seguirpersona()
            break
        elif SIG == "D":
            dejarpersona()
            break
        elif SIG == "INVENTARIO":
            inventario()
        elif SIG == "GUARDAR":
            SAVE = 5
            APSAVE = AP
            HPSAVE = VIDA
            guardar()
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "AP":
            print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        elif SIG == "VIDA":
                if VIDA == 1:
                    print("\nTienes "+str(VIDA)+" vida.\n")
                else:
                    print("\nTienes "+str(VIDA)+" vidas.\n")    
        else:
            print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")

def castigo():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\n\nEl guardia te agarra fuertemente y empieza a caminar contigo hacia el exterior de la prisión.")
    time.sleep(5)
    print("\nAntes de salir, pudiste observar la expresión de tristeza en la cara del otro prisionero.")
    time.sleep(5)
    print("\nEn cuanto el guardia abre la puerta, tus ojos se fijan en una columna central.")
    time.sleep(4)
    print("\nAlrededor de ella, se encuentran cinco guardias con caras de anticipación. El castigo se aproxima.")
    time.sleep(5)
    print("\nLlegan a la columna y el guardia principal comienza a amarrarte a ella.")
    time.sleep(4)
    print("\nMirando de reojo, ves a un par de figuras oscuras moviéndose en el bosque cercano.")
    time.sleep(4)
    print("\nApunto de empezar el castigo, escuchas que un guardia lanza un llanto al aire.\n")
    time.sleep(4)
    GRITO = "\"¡INTRUUSOOOOS!\""
    for char in GRITO:
        sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(2)
    print("\n\nTodos los guardias se detienen y voltean a ver al bosque.")
    time.sleep(4)
    print("\nDe repente, salen dos personas del bosque, con caras tapadas y espadas. Sus movimientos eran elegantes y controlados.")
    time.sleep(5)
    print("\nDespués de poco, lograron deshacerse de los guardias y se acercaron a ti. Te liberan y te dice uno de ellos:\n")
    time.sleep(5)
    DIAL = "\"Somos los Guardianes del Bosque. Mi nombre es Farion. Venimos a rescatarte. Los Jefes del Vacío te secuestraron y están destruyendo nuestro hogar.\nVen con nosotros a nuestra base. Ahí puedes descansar y entrenar para cobrar tu venganza.\""
    for char in DIAL:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(2)
    print("\n\n¿Qué quieres hacer?")
    time.sleep(2)
    print("\nSEGUIRLOS = S\nDEJARLOS = D\n")
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == "S":
            seguirpersona()
            break
        elif SIG == "D":
            dejarpersona()
            break
        elif SIG == "INVENTARIO":
            inventario()
        elif SIG == "GUARDAR":
            SAVE = 6
            APSAVE = AP
            HPSAVE = VIDA
            guardar()
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "AP":
            print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        elif SIG == "VIDA":
                if VIDA == 1:
                    print("\nTienes "+str(VIDA)+" vida.\n")
                else:
                    print("\nTienes "+str(VIDA)+" vidas.\n")    
        else:
            print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")

def cavartunel():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nDecides cavar el túnel con Torb.")
    time.sleep(3)
    print("\nSe acercan un poco a la pared para facilitar su trabajo.")
    time.sleep(4)
    print("\nTorb te pasa una herramienta especial para cavar y se preparan para hacer el túnel.")
    time.sleep(5)
    print("\nEmpiezan a cavar y, después de varias horas de trabajo, empiezan a escuchar voces encima de ustedes.")
    time.sleep(6)
    print("\nTorb te susurra:\n")
    time.sleep(2)
    DIAL = "\"Hay gente arriba. Es muy frágil el terreno aquí hay que tener cuidado con no cavar de más.\""
    for char in DIAL:
        sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(2)
    print("\n\nAdivina un número entre 1-3 para ver si pudiste cavar con éxito. Sólo tienes una oportunidad.")
    PUZ=random.randint(1,3)
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == str(PUZ):
            exitocavar()
            break
        elif SIG == "GUARDAR":
                print("\nEstás en la misión final. No puedes guardar el juego.")
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "VIDA":
            if VIDA == 1:
                print("\nTienes "+str(VIDA)+" vida.\n")
            else:
                print("\nTienes "+str(VIDA)+" vidas.\n")
        elif SIG == "AP":
            print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        elif SIG == "INVENTARIO":
            inventario()
        else:
            fracasocavar()
            break

def ciclopemuerto():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(2)
    print("\nCon el último golpe de tu arma, el cíclope cae, incado ante ti y te dice:")
    time.sleep(4)
    words = "\n\"No me arrepiento de nada. Eres basura para mí.\"\n"
    for char in words:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(2)
    print("\nNo le das la satisfacción de contestarle.")
    time.sleep(3)
    print("\nCon un movimiento rápido terminas la pelea.")
    time.sleep(3)
    print("\nEl resto del grupo se acerca contigo y juntos festejan la derrota del jefe de la obscuridad.")
    time.sleep(5)
    print("\nFueron victoriosos. ¡Felicidades!")
    time.sleep(3)
    gameover()

def comer():
    global I
    global SAVE
    global VIDA
    global AP
    global BASE
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nEntras al comedor de la base, hambriento por el hecho de no haber comido por varios días.")
    time.sleep(5)
    print("\nEn cuánto entras, una de las cocineras se aproxima hacia ti con un plato lleno de quesos.")
    time.sleep(5)
    SUYO = "\n\"Bienvenido al salón de festines. Nos encargaremos bien de ti.\""
    for char in SUYO:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(2)
    print("\n\nDespués de 7 platillos llenos de comida finalmente estás satisfecho.")
    time.sleep(5)
    print("\nLa calidad de la comida te hizo sentir más fuerte y hábil que antes.")
    time.sleep(4)
    print("\nTu vida se ha regenerado y ha aumentado por 2.")
    time.sleep(4)
    VIDA = 5
    print("\nAhora tienes "+str(VIDA)+" vidas.")
    time.sleep(3)
    print("\nCon el último platillo acabado, le agradeces a la cocinera y sales de la habitación.")
    time.sleep(5)
    print("\nVuelves a regresar a la base.")
    time.sleep(3)
    if BASE == 2:
        print("\nAhora puedes elegir dormir o ir a entrenar.")
        print("\nDORMIR = D\nENTRENAR = E\n")
        while True:
            SIG=str(input())
            time.sleep(1)
            if SIG == "E":
                entrenar()
                break
            elif SIG == "D":
                dormir()
                break
            elif SIG == "INVENTARIO":
                inventario()
            elif SIG == "GUARDAR":
                APSAVE = AP
                HPSAVE = VIDA
                SAVE = 7
                guardar()
            elif SIG == "REGRESAR":
                if SAVE == 0:
                    print("\nNo hay juego guardado.\n")
                else:
                    regresar()
                    break
            elif SIG == "VIDA":
                if VIDA == 1:
                    print("\nTienes "+str(VIDA)+" vida.\n")
                else:
                    print("\nTienes "+str(VIDA)+" vidas.\n")    
            elif SIG == "AP":
                print("\nTienes "+str(AP)+" Poder de Ataque.\n")
            else:
                print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")
    elif BASE == 1:
        print("\nYa hiciste todo lo que había por hacer en la base.")
        time.sleep(4)
        print("\nCaminando cansado, te vas a tu cama donde esperas el siguiente día.")
        time.sleep(5)
        dormir()

def dejarpersona():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    MIO = "\n\"Muchas gracias pero seguiré mi camino sólo.\"\n"
    for char in MIO:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(2)
    print("\nTe ayudan a levantarte y se despiden de ti. Tu te diriges hacia la pradera cercana para alejarte de la prisión.")
    time.sleep(6)
    print("\nDespués de medio día de caminar, la luna ya se encuentra en el cielo y se puede ver una luz a lo lejos.")
    time.sleep(5)
    print("\nPiensas que la luz puede ser un pueblo o un par de granjas. Tienes mucha hambre.")    
    time.sleep(5)
    print("\n¿Qué quieres hacer?")
    time.sleep(2)
    print("\nIR AL PUEBLO = P\nSEGUIR CAMINANDO = C\n")
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == "P":
            pueblo()
            break
        elif SIG == "C":
            caminando()
            break
        elif SIG == "INVENTARIO":
            inventario()
        elif SIG == "GUARDAR":
            SAVE = 8
            APSAVE = AP
            HPSAVE = VIDA
            guardar()
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "VIDA":
                if VIDA == 1:
                    print("\nTienes "+str(VIDA)+" vida.\n")
                else:
                    print("\nTienes "+str(VIDA)+" vidas.\n")    
        elif SIG == "AP":
                print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        else:
            print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")
    
def drenaje():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nEn cuanto abres la alcantarilla, te llega un olor a gases fecales.")
    time.sleep(5)
    print("\nCierras los ojos, te tapas la nariz y brincas hacia el olor.")
    time.sleep(4)
    print("\nCaes en una agua sucia e inmediatamente te arrepientes de tu decisión.")
    time.sleep(5)
    print("\nEmpiezas a caminar por el drenaje hasta que ves una luz a lo lejos.")
    time.sleep(5)
    print("\nAl acercarte a la luz, te das cuenta de que es el desagüe del drenaje.")
    time.sleep(5)
    print("\nSales por el desagüe y te encuentras en la parte trasera del edificio en el que estabas.")
    campamento()

def dormir():
    global I
    global SAVE
    global VIDA
    global AP
    time.sleep(1)
    print("\nLlegas a la habitación que te fue asignada.")
    time.sleep(3)
    print("\nEs un cuarto muy simple pero parece una mansión comparado con la celda en la que estabas.")
    time.sleep(5)
    print("\nTe preparas para dormir y te acuestas en tu cama.")
    time.sleep(4)
    print("\nCierras los ojos.")
    time.sleep(3)
    print("\nEstás dormido. En cuánto despiertes vas a empezar la última misión y ya no vas a poder guardar el juego.")
    time.sleep(6)
    print("\n¿Quiéres guardar el juego ahora?")
    time.sleep(3)
    print("\nSI = S\nNO = N\n")
    while True:
        SIG=str(input())
        time.sleep(2)
        if SIG == "N":
            iniciomision()
            break
        elif SIG == "INVENTARIO":
            inventario()
        elif SIG == "S":
            SAVE = 9
            APSAVE = AP
            HPSAVE = VIDA
            print("\nTu juego ha sido guardado con éxito. Teclea REGRESAR para volver a este punto.")
            iniciomision()
            break
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "VIDA":
                if VIDA == 1:
                    print("\nTienes "+str(VIDA)+" vida.\n")
                else:
                    print("\nTienes "+str(VIDA)+" vidas.\n")    
        elif SIG == "AP":
                print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        else:
            print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")

def empujarventana():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nTe acomodas de tal manera que tus pies están poniendo presión en la ventana.")
    time.sleep(5)
    print("\nPara empujar la ventana, adivina el número entre 1-2. Sólo tienes una oportunidad.\n")
    PUZ=random.randint(1,2)
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == str(PUZ):
            exitoventana()
            break
        elif SIG == "GUARDAR":
            SAVE = 10
            APSAVE = AP
            HPSAVE = VIDA
            guardar()
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "VIDA":
            if VIDA == 1:
                print("\nTienes "+str(VIDA)+" vida.\n")
            else:
                print("\nTienes "+str(VIDA)+" vidas.\n")
        elif SIG == "AP":
            print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        elif SIG == "INVENTARIO":
            inventario()
        else:
            fracasoventana()
            break
    
def entrenar():
    global I
    global SAVE
    global VIDA
    global AP
    global BASE
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nDecides ir a la zona de entrenamiento de la base.")
    time.sleep(3)
    print("\nEn cuanto entras, ves a los guardias y guerreros y uno de ellos se aproxima hacia ti.")
    time.sleep(5)
    SUYO = "\n\"Bienvenido a la zona de entrenamiento. Vamos a pelear para acostumbrarte.\"\n"
    for char in SUYO:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    MALO = 4
    time.sleep(2)
    print("\nTe acercas al entrenador y te preparas para pelear.")
    time.sleep(4)
    print("\nEn el combate, tu Poder de Ataque (AP) determina cuánto daño le haces al enemigo que tiene cierta vida (HP).")
    time.sleep(7)
    print("\nCuando ellos te pegan, solamente te quitarán una vida, al menos de que diga lo contrario.")
    time.sleep(6)
    print("\nPara determinar si le pegas, tienes que acertar un número entre un rango determinado.")
    time.sleep(6)
    print("\nSi le fallas al enemigo, puede ahora atacarte él. Sin embargo, existe una cierta probabilidad de que te falle.")
    time.sleep(8)
    print("\nVamos a intentarlo ahora.")
    time.sleep(3)
    print("\nSe acerca contigo el ENTRENADOR ("+str(MALO)+" HP). Adivina el número entre 1-2.\n")
    while True:
        ATT=random.randint(1,2)
        SIG=str(input())
        time.sleep(1)
        if SIG == str(ATT):
            MALO = MALO - AP
            print("\nLogras sorprender al entrenador y le quitas "+str(AP)+" vidas. Ahora tiene "+str(MALO)+" HP.") 
            time.sleep(1)
            if MALO <= 0:
                entrenadormuerto()
                break
            else:
                print("\nSe vuelve a acercar contra ti el entrenador. Adivina el número entre 1-2.\n")
        elif SIG == "GUARDAR":
            SAVE = 11
            APSAVE = AP
            HPSAVE = VIDA
            guardar()
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "VIDA":
            if VIDA == 1:
                print("\nTienes "+str(VIDA)+" vida.\n")
            else:
                print("\nTienes "+str(VIDA)+" vidas.\n")
        elif SIG == "AP":
            print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        elif SIG == "INVENTARIO":
            inventario()
        else:
            print("\nLe fallas a tu enemigo y él aprovecha para atacarte a ti.")
            time.sleep(3)
            RAN=random.randint(1,2)
            ATA=random.randint(1,2)
            if RAN == ATA:
                print("\nEl entrenador te pega fuertemente pero como están entrenando, no te hace daño.\n")
            else:
                print("\nEl entrenador te falla y regresa a su lugar.")
            time.sleep(2)
            print("\nSe vuelve a acercar contra ti el entrenador ("+str(MALO)+" HP). Adivina el número entre 1-2.\n")

def entrenadormuerto():
    global I
    global SAVE
    global VIDA
    global AP
    global BASE
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nCon el último golpe, el entrenador cae al piso y te felicita por tu habilidad de combate.")
    time.sleep(5)
    print("\nVuelves a regresar a la base.")
    time.sleep(2)
    if BASE == 1:
        print("\nAhora puedes elegir dormir o ir a comer.")
        time.sleep(3)
        print("\nDORMIR = D\nCOMER = C\n")
        while True:
            SIG=str(input())
            time.sleep(1)
            if SIG == "C":
                comer()
                break
            elif SIG == "D":
                dormir()
                break
            elif SIG == "INVENTARIO":
                inventario()
            elif SIG == "GUARDAR":
                SAVE = 12
                APSAVE = AP
                HPSAVE = VIDA
                guardar()
            elif SIG == "REGRESAR":
                if SAVE == 0:
                    print("\nNo hay juego guardado.\n")
                else:
                    regresar()
                    break
            elif SIG == "VIDA":
                if VIDA == 1:
                    print("\nTienes "+str(VIDA)+" vida.\n")
                else:
                    print("\nTienes "+str(VIDA)+" vidas.\n")    
            elif SIG == "AP":
                print("\nTienes "+str(AP)+" Poder de Ataque.\n")
            else:
                print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")
    elif BASE == 2:
        print("\nYa hiciste todo lo que había por hacer en la base.")
        time.sleep(4)
        print("\nCaminando cansado, te vas a tu cama donde esperas el siguiente día.")
        dormir()

def escalarpared():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nDecides escalar la pared con Farion.")
    time.sleep(3)
    print("\nDe manera sigilosa, caminan hacia la torre más cercana.")
    time.sleep(4)
    print("\nFarion te pasa un arpeo y se preparan para subir.")
    time.sleep(4)
    print("\nComienzan a escalar cuando escuchan que hay un guardia (4 HP) arriba de la torre.")
    time.sleep(5)
    print("\nFarion te hace señas como para que lo ataques de manera sigilosa.")
    time.sleep(5)
    print("\nAdivina un número entre 1-3. Sólo tienes una oportunidad.\n")
    PUZ=random.randint(1,3)
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == str(PUZ):
            exitoescalar()
            break
        elif SIG == "GUARDAR":
                print("\nEstás en la misión final. No puedes guardar el juego.\n")
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "VIDA":
            if VIDA == 1:
                print("\nTienes "+str(VIDA)+" vida.\n")
            else:
                print("\nTienes "+str(VIDA)+" vidas.\n")
        elif SIG == "AP":
            print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        elif SIG == "INVENTARIO":
            inventario()
        else:
            fracasoescalar()
            break
    
def escaparguardia():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nPara escapar silenciosamente es necesario que adivines el número entre 1-3. Sólo tienes una oportunidad.\n")
    PUZ=random.randint(1,3)
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == str(PUZ):
            exitoescapar()
            break
        elif SIG == "GUARDAR":
            SAVE = 13
            APSAVE = AP
            HPSAVE = VIDA
            guardar()
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "VIDA":
            if VIDA == 1:
                print("\nTienes "+str(VIDA)+" vida.\n")
            else:
                print("\nTienes "+str(VIDA)+" vidas.\n")
        elif SIG == "AP":
            print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        elif SIG == "INVENTARIO":
            inventario()
        else:
            fracasoescapar()
            break

def escogerarma():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nEntras a la base de los Guardianes y estás impresionado con todo lo que ves.")
    time.sleep(5)
    print("\nLa base estaba llena de todo tipo de armas y de suficientes provisiones para durar por años.")
    time.sleep(6)
    SUYO = "\n\"Es momento de que escogas tu arma. ¿Cuál quieres?\"\n"
    for char in SUYO:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)
    print("\nExaminas los diferentes tipos de armas que hay.")
    time.sleep(4)
    print("\n¿Cuál quieres escoger?")
    time.sleep(3)
    print("\nESPADA = E\nMAZO = M\nHACHA = H\nALABARDA = A\n")
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == "E":
            print("\nHas escogido una espada como tu arma.")
            AP+=1
            if I == 0:
                I = 2
            else:
                I = 6
            base()
            break
        elif SIG == "M":
            print("\nHas escogido un mazo como tu arma.")
            AP+=1
            if I == 0:
                I = 3
            else:
                I = 7
            base()
            break
        elif SIG == "H":
            print("\nHas escogido una hacha como tu arma.")
            AP+=1
            if I == 0:
                I = 4
            else:
                I = 8
            base()
            break
        elif SIG == "A":
            print("\nHas escogido una alabarda como tu arma.")
            AP+=1
            if I == 0:
                I = 5
            else:
                I = 9
            base()
            break
        elif SIG == "INVENTARIO":
            inventario()
        elif SIG == "GUARDAR":
            SAVE = 14
            APSAVE = AP
            HPSAVE = VIDA
            guardar()
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "VIDA":
                if VIDA == 1:
                    print("\nTienes "+str(VIDA)+" vida.\n")
                else:
                    print("\nTienes "+str(VIDA)+" vidas.\n")    
        elif SIG == "AP":
                print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        else:
            print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")

    
def exitoatacarguardia():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nÉXITO")
    time.sleep(1)
    print("\nTe mueves de manera sigilosa y, llegándole por atrás al guardia, lo tumbas con un golpe.")
    time.sleep(5)
    print("\nEl guardia cae al piso inconsciente.")
    time.sleep(3)
    print("\nEstas apunto de salir de la habitación cuando escuchas que el prisionero te habla:")
    time.sleep(4)
    words = "\nOye tu. Ya te deshiciste del guardia. ¿Por qué no me rescatas a mi también?\n"
    for char in words:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    print("\n¿Qué quieres hacer?")
    time.sleep(2)
    print("\nRESCATARLO = R\nIGNORARLO = I\n")
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == "R":
            rescatado()
            break
        elif SIG == "I":
            ignorado()
            break
        elif SIG == "INVENTARIO":
            inventario()
        elif SIG == "GUARDAR":
            SAVE = 15
            APSAVE = AP
            HPSAVE = VIDA
            guardar()
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "VIDA":
                if VIDA == 1:
                    print("\nTienes "+str(VIDA)+" vida.\n")
                else:
                    print("\nTienes "+str(VIDA)+" vidas.\n")    
        elif SIG == "AP":
                print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        else:
            print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")
    
def exitocavar():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nÉXITO")
    time.sleep(1)
    print("\nCon mucha habilidad, logras excavar de tal manera que no hacen ruido y no se destruye nada.")
    time.sleep(5)
    print("\nSalen al patio principal exactamente como lo habían planeado.")
    time.sleep(2)
    patio()
    
def exitoescalar():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nÉXITO")
    time.sleep(1)
    print("\nSubes rapidamente y, antes de que se de cuenta el guardia, le brincas y lo atacas.")
    time.sleep(5)
    print("\nCon un sólo golpe lo tumbas al piso, inconsciente.")
    time.sleep(3)
    print("\nFarion sube junto a ti y te felicita por tu habilidad.")
    time.sleep(4)
    print("\nEmpiezan a caminar por la pared y se detienen cuando llegan al patio principal.")
    time.sleep(5)
    print("\nHay varios guardias de patrullas pero se esperan hasta que no haya nadie y brincan al patio.")
    time.sleep(4)
    patio()
    
def exitoescapar():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nÉXITO")
    time.sleep(1)
    print("\nTe mueves de manera sigilosa y logras escaparte de la prisión.")
    time.sleep(4)
    print("\nEl guardia no tiene la menor idea de lo que estás haciendo.")
    time.sleep(4)
    print("\nSales de la habitación donde estaban las celdas y te das cuenta que hay un pasillo largo.")
    time.sleep(6)
    print("\nEn la mitad del pasillo, hay una alcantarilla que probablemente lleva a un drenaje.")
    time.sleep(5)
    print("\n¿Qué quieres hacer?")
    time.sleep(2)
    print("\nIR POR EL PASILLO = P\nIR POR LA ALCANTARILLA = A\n")
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == "A":
            drenaje()
            break
        elif SIG == "P":
            pasillo()
            break
        elif SIG == "INVENTARIO":
            inventario()
        elif SIG == "GUARDAR":
            SAVE = 16
            APSAVE = AP
            HPSAVE = VIDA
            guardar()
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "VIDA":
                if VIDA == 1:
                    print("\nTienes "+str(VIDA)+" vida.\n")
                else:
                    print("\nTienes "+str(VIDA)+" vidas.\n")    
        elif SIG == "AP":
                print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        else:
            print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")
    
def exitopuerta():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nÉXITO")
    time.sleep(1.5)
    print("\nTu ganzúa funciona perfectamente y pudiste abrir la puerta con éxito.")
    time.sleep(2)
    print("\nAl salir de la celda, volteas a ver al guardia. Como te está dando la espalda, no te puede ver.")
    time.sleep(2)
    print("\n¿Qué quieres hacer?")
    time.sleep(2)
    print("\nTRATAR DE ATACAR AL GUARDIA = A\nTRATAR DE ESCAPAR SILENCIOSAMENTE = E\n")
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == "A":
            atacarguardia()
            break
        elif SIG == "E":
            escaparguardia()
            break
        elif SIG == "INVENTARIO":
            inventario()
        elif SIG == "GUARDAR":
            SAVE = 17
            APSAVE = AP
            HPSAVE = VIDA
            guardar()
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "VIDA":
            if VIDA == 1:
                print("\nTienes "+str(VIDA)+" vida.\n")
            else:
                print("\nTienes "+str(VIDA)+" vidas.\n")
        elif SIG == "AP":
            print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        else:
            print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")
 
def exitoventana():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nÉXITO")
    time.sleep(1)
    print("\nEn cuanto empujas la ventana, te llega el aire fresco de la pradera.")
    time.sleep(4)
    print("\nCierras los ojos, y brincas desde tu ventana hacia el piso.")
    time.sleep(4)
    print("\nCaes fuertemente pero no te pasa nada y te paras de inmediato.")
    time.sleep(3)
    campamento()
 
def fracasoatacarguardia():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nFRACASO")
    time.sleep(1.5)
    print("\nAl intentar atacar al guardia, le metes un golpe que no le hace daño y se voltea hacia ti.")
    time.sleep(5)
    MIO = "\n\"¡Qué te pasa! ¿Crees que me podías atacar?\nEres un inútil.\n¡Te llevaré al castigo!\""
    for char in MIO:
        sleep(0.12)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(2)
    if I == 1:
        print("\n\nAl llevarte al castigo, el guardia se da cuenta que tienes una ganzúa y te la quita.")
        I=0
        time.sleep(2)
        print("\nTu inventario ha sido vaciado.")
        castigo()
    else:
        castigo()
 
def fracasocavar():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nFRACASO")
    time.sleep(1)
    print("\nIntentando salir, haces un agujero enorme y de desestabiliza el túnel.")
    time.sleep(4)
    print("\nEmpiezan a caer piedras del techo y una de ellas te pega en la cabeza.")
    time.sleep(4)
    print("\nTe quita una vida.")
    time.sleep(2)
    VIDA = VIDA - 1
    print("\nA pesar del accidente, te das cuenta de que están en el patio principal, justo como querían.")
    time.sleep(4)
    patio()
 
def fracasoescalar():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nFRACASO.")
    time.sleep(1)
    print("\nEn cuanto subes para atacar al guardia, él se voltea hacia ti.")
    time.sleep(4)
    SUYO = "\n\"¡Intruso! Vas a morir.\"\n"
    for char in SUYO:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    MALO = 4
    time.sleep(1)
    print("\nTe acercas al guardia (4 HP) y te preparas para pelar.")
    time.sleep(3)
    print("\nSe acerca contigo el GUARDIA ("+str(MALO)+" HP). Adivina el número entre 1-2.\n")
    while True:
        if VIDA <= 0:
            time.sleep(1)
            print("\nCon el último golpe de tu enemigo, caes al piso y sueltas tu último respiro.\n")
            time.sleep(4)
            gameover()
            break
        ATT=random.randint(1,2)
        SIG=str(input())
        time.sleep(1)
        if SIG == str(ATT):
            MALO = MALO - AP
            print("\nLogras sorprender al guardia y le quitas "+str(AP)+" vidas. Ahora tiene "+str(MALO)+" HP.") 
            if MALO <= 0:
                time.sleep(1)
                guardiamuerto()
                break
            else:
                time.sleep(1)
                print("\nSe vuelve a acercar contra ti el guardia. Adivina el número entre 1-2.\n")
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "GUARDAR":
            print("\nEstás en la misión final. No puedes guardar el juego.\n")
        elif SIG == "VIDA":
            if VIDA == 1:
                print("\nTienes "+str(VIDA)+" vida.\n")
            else:
                print("\nTienes "+str(VIDA)+" vidas.\n")
        elif SIG == "AP":
            print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        elif SIG == "INVENTARIO":
            inventario()
        else:
            print("\nLe fallas a tu enemigo y él aprovecha para atacarte a ti.")
            RAN=random.randint(1,2)
            ATA=random.randint(1,2)
            time.sleep(3)
            if RAN == ATA:
                print("\nEl guardia te pega fuertemente y te quita una vida.\n")
                VIDA = VIDA-1
            else:
                print("\nEl guardia te falla y regresa a su lugar.\n")
            time.sleep(2)
            print("Se vuelve a acercar contigo el GUARDIA ("+str(MALO)+" HP). Adivina el número entre 1-2.\n")
 
def fracasoescapar():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nFRACASO")
    time.sleep(1.5)
    print("\nAl intentar escapar, haces mucho ruido y el guardia voltea y se acerca hacia ti rapidamente.")
    time.sleep(3)
    MIO = "\n\"¡Qué te pasa! ¿Crees que te podías escapar de mi?\n¡Te llevaré al castigo!\""
    for char in MIO:
        sleep(0.12)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    if I == 1:
        print("\n\nAl llevarte al castigo, el guardia se da cuenta que tienes una ganzúa y te la quita.")
        I=0
        time.sleep(2)
        print("\nTu inventario ha sido vaciado.")
        castigo()
    else:
        castigo()

def fracasopasillo():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nFRACASO")
    time.sleep(1)
    print("\nEl guardia alcanza a correr hacia ti con velocidad y te toma del cuello.")
    time.sleep(4)
    words = "\n¡No te ibas a esconder de mi rata inmunda!\nTe llevaré al castigo."
    for char in words:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    if I == 1:
        print("\n\nAl llevarte al castigo, el guardia se da cuenta que tienes una ganzúa y te la quita.")
        I=0
        time.sleep(4)
        print("\nTu inventario ha sido vaciado.")
        castigo()
    else:
        castigo()
 
def fracasopuerta():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nFRACASO")
    time.sleep(1.5)
    print("\nTu ganzúa se ha roto.")
    I=0
    time.sleep(3)
    print("\nAl utilizar la ganzúa de manera incorrecta, el guardia se acerca hacia ti rapidamente y abre la puerta.")
    time.sleep(3)
    MIO = "\n\"¡Te vas a arrepentir mocoso insolente!\n¡Te llevaré al castigo!\""
    for char in MIO:
        sleep(0.12)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    castigo()

def fracasoventana():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nFRACASO")
    time.sleep(1)
    print("\nAl intentar abrir la ventana, tus pies le pegan pero ésta no se mueve.")
    time.sleep(3)
    print("\nEl guardia escucha tus movimientos y abre la puerta de tu celda.")
    time.sleep(3)
    words = "\n¡No te escaparás insecto!\nTe llevaré al castigo."
    for char in words:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    if I == 1:
        print("\n\nAl llevarte al castigo, el guardia se da cuenta que tienes una ganzúa y te la quita.")
        I=0
        time.sleep(2)
        print("\nTu inventario ha sido vaciado.")
        castigo()
    else:
        castigo()
    
def gameover():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(2)
    print("\nSE HA ACABADO EL JUEGO")
    time.sleep(3)
    print("\n¿Qué quieres hacer?")
    time.sleep(2)
    print("\nREGRESAR A TU JUEGO GUARDADO = REGRESAR\nVOLVER A EMPEZAR = V\nACABAR = A\n")
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == "A":
            exit()
        elif SIG == "V":
            start()
            break
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
        else:
            print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")

def guardar():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(2)
    print("\nTu juego ha sido guardado con éxito. Para regresar a este punto teclea REGRESAR.\n")

def guardia1dead():
    global I
    global SAVE
    global VIDA
    global AP
    global PATIO
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nDerrotando al primer guardia, el guardia jefe se prepara para ir contra ti.")
    time.sleep(4)
    MALO=6
    print("\nSe acerca contigo el GUARDIA JEFE ("+str(MALO)+" HP). Adivina el número entre 1-2.\n")
    while True:
        if VIDA <= 0:
            print("\nCon el último golpe de tu enemigo, caes al piso y sueltas tu último respiro.\n")
            time.sleep(3)
            gameover()
            break
        ATT=random.randint(1,2)
        SIG=str(input())
        time.sleep(1)
        if SIG == str(ATT):
            MALO = MALO - AP
            print("\nLogras sorprender al guardia jefe y le quitas "+str(AP)+" vidas. Ahora tiene "+str(MALO)+" HP.") 
            if MALO <= 0:
                guardbattlevictory()
                break
            else:
                time.sleep(4)
                print("\nSe vuelve a acercar contra ti el guardia jefe. Adivina el número entre 1-2.\n")
        elif SIG == "GUARDAR":
            print("\nEstás en la misión final. No puedes guardar el juego.\n")
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "VIDA":
            if VIDA == 1:
                print("\nTienes "+str(VIDA)+" vida.\n")
            else:
                print("\nTienes "+str(VIDA)+" vidas.\n")
        elif SIG == "AP":
            print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        elif SIG == "INVENTARIO":
            inventario()
        else:
            print("\nLe fallas a tu enemigo y él aprovecha para atacarte a ti.")
            RAN=random.randint(1,2)
            ATA=random.randint(1,2)
            time.sleep(3)
            if RAN == ATA:
                print("\nEl guardia jefe te pega fuertemente y te quita una vida.\n")
                VIDA = VIDA-1
            else:
                print("\nEl guardia jefe te falla y regresa a su lugar.")
            time.sleep(2)
            print("\nSe vuelve a acercar contigo el GUARDIA JEFE ("+str(MALO)+" HP). Adivina el número entre 1-2.\n")

def guardbattle():
    global I
    global SAVE
    global VIDA
    global AP
    global PATIO
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nJuntos abren la puerta corrediza y de inmediato se arrepienten.")
    time.sleep(4)
    print("\nAcaban de entrar a la habitación de los guardias.")
    time.sleep(3)
    print("\nPor suerte nada más había tres guardias. Uno de ellos tiene mejor armadura.")
    time.sleep(5)
    print("\nFarion corre hacia uno de los normales y lo derrota antes de que pueda reaccionar.")
    time.sleep(5)
    print("\nLos demás guardias se alborotan y agarran sus armas.")
    time.sleep(3)
    print("\nUstedes se preparan para pelear.")
    time.sleep(3)
    MALO1=4
    print("\nSe acerca contigo el GUARDIA 1 ("+str(MALO1)+" HP). Adivina el número entre 1-2.\n")
    while True:
        if VIDA <= 0:
            print("\nCon el último golpe de tu enemigo, caes al piso y sueltas tu último respiro.\n")
            time.sleep(4)
            gameover()
            break
        ATT=random.randint(1,2)
        print(str(ATT))
        SIG=str(input())
        time.sleep(1)
        if SIG == str(ATT):
            MALO1 = MALO1 - AP
            print("\nLogras sorprender al guardia y le quitas "+str(AP)+" vidas. Ahora tiene "+str(MALO1)+" HP.") 
            if MALO1 <= 0:
                guardia1dead()
                break
            else:
                time.sleep(1)
                print("\nSe vuelve a acercar contra ti el guardia. Adivina el número entre 1-2.\n")
        elif SIG == "GUARDAR":
            print("\nEstás en la misión final. No puedes guardar el juego.\n")
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "VIDA":
            if VIDA == 1:
                print("\nTienes "+str(VIDA)+" vida.\n")
            else:
                print("\nTienes "+str(VIDA)+" vidas.\n")
        elif SIG == "AP":
            print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        elif SIG == "INVENTARIO":
            inventario()
        else:
            print("\nLe fallas a tu enemigo y él aprovecha para atacarte a ti.")
            RAN=random.randint(1,2)
            ATA=random.randint(1,2)
            time.sleep(2)
            if RAN == ATA:
                print("\nEl guardia te pega fuertemente y te quita una vida.\n")
                VIDA = VIDA-1
            else:
                print("\nEl guardia te falla y regresa a su lugar.")
            time.sleep(2)
            print("\nSe vuelve a acercar contigo el GUARDIA 1 ("+str(MALO1)+" HP). Adivina el número entre 1-2.\n")
    
def guardbattlevictory():
    global I
    global SAVE
    global VIDA
    global AP
    global PATIO
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nDerrotando al último enemigo, todo el grupo se sienta a descansar.")
    time.sleep(4)
    print("\nFue una pelea dificil pero la más dificil aún está por venir.")
    time.sleep(3)
    print("\nGuardando sus armas, salen del cuarto.")
    time.sleep(3)
    if PATIO == 2:
        print("\nAhora puedes elegir entre la puerta negra o la puerta de metal.")
        time.sleep(3)
        print("\nPUERTA NEGRA = N\nPUERTA DE METAL = M\n")
        while True:
            SIG=str(input())
            time.sleep(1)
            if SIG == "N":
                bossbattle()
                break
            elif SIG == "M":
                armory()
                break
            elif SIG == "INVENTARIO":
                inventario()
            elif SIG == "GUARDAR":
                print("\nEstás en la misión final. No puedes guardar el juego.")
            elif SIG == "REGRESAR":
                if SAVE == 0:
                    print("\nNo hay juego guardado.\n")
                else:
                    regresar()
                    break
            elif SIG == "VIDA":
                if VIDA == 1:
                    print("\nTienes "+str(VIDA)+" vida.\n")
                else:
                    print("\nTienes "+str(VIDA)+" vidas.\n")    
            elif SIG == "AP":
                print("\nTienes "+str(AP)+" Poder de Ataque.\n")
            else:
                print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")
    elif PATIO == 1:
        print("\nYa hiciste todo lo que había por hacer en el patio.")
        time.sleep(3)
        print("\nSe reúnen y se preparan para la última puerta.")
        time.sleep(1)
        bossbattle()

def guardiaenojado():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nEl guardia voltea rápidamente hacia ti.")
    time.sleep(0.5)
    MIO = "\n\"¡¿QUÉ SE TE OFRECE?! Ya estoy harto de ti.\n¡Te llevaré al castigo!\""
    for char in MIO:
        sleep(0.12)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(2)
    if I == 1:
        print("\n\nAl llevarte al castigo, el guardia se da cuenta que tienes una ganzúa y te la quita.")
        I=0
        time.sleep(2)
        print("\nTu inventario ha sido vaciado.")
        time.sleep(1)
        castigo()
    else:
        castigo()
    
def guardiamuerto():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nCon tu último golpe, el guardia cae al piso, derrotado.")
    time.sleep(3)
    print("\nFarion sube junto a ti y te felicita por tu habilidad.")
    time.sleep(3)
    print("\nEsperas que nadie haya escuchado su pelea.")
    time.sleep(3)
    print("\nEmpiezan a caminar por la pared y se detienen cuando llegan al patio principal.")
    time.sleep(5)
    print("\nHay varios guardias de patrullas pero se esperan hasta que no haya nadie y brincan al patio.")
    time.sleep(4)
    patio()
    
def hablarguardia():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nLe hablas y gritas al guardia. Ignorándote por completo, el guardia permanece quieto. TECLEA OTRO COMANDO.\n")    
    
def hablarprisionero():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nLe dices al prisionero:")
    time.sleep(2)
    MIO = "\n\"Hola. ¿Qué está pasando?\""
    for char in MIO:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    print("\n\nEl te responde con mucho ánimo:")
    time.sleep(2)
    SUYO = "\n\"Buenos días bella durmiente. Lo único que debes saber es que nos encerraron injustamente y tenemos que salir.\nYo no soy muy hábil pero ten esta ganzúa para que intentes abrir la puerta.\"\n"
    for char in SUYO:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(2)
    print("\nGanzúa agregada a tu inventario.\n")
    I=1
    time.sleep(2)
    print("¿Qué quieres hacer?\n")
    time.sleep(2)
    print("INTENTAR DE ABRIR PUERTA = A\nHABLAR CON GUARDIA = G\nEMPUJAR VENTANA = V\n")
    global VECES
    VECES = int()
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == "A":
            abrirpuerta()
            break
        elif SIG == "G":
            VECES+=1
            if VECES==3:
                guardiaenojado()
                break
            else:
                hablarguardia()
        elif SIG == "V":
            empujarventana()
            break
        elif SIG == "INVENTARIO":
            inventario()
        elif SIG == "GUARDAR":
            SAVE = 18
            APSAVE = AP
            HPSAVE = VIDA
            guardar()
        elif SIG == "AP":
            print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        elif SIG == "VIDA":
            if VIDA == 1:
                print("\nTienes "+str(VIDA)+" vida.\n")
            else:
                print("\nTienes "+str(VIDA)+" vidas.\n")
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        else:
            print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")
    
def ignorado():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nIgnoras los llantos del prisionero y sigues tu camino.")
    time.sleep(3)
    print("\nSales de la habitación donde estaban las celdas y te das cuenta que hay un pasillo largo.")
    time.sleep(5)
    print("\nEn la mitad del pasillo, hay una alcantarilla que probablemente lleva a un drenaje.")
    time.sleep(5)
    print("\n¿Qué quieres hacer?")
    time.sleep(2)
    print("\nIR POR EL PASILLO = P\nIR POR LA ALCANTARILLA = A\n")
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == "A":
            drenaje()
            break
        elif SIG == "P":
            pasillo()
            break
        elif SIG == "INVENTARIO":
            inventario()
        elif SIG == "GUARDAR":
            SAVE = 19
            APSAVE = AP
            HPSAVE = VIDA
            guardar()
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "VIDA":
                if VIDA == 1:
                    print("\nTienes "+str(VIDA)+" vida.\n")
                else:
                    print("\nTienes "+str(VIDA)+" vidas.\n")    
        elif SIG == "AP":
                print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        else:
            print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")
    
def iniciomision():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nEstás en un sueño profundo cuando sientes un movimiento brusco que te despierta.")
    time.sleep(4)
    print("\nEs Farion y te dice que te prepares porque están a punto de irse.")
    time.sleep(3)
    print("\nAgarras tus cosas y junto con el resto del grupo, salen rumbo al castillo del enemigo.")
    time.sleep(4)
    print("\nDespués de salir de la base y caminar por un buen rato, finalmente llegan a su destino.")
    time.sleep(4)
    print("\nNunca habías visto el castillo completo desde afuera.")
    time.sleep(3)
    print("\nEs un castillo enorme hecho a base de piedra negra con 5 torres en pentagono en su pared principal.")
    time.sleep(5)
    print("\nFarion se acerca y te propone el plan de escalar por afuera de una de las torres para entrar.")
    time.sleep(5)
    print("\nOtro del grupo, Torb, un enano, propuso crear un túnel que nos lleve directo al centro de su base.")
    time.sleep(5)
    print("\n¿Qué quieres hacer?")
    time.sleep(2)
    print("\nESCALAR LA PARED = P\nCAVAR UN TÚNEL = T\n")
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == "P":
            escalarpared()
            break
        elif SIG == "T":
            cavartunel()
            break
        elif SIG == "INVENTARIO":
            inventario()
        elif SIG == "GUARDAR":
                print("\nEstás en la misión final. No puedes guardar el juego.")
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "VIDA":
                if VIDA == 1:
                    print("\nTienes "+str(VIDA)+" vida.\n")
                else:
                    print("\nTienes "+str(VIDA)+" vidas.\n")    
        elif SIG == "AP":
                print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        else:
            print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")
    
def instrucciones():
    print("\nGuardianes del Bosque es un juego de texto desarrollado por los alumnos de la clase de Pensamiento Computacional.")
    time.sleep(3)
    print("\nEl usuario va a iniciar el juego en un universo previamente creado y va a poder interactuar con él.\n")
    time.sleep(4)
    print("Cuando el juego le permita hacer una elección, le van a salir opciones con las cuales puede actuar.\n")
    time.sleep(3)
    print("Ej. Si el juego dice:")
    time.sleep(2)
    print("\n\"¿Quieres bailar?\"\n\nSI = S\nNO = N\n")
    time.sleep(2)
    print("Tu puedes teclear S o N según lo que quieras hacer.")
    time.sleep(3)    
    print("\nAlgo importante a tomar en cuenta es que siempre tienes que teclear el comando exactamente igual para que funcione.\n")
    time.sleep(4)
    print("Te recomendamos prender el CAPS LOCK ya que todos los comandos son en mayúsculas.\n")
    time.sleep(3)
    print("Existen también algunos comandos predefinidos que puedes usar siempre. Esta es la lista:\n")
    time.sleep(4)   
    print("\nINVENTARIO = Checar los objetos que tienes en tu inventario.\nGUARDAR = Guardas tu progreso para regresar\nVIDA = Checar el número de vidas que te quedan.\nREGRESAR = Regresas al punto en el juego de la última vez que guardaste.\n")
    time.sleep(3)
    print("Ahora que ya conoces las instrucciones, ¿estás listo para comenzar el juego?\n")
    time.sleep(3)
    print("SI = S\nNO = N\n")
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == "S":
            nombre()
            break
        elif SIG == "N":
            print("\nCuando estés listo teclea la letra S.\n")
        else:
            print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")

def inventario():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(2)
    if I == 0:
        print("\nTu inventario está vacío.\n")
    elif I == 1:
        print("\nSolamente tienes una ganzúa en tu inventario.\n")
    elif I == 2:
        print("\nSolamente tienes tu espada en tu inventario.\n")
    elif I == 3:
        print("\nSolamente tienes tu mazo en tu inventario.\n")
    elif I == 4:
        print("\nSolamente tienes tu hacha en tu inventario.\n")
    elif I == 5:
        print("\nSolamente tienes tu alabarda en tu inventario.\n")
    elif I == 6:
        print("\nTienes una ganzúa y tu espada en tu inventario.\n")
    elif I == 7:
        print("\nTienes una ganzúa y tu mazo en tu inventario.\n")
    elif I == 8:
        print("\nTienes una ganzúa y tu hacha en tu inventario.\n")
    elif I == 9:
        print("\nTienes una ganzúa y tu alabarda en tu inventario.\n")
    elif I == 10:
        print("\nTienes tu espada, tu escudo y la espada dorada en tu inventario.\n")
    elif I == 11:
        print("\nTienes tu mazo, tu escudo y la espada dorada en tu inventario.\n")
    elif I == 12:
        print("\nTienes tu hacha, tu escudo y la espada dorada en tu inventario.\n")
    elif I == 13:
        print("\nTienes tu alabarda, tu escudo y la espada dorada en tu inventario.\n")
    elif I == 14:
        print("\nTienes una ganzúa, tu espada, tu escudo y la espada dorada en tu inventario.\n")
    elif I == 15:
        print("\nTienes una ganzúa, tu mazo, tu escudo y la espada dorada en tu inventario.\n")
    elif I == 16:
        print("\nTienes una ganzúa, tu hacha, tu escudo y la espada dorada en tu inventario.\n")
    elif I == 17:
        print("\nTienes una ganzúa, tu alabarda, tu escudo y la espada dorada en tu inventario.\n")

def nombre():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nPrimero que nada, vamos a empezar con la creación de tu personaje. ¿Qué nombre eliges?\n")
    global NOM
    NOM=str(input())
    time.sleep(1)
    print("\nEscogiste el nombre: " + NOM + ". ¿Está bien o lo quieres cambiar?\n\nCAMBIAR = C\nDEJAR = D\n")
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == "C":
            nombre()
            break
        elif SIG == "D":
            time.sleep(0.5)
            print("\nHola "+ NOM + ". Vamos a comenzar el juego.")
            begin()
            break
        else:
            print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")

def pasillo():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nDecides en seguir por el pasillo.")
    time.sleep(2)
    print("\nEn cuanto llegas al fondo del pasillo, se escucha una voz alarmada.")
    time.sleep(4)
    print("\nUn guardia estaba vigilando el pasillo y te vio.")
    time.sleep(3)
    print("\nEmpieza a correr hacia ti.")
    time.sleep(2)
    print("\nTu única opción es regresar hacia la alcantarilla que estaba antes.")
    time.sleep(4)
    print("\nPara llegar a la alcantarilla es necesario que adivines el número entre 1-3. Sólo tienes una oportunidad.\n")
    PUZ=random.randint(1,3)
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == str(PUZ):
            print("\nÉXITO")
            drenaje()
            break
        elif SIG == "GUARDAR":
            SAVE = 20
            APSAVE = AP
            HPSAVE = VIDA
            guardar()
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "VIDA":
            if VIDA == 1:
                print("\nTienes "+str(VIDA)+" vida.\n")
            else:
                print("\nTienes "+str(VIDA)+" vidas.\n")
        elif SIG == "AP":
            print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        elif SIG == "INVENTARIO":
            inventario()
        else:
            fracasopasillo()
            break

def patio():
    global I
    global SAVE
    global VIDA
    global AP
    global PATIO
    global APSAVE
    global HPSAVE
    PATIO = 0
    time.sleep(1)
    print("\nEl patio principal es un cuadrado grande ubicado en el centro del castillo.")
    time.sleep(5)
    print("\nDe aquí se pueden visitar las diferentes habitaciones.")
    time.sleep(4)
    print("\nLa mayoría de las puertas se ven normales pero pueden ver tres que destacan.")
    time.sleep(5)
    print("\nUna de ellas, y la más grande de todas, está pintada de negro y tiene picos rojos como marco.")
    time.sleep(6)
    print("\nLa segunda de ellas es una puerta de metal gruesa que se ve muy pesada.")
    time.sleep(5)
    print("\nLa última de ellas es una puerta corrediza hecha de una madera muy ligera.")
    time.sleep(5)
    print("\n¿A qué puerta quieres ir?")
    time.sleep(3)
    print("\nPUERTA NEGRA = N\nPUERTA DE METAL = M\nPUERTA CORREDIZA = C\n")
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == "N":
            bossbattle()
            break
        elif SIG == "M":
            PATIO = 1
            armory()
            break
        elif SIG == "C":
            PATIO = 2
            guardbattle()
            break
        elif SIG == "INVENTARIO":
            inventario()
        elif SIG == "GUARDAR":
                print("\nEstás en la misión final. No puedes guardar el juego.")
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "VIDA":
                if VIDA == 1:
                    print("\nTienes "+str(VIDA)+" vida.\n")
                else:
                    print("\nTienes "+str(VIDA)+" vidas.\n")    
        elif SIG == "AP":
                print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        else:
            print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")

def pueblo():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nTe acercas a la luz de poco en poco.")
    time.sleep(2)
    print("\nDespués de avanzar por unos minutos, comienzas a discernir unas figuras moviéndose.")
    time.sleep(4)
    print("\nUna de las figuras te apunta y comienza a correr hacia una carpa.")
    time.sleep(3)
    print("\nTe das cuenta que en realidad la luz no era un pueblo sino una guarida de bandidos.")
    time.sleep(4)
    print("\nComienzas a huir de ellos pero escuchas que el piso empieza a temblar. ¡Están montados en caballos!")
    time.sleep(5)
    print("\nDespués de poco, decides que correr no va a servir y te preparas para pelear.")
    time.sleep(2)
    sobrevivir()

def regresar():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    VIDA = HPSAVE
    AP = APSAVE
    print("\nEl juego se regresará a tu último punto donde guardaste el juego.")
    time.sleep(2)
    if SAVE == 1:
        abrirpuerta()
    elif SAVE == 2:
        atacarguardia()
    elif SAVE == 3:
        base()
    elif SAVE == 4:
        begin()
    elif SAVE == 5:
        campamento()
    elif SAVE == 6:
        castigo()
    elif SAVE == 7:
        comer()
    elif SAVE == 8:
        dejarpersona()
    elif SAVE == 9:
        dormir()
    elif SAVE == 10:
        empujarventana()
    elif SAVE == 11:
        entrenar()
    elif SAVE == 12:
        entrenadormuerto()
    elif SAVE == 13:
        escaparguardia()
    elif SAVE == 14:
        escogerarma()
    elif SAVE == 15:
        exitoatacarguardia()
    elif SAVE == 16:
        exitoescapar()
    elif SAVE == 17:
        exitopuerta()
    elif SAVE == 18:
        hablarprisionero()
    elif SAVE == 19:
        ignorado()
    elif SAVE == 20:
        pasillo()
    elif SAVE == 21:
        rescatado()

def rescatado():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    print("\nLe quitas las llaves al guardia y te acercas a la celda del prisionero.")
    time.sleep(4)
    print("\nAbres su puerta y en cuanto lo dejas salir el corre hacia ti.")
    time.sleep(3)
    print("\nTe preparas para pelear pero en realidad se acerca el prisionero y te da un abrazo.")
    time.sleep(4)
    words = "\n¡Wow! Muchísimas gracias. Te debo toda mi vida.\nTen este regalo como símbolo de mi gratitud.\n"
    for char in words:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    print("\nEl prisionero te da una pócima extraña. Te la tomas y te sientes como si pudieras cargar un caballo entero.")
    time.sleep(5)
    print("\nEs una pócima de ataque. Tu poder de ataque (AP) sube por 1.")
    AP+=1
    time.sleep(3)
    print("\nDespués de darte la pócima, el prisionero sale de la prisión.")
    time.sleep(3)
    print("\nSales de la habitación y te encuentras en un pasillo largo.")
    time.sleep(3)
    print("\nHay una alcantarilla a la mitad del pasillo.")
    time.sleep(3)
    print("\n¿Qué quieres hacer?")
    time.sleep(2)
    print("\nIR POR EL PASILLO = P\nIR POR LA ALCANTARILLA = A\n")
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == "A":
            drenaje()
            break
        elif SIG == "P":
            pasillo()
            break
        elif SIG == "INVENTARIO":
            inventario()
        elif SIG == "GUARDAR":
            SAVE = 21
            APSAVE = AP
            HPSAVE = VIDA
            guardar()
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "VIDA":
                if VIDA == 1:
                    print("\nTienes "+str(VIDA)+" vida.\n")
                else:
                    print("\nTienes "+str(VIDA)+" vidas.\n")    
        elif SIG == "AP":
                print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        else:
            print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")

def seguirpersona():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    time.sleep(1)
    MIO = "\n\"Muchas gracias. Los seguiré a su base.\"\n"
    for char in MIO:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    print("\nJuntos entran al bosque.")
    time.sleep(2)
    print("\nDespués de media hora de caminar, llegan a una parte del bosque donde sale una gran piedra del piso.")
    time.sleep(5)
    print("\nAcercándose a la piedra, uno de los guerreros saca un amuleto de su bolsillo y lo pega a la piedra.")
    time.sleep(4)
    print("\nEmpieza a temblar la tierra y se abre una puerta escondida de la piedra.")
    time.sleep(3)
    EL = "\n\"Bienvenido a la base.\"\n"
    for char in EL:
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    escogerarma()

def start():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    global NOM
    AP = 1
    VIDA = 3
    I = 0
    SAVE = 0
    APSAVE = 1
    HPSAVE = 3
    print("\n¡Bienvenido a Guardianes del Bosque!\n")
    time.sleep(2)
    print("¿Quieres conocer las instrucciones?\n")
    time.sleep(2)
    print("SI = S\nNO = N\n")
    while True:
        SIG=str(input())
        time.sleep(1)
        if SIG == "S":
            instrucciones()
            break
        elif SIG == "N":
            nombre()
            break
        elif SIG == "1":
            NOM = "PENE"
            patio()
            break
        else:
            print("\nNo entiendo lo que quieres hacer. Vuelve a intentarlo.\n")

def sobrevivir():
    global I
    global SAVE
    global VIDA
    global AP
    global APSAVE
    global HPSAVE
    COUNT = 0
    time.sleep(1)
    print("\nSe aproxima un bandido montado en caballo y te va a atacar. Teclea un número del 1-3 para ver tu resultado.\n")
    while True:
        if VIDA <= 0:
            time.sleep(2)
            print("Con el último golpe de tu enemigo, caes al piso y sueltas tu último respiro.")
            time.sleep(3)
            print("\nLograste derrotar a "+str(COUNT)+" enemigos.")
            time.sleep(2)
            gameover()
            break
        ATT=random.randint(1,3)
        SIG=str(input())
        time.sleep(1)
        if SIG == str(ATT):
            print("\nLogras sorprender a tu oponente y lo derrotas facilmente.") 
            COUNT+=1
            time.sleep(3)
            print("\nEn cuanto acabas con él, otro bandido toma su lugar y se aproxima hacia ti. Teclea un número del 1-3.\n")
        elif SIG == "REGRESAR":
            if SAVE == 0:
                print("\nNo hay juego guardado.\n")
            else:
                regresar()
                break
        elif SIG == "VIDA":
            if VIDA == 1:
                print("\nTienes "+str(VIDA)+" vida.\n")
            else:
                print("\nTienes "+str(VIDA)+" vidas.\n")
        elif SIG == "AP":
            print("\nTienes "+str(AP)+" Poder de Ataque.\n")
        elif SIG == "INVENTARIO":
            inventario()
        else:
            print("\nLe fallas a tu enemigo y él aprovecha para atacarte a ti.")
            RAN=random.randint(1,2)
            ATA=random.randint(1,2)
            time.sleep(2)
            if RAN == ATA:
                print("\nEl enemigo te pega fuertemente y te quita una vida. Teclea un número del 1-3 para atacar.\n")
                VIDA=VIDA-1
            else:
                print("\nEl enemigo te falla y regresa a su lugar. Tecela un número del 1-3 para atacar.\n")
    
start()
