def barra_espaciadora ():
    print ("-" * 100)


def mini_espaciadora ():
    print (" - " * 9)

barra_espaciadora()


def notas ():
    
        print("Notas estudiantes") #se ponen notas de los estudiantes
        santiago1 = float (input("Nota Santiago primer corte: "))
        santiago2 = float (input("Nota Santiago segundo corte: "))
        santiago3 = float (input("Nota Santiago tercer corte: "))

        mini_espaciadora()

        gabriela1 = float (input ("Nota Gabriela primer corte: "))
        gabriela2 = float (input ("Nota Gabriela segundo corte: "))
        gabriela3 = float (input ("Nota Gabriela tercer corte: "))

        mini_espaciadora()

        juan1 = float (input("Nota Juan primer corte: "))
        juan2 = float (input("Nota Juan segundo corte: "))
        juan3 = float (input("Nota Juan tercer corte: "))

        mini_espaciadora() #se dividen entre el numero de cortes

        santiago= ((santiago1+ santiago2 + santiago3) / 3)
        gabriela= ((gabriela1+ gabriela2 + gabriela3) / 3)
        juan= ((juan1+ juan2 + juan3) / 3)

        #resultado si es aprobado o reprobado y convertir a str

        if santiago > 3:
            print("Santiago: Aprobado " + str(santiago))
        else:
            print("Santiago: Reprobado " + str(santiago))

        mini_espaciadora()
    
        if gabriela > 3:
            print ("Gabriela: Aprobado " + str(gabriela))  
        else:
            print("Gabriela: Reprobado " + str(gabriela))

        mini_espaciadora()

        if juan > 3:
            print ("Juan: Aprobado " + str(juan))
        else:
            print("Juan: Reprobado " + str(juan))
            

        barra_espaciadora()
while True:
    notas()
    continuar= input ("Quieres volver a introducir las notas? (si/no) ").lower()
    
    if continuar != "si":
      print ("pailox")
      break





