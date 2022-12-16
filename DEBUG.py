dev=True
#librairies
from ast import Store
import os #la base;)
from os import * #la base;))
from time import sleep
from xml.etree.ElementTree import TreeBuilder#la base;)))
from tqdm import * #pour la barre de progression
import sys#Bah...
from sys import *#Bah c'est sys
#/////////////C++ = BAD :)
#Composants
BIOS = "refi" #UEFI/REFI/BIOS/UEFI CSM
Ram =  256 # X GO ex: 2 GO
####VAR POUR LE BON FONCTIONNEMENNT IZ OS A NE PAS TOUCHER !###########
izos = "booted"
username = "root" 
mdp =""
ComputerName = "[Kernel.DEBUGSYS]"
hlp = ['Store','listdir','shutdwn','calculatrice','GTAV','assembler','txtv2']
GTAV = False
calculator = False
assembler = False
txt = False
##############

def prgsbr(size , time):
    for i in tqdm(range(size)):
        sleep(time)
def boot():
    izos = "booting"
    if BIOS == "REFI" and Ram >= 128 or dev == True:
        prgsbr(200, 1/10)
    else:
        prgsbr(20, 1)
        izos = "booted"
def sprint(str):#ca c'est pour le slowprint
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     sleep(1/10)

def wait(time):#cest du (Nan c'est pas marrant :( ))C :)
    sleep(time)
izos = "booted"
#C'est PARTI !*
#login 1
userverif = input("Entrez le nom d'utilisateur: ")
mdpverif = input("Entrez le MDP:")
#verifification
if userverif == username and mdpverif == mdp:
    print("Bienvenue "+username.title()+" !")
else:
    #login2
    sprint("FAUX !")
    userverif = input("Entrez le nom d'utilisateur: ")
    mdpverif = input("Entrez le MDP:")
    print("Bienvevnue "+username.title()+"")
    ##############################################################SSSSHHHHHHEEEELLLLLLLLL#######################################
while izos == "booted": 

            
    choix = input(""+username+"@"+ComputerName+" $ ")
    if choix == "GTAV":
        if GTAV == True:
            GTAV()
        else:
            sprint("GTAV PAS ENCOREV INSTALLE.")
    if choix == "help":
        sprint("help")
        print(hlp)
    if choix == "shutdwn":
        confshtdwn = int(input("Etes vous sur 1.oui 2.non"))
        if confshtdwn == 1:
            izos = "shutdown"
            sys.exit("[IZ-OS_KERNEL]Shutdown at @service.shtdwn.service.c")
        else:
            sprint("[@KERNEL.sys}////Booting kernel sys...")
            sleep(4)
    if choix == "listdir":
        print(listdir())
    if choix != [hlp]:
        print(""+choix+": commande non trouvée") 
    if choix == "calculatrice":
        if calculator == True:
            calculatordef()
        else:
            print("L'app n'est pas installé")
    if choix == "txtv2":
        if txt ==  True:
            txt()
        else:
            sprint("L'app n'est pas installé ! ")
    if choix == "assemler":
        if assembler == True:
            assembler()
        else:
            sprint("L'app n'est pas installé")
    if choix  == "Store":
        print("Bienvenue au store !")
        sprint("..............")
        choixStore = input("Chercher une appli (exit pour quitter) (? pour la liste)")
        if choixStore == "?":
            lstapp = ['GTAV (DECONSEILLE)','Calculatrice','TXT CREATORv2','Message sender discord BOT EDITION']   
            print(lstapp)
        if choixStore == "exit":
            print("BYE, "+username.upper()+"")
            storevar = False
        if choixStore == "GTAV":
            if GTAV == True:
                sprint("GTAV DEJA INSTALLE")
            else:
                prgsbr(10000011 , 1/2)
                GTAV=True
                def GTAV():
                    gtavconf = input("Etes vous sur ? (oui/non)")
                    if gtavconf == "oui" or gtavconf == "Oui" or gtavconf == "OUI" or gtavconf == "o" or gtavconf == "O" or gtavconf == "yes"or gtavconf == "YES" or gtavconf == "y" or gtavconf == "Y":
                        izos = "corrupted"
                print("installé pour l'executer tapez GTAV.exe dans le terminal")
        if choixStore == "Calcultrice":
            if calculator == False:
                prgsbr(12 , 1/2)
                def calculatordef():
                    choice1 = int(input("Nombre 1:"))
                    choice2 = int(input("+ "))
                    print(choice1 + choice2)
                calculator = True
            else:
                sprint("Déja installé")
        if choixStore == "txt":
            def txt():
                txt = True
                while txt == True:

                    lstchoix = [1, 2, 3, 4, 5]
                    choixtxt = int(input("Bonjour ! 1.lire le fichier txt.txt 2.creer le fichier 3.ecrire dans le fichier 4.formater le fichier 5.quitter"))
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
        if choixStore == "assembler":
            if assembler == False:
                def assembler():
                    choice1 = input("Nombre1: ")
                    choice2 = input("+ ")
                    somme =  choice1 + choice2
                    print("= "+somme+"")

    