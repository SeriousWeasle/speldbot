from lxml import html
import requests

pagespeld = requests.get("https://speld.nl/2017/12/13/")
treespeld = html.fromstring(pagespeld.content)
titlesspeld = treespeld.xpath("//a[@rel='bookmark']/text()")

pagenos = requests.get("https://nos.nl/nieuws/")
treenos = html.fromstring(pagenos.content)
titlesnos = treenos.xpath("//h3[@class='list-items__title list-items__link-hover']/text()")

pagertl = requests.get("https://www.rtl.nl/")
treertl = html.fromstring(pagertl.content)
titlesrtl = treertl.xpath("//h3[@class='title-element---title']/text()")

print (titlesspeld)
print (titlesnos)
print (titlesrtl)