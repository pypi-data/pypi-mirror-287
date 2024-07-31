apiurl='https://a1.fanbook.mobi/api/bot/'
apilist={
    'getme':apiurl+'getMe'
}

from .getme import *

__all__ = ['getme']