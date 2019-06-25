import requests

li = ["r.status_code","r.ok","r.header","r.content","r.text","requests.get/requests.post vs params/data","r_dict['form']"]


r= requests.get('http://httpbin.org/delay/2' , timeout=3)

print (r)



r= requests.get('https://imgs.xkcd.com/comics/python.png')
with open('comic.png','wb') as f:
	f.write(r.content)



