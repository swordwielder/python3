import requests


r = requests.get('twitter.com/qchen125')

print ("printing r")
print (r)
print ("r.context: --------------   ")
print (r.content)
print ("r.url: ---------------")
print (r.url)

