from lxml import html
import requests

page = requests.get("https://www.buzzfeed.com/")
tree = html.fromstring(page.content)
titles = tree.xpath("//h2[@class='xs-mb05 xs-pt05 sm-pt0 xs-text-4 sm-text-2 bold']/text()")

print (titles)