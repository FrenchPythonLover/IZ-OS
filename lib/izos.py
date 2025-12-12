###### IZOS.py
import rich,os,hashlib,sys,warnings,time,psutil,platform,data,tmp
from rich.prompt import Prompt
def input(q=""):
    return Prompt.ask(q.replace(":",""))
from rich import print # making the default print from rich
initsystem = "./shell/init.py" # init program path
loginsystem = "./shell/login.py" # login program path

#Functions

def ok(text): 
    print(f"\[[green] OK [/green]] {text}")
def error(text):
    print(f"\[[red] FATAL [/red]] {text}")
def warn(text):
    print(f"\[[yellow] WARN [/yellow]] {text}")
def info(text):
    print(f'\[[blue] INFO [/blue]] {text}')