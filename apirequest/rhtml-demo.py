
from requests_html import HTML

with open('index.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

print(html.html)
