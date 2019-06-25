import requests

r= requests.get('https://imgs.xkcd.com/comics/python.png')




print (r.status_code)
print (r.ok)
print (r.headers)
