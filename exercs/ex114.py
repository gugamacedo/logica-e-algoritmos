# verifique se dá pra acessar um site
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://github.com/gugamacedo')
except Exception as erro:
    print('O pai tá off 😴')
else:
    print('O pai tá on 😎')
