from lxml import html
import requests

pagespeld = requests.get("https://speld.nl/2017/12/13/")
treespeld = html.fromstring(pagespeld.content)
titlesspeld = treespeld.xpath("//a[@rel='bookmark']/text()")

pagenos = requests.get("https://nos.nl/nieuws/")
treenos = html.fromstring(pagenos.content)
titlesnos = treenos.xpath("//h3[@class='list-items__title list-items__link-hover']/text()")

pagenu = requests.get("https://www.nu.nl/net-binnen")
treenu = html.fromstring(pagenu.content)
titlesnu = treenu.xpath("//span[@class='title']/text()")

pagetelegraaf = requests.get("https://www.telegraaf.nl/")
treetelegraaf = html.fromstring(pagetelegraaf.content)
titlestelegraaf = treetelegraaf.xpath("//h2[@class='__headline break-words underline_hover underline_focus roboto-black-s gray2 top-margin-0 bottom-margin-0 right-padding-2']/text()")

print (titlesspeld)
print (titlesnos)
print (titlesnu)
print (titlestelegraaf)