from cmd import Cmd
import os

def columnize(s:list):
    Cmd().columnize(s)

def public (obj):
    columnize(list(filter(lambda s: not s.startswith('_'), dir(obj))))   

def ls (s=os.curdir):
    columnize(sorted(os.listdir(s)))

def dispose_of(s):
    pass
    
def ask(prompt):
    """ Print the prompt and return the response. """
    pass
