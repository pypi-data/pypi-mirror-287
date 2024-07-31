import requests,json,apilist

def getme(token) ->object:
    r=requests.get(apilist.apilist['getme'])
    return r
