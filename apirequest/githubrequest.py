import requests
import os

gituser = os.environ.get('GIT_USER')
gitpassword = os.environ.get('GIT_PASS')

r = requests.get('https://api.github.com/user', auth=(gituser, gitpassword))

print("r status code",r.status_code)
print("r headers",r.headers['content-type'])
print("r encoding",r.encoding)
print("r text",r.text)
print("r json",r.json())
