from urllib import request
import sys

myUrl = 'http://adv400.tripod.com/kartinka.jpg'
myFile = 'C:\\parser\\kartinka.jpg'

try:
    print('Stat Downloading File from: ' + myUrl)
    request.urlretrieve(myUrl, myFile)
except Exception:
    print('Error downloading')
    print(sys.exc_info()[1])
    exit

