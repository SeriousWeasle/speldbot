from lxml import html
import requests
import time

#complete despeld loop for eternity's bound
#also can be commented out if all information is gotton
Ftime=time.time()
for year in [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]:
    for month in range(13):
        for day in range(32):
            try:
                pagespeld4ever = requests.get("https://speld.nl/"+str(year)+"/"+str(month)+"/"+str(day)+"/")
                treespeld4ever = html.fromstring(pagespeld4ever.content)
                titlesspeld4ever = treespeld4ever.xpath("//a[@rel='bookmark']/text()")
                print("current date:"+str(year)+"/"+str(month)+"/"+str(day))
                with open("headersmap/speldheaders.txt",'r') as readingMAT:
                    EASYREADING = readingMAT.read()
                    for TITLE in titlesspeld4ever:
                        try:
                            if((EASYREADING.index(TITLE) == False) == False):
                                pass
                        except:
                            with open("headersmap/speldheaders.txt",'a') as dcmt:
                                try:
                                    dcmt.write(str(TITLE))
                                    dcmt.write("|")
                                except:
                                    pass
            finally:
                pass
Fintime = time.time() - Ftime
print("It took {} minutes to get though all of 'the speld'!".format(str(Fintime/60)))
            

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

pagenietspeld = requests.get("https://www.reddit.com/r/nietdespeld/")
treenietspeld = html.fromstring(pagenietspeld.content)
titlesnietspeld = treenietspeld.xpath("//a[@tabindex='1']/text()")

websites = [["nos",titlesnos],["nietspeld",titlesnietspeld],["nu",titlesnu],["telegraaf",titlestelegraaf],["speld",titlesspeld]]

for site in websites:
    headers = site[0]+"headers.txt"
    with open("headersmap/"+headers,'r') as readingMAT:
        EASYREADING = readingMAT.read()
        for TITLE in site[1]:
            try:
                if((EASYREADING.index(TITLE) == False) == False):
                    pass
            except:
                with open("headersmap/"+headers,'a') as dcmt:
                    dcmt.write(str(TITLE))
                    dcmt.write("|")
            finally:
                pass
                


#print (titlesspeld)
#print (titlesnos)
#print (titlesnu)
#print (titlestelegraaf)
#print (titlesnietspeld)
