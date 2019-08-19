import requests
import os


gituser = "swordwielder" #os.environ.get('GIT_USER')
gitpassword ="Well1170"  #os.environ.get('GIT_PASS')

r = requests.get('https://api.github.com/user', auth=(gituser, gitpassword))

print("r status code",r.status_code)
print("r headers",r.headers['content-type'])
print("r encoding",r.encoding)
print("r text",r.text)
print("r json",r.json())



user = "swordwielder"
password = "Well1170"

#r = requests.get('https://github.com/swordwielder/json-server', auth=(user,password))

#print("r status code",r.status_code)
#print("r headers",r.headers['content-type'])
#print("r encoding",r.encoding)
#print("r text",r.text)
#print("r json",r.json())
