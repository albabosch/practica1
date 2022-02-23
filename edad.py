
sortir = False
while sortir != True:
    
    edad = int(input("Indica la teva edat: "))
    if (edad < 18):
        print("Ets menor d'edat.")
    else:
        print("Ets major d'edat")

    fora = input("Vols sortir del programa? (SI/NO): ")

    if fora == "SI":
        sortir = True



    