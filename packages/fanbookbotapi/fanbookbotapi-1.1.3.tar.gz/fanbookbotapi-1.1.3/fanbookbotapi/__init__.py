apiurl='https://a1.fanbook.mobi/api/bot/'
apilist={
    'getme':apiurl+'getMe'
}

import requests,json

def getme(token) ->object:
    r=requests.get(apilist['getme'])
    return r