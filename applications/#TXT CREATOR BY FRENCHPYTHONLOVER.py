# TXT CREATOR BY FRENCHPYTHONLOVER
def txt():
    txt = True
    while txt == True:

        lstchoix = [1, 2, 3, 4, 5]
        choixtxt = int(input(
            "Bonjour ! 1.lire le fichier txt.txt 2.creer le fichier 3.ecrire dans le fichier 4.formater le fichier 5.quitter"))
        if choixtxt == 1:
            fichopen = open("txt.txt", "r")
            print(fichopen.read())
        else:
            if choixtxt == 2:
                fichiercreate = open("txt.txt", "a")
                print(fichiercreate)
                fichiercreate.close()
            else:
                if choixtxt == 3:
                    writechoice = input("Que voulez vous écrire ?:")
                    fichier = open("data.txt", "a")
                    fichier.write(writechoice)
                    fichier.close()
                    print(""+writechoice+" écrit.")
                else:
                    if choixtxt == 4:
                        fichierformat = open("txt.txt", "w")
                        fichier.close()
                    else:
                        if choixtxt == 5:
                            txt = False
