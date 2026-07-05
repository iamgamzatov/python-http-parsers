from urllib import request
from bs4 import BeautifulSoup
myUrl = 'http://my-first-flask-env.eba-npgrppep.eu-north-1.elasticbeanstalk.com'

otvet = request.urlopen(myUrl)
hhtml_content = otvet.read()

soup = BeautifulSoup(hhtml_content, 'html.parser')

print(soup)