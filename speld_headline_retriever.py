from lxml import html
import requests

page = requests.get("https://speld.nl/2017/12/13/")
tree = html.fromstring(page.content)

titles = tree.xpath("//a[@rel='bookmark']/text()")

print (titles)