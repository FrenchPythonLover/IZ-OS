dev=True
#librairies


from ast import Store
import os #la base;)
from os import * #la base;))
from time import sleep#la base;)))
from tqdm import * #pour la barre de progression
import sys#Bah...
from sys import *#Bah c'est sys
#
#Composants
BIOS = "BIOS" #UEFI/REFI/BIOS/UEFI CSM
Ram = 2 # X GO ex: 2 GO
####VAR POUR LE BON FONCTIONNEMENNT IZ OS A NE PAS TOUCHER !###########
izos = ""
username = "" 
mdp =""
ComputerName = ""
GTAV = False
##############
def prgsbr(size , time):
    for i in tqdm(range(size)):
        sleep(time)
def boot():
    izos = "booting"
    if BIOS == "REFI" and Ram >= 128 or dev == True:
        for i in tqdm(range(100)):
            izos = "booted"
    else:
        for i in tqdm(range(20)):
            sleep(1)
            izos = "booted"
def sprint(str):#ca c'est pour le slowprint
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     sleep(1/10)

def wait(time):#cest du C :)
    sleep(time)
#configuration
sprint("Bienvenue sur IZ OS !--")
username = str(input("Choissiez un nom d'utilistaeur :"))
sprint(username)
sprint("Très beau nom !")
mdp = input("Saissisez un mot de passe (mdp):")
sprint("Très beau Mot De Passe!")
ComputerName=input("Entrez un Nom de machine:")
sprint("OK Récapitulatif")
print("Nom = "+username+"")
wait(2)
print("Nom de machine = "+ComputerName+"")
wait(2)
print("MDP = "+mdp+"")
wait(3)
conf = input("Vous etes sur de poursuivre l'installation ? (O/N):")
if conf == "O" or conf == "o" or conf == "Y" or conf == "y":
    print("PARFAIT !")
else:
    boot()
    for i in tqdm(range(4)):#"installation"
        sleep(2)
        def reboot():
            boot()
            userverif = input("Entrez le nom d'utilisateur: ")
            mdpverif = input("Entrez le MDP:")
            if userverif == username and mdpverif == mdp:
                print("Bienvenue "+username.upper()+" !")
    izos = "Ready to use"
    izos = "booted"
boot()
boot()
izos = "booted"
#C'est PARTI !
userverif = input("Entrez le nom d'utilisateur: ")
mdpverif = input("Entrez le MDP:")
if userverif == username and mdpverif == mdp:
    print("Bienvenue "+username.upper()+" !")
else:
    sprint("FAUX !")
    userverif = input("Entrez le nom d'utilisateur: ")
    mdpverif = input("Entrez le MDP:")
while izos == "booted":
    choix = input(""+username+"@"+ComputerName+"")
    if choix == "help":
        sprint("help")
        print("Store help listdir(real machine)")
    if choix == "listdir":
        listdir()
    if choix == "Store" or choix == "store":
        print("Bienvenue au store !")
        sprint("..............")
        choixStore = input("Chercher une appli (? pour la liste)")
        if choixStore == "?":
            lstapp = ['GTAV (DECONSEILLE)','Calculatrice','TXT CREATORv2']   
            print(lstapp)
        if choixStore == "GTAV":
            if GTAV == True:
                sprint("GTAV DEJA INSTALLE")
            else:
                prgsbr(10000011 , 1/2)
                def GTAV():
                    gtavconf = input("Etes vous sur ? (oui/non)")
                    if gtavconf == "oui" or gtavconf == "Oui" or gtavconf == "OUI" or gtavconf == "o" or gtavconf == "O" or gtavconf == "yes"or gtavconf == "YES" or gtavconf == "y" or gtavconf == "Y":
                        izos = "corrupted"
                print("installé pour l'executer tapez GTAV.exe dans le terminal")
            if choixStore == "exit":
                print("BYE, "+username.upper()+"")

        
    