import urllib2
req=urllib2.urlopen('https://lucici.tuchong.com/13790957/')
buf=req.read()
import re
list=re.findall(r'https://photo.tuchong.com.+\.jpg',buf)
i=0
for url in list:
    f=open(str(i)+'.jpg','w')
    req=urllib2.urlopen(url)
    buf=req.read()
    f.write(buf)
    f.close()
    i=i+1