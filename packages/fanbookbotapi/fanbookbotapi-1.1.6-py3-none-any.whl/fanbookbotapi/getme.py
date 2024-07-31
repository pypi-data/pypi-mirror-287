import requests,json
from .apilist import *

def getme(token) ->object:
    r=requests.get(apilist['getme'])
    return r
