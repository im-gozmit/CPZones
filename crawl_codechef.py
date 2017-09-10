import requests
from lxml import html
from lxml import etree

url = "https://www.codechef.com/users/akshayv3"
head = {}
head['user-agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.103 Safari/537.36"

page = requests.get(url , headers = head)
tree = html.fromstring(page.content)
name = tree.xpath('/html/body/main/div/div/div/div/div/section[6]/div/article[1]/p[1]/span/a') # Ye inspect krke milega left click and xpath


x = len(name)
for i in range( 0 , x):

	print name[i].text_content()



