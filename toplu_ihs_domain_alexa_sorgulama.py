#coding:utf-8
import requests
import sys
from bs4 import BeautifulSoup
import re
from threading import Thread
coder= "* Cüneyt TANRISEVER *"
print "*"*len(coder)
print coder
print "*"*len(coder)
tolu=[]
sor=raw_input("Dosya adini giriniz = ")
oku=open(sor,"r").readlines()
urller=[]
for i in oku:
	dd=i.replace("http://","").replace("https://","").replace("/","")
	urller.append(dd)

yaz=open("alexsasiralama.txt","w")
yaz.close()


print str(len(urller))+" site inin alexsa sorgusu basladi bekleyiniz..."
def dex(sss):
	
	i=urller[sss]
	url="https://www.ihs.com.tr/seo/alexa-siralama-sorgulama/output"
	data={"url":i,"submit":"G%C3%B6nder"}
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
	rq=requests.session()
	rq.headers.update(headers)
	res=rq.post(url,data=data)
	rm=res.content
	soup = BeautifulSoup(rm,'html.parser')
	try:
		tab = soup.find("table",{"class":"table table-bordered"})
		tt= re.findall("<td>.+</td>",str(tab))
		sildunya1=[str(tt[1]).replace("<td>","").replace("</td>","")]
		sildunya2=str(sildunya1).replace("[","").replace("]","").replace("\'","").replace(",","")
		silulke=[str(tt[5]).replace("<td>","").replace("</td>","")]
		silulke1=str(silulke).replace("[","").replace("]","").replace("\'","").replace(",","")
		dunya= [str(tt[1]).replace("<td>","").replace("</td>","")," = dunya siralamasi  / "]
		ulkea= [str(tt[5]).replace("<td>","").replace("</td>","")," = ulke siralamasi / "]
		ulkeismi=["ulkesi = ", str(tt[3]).replace("<td>","").replace("</td>","")]
		dunya1=str(dunya).replace("[","").replace("]","").replace("\'","").replace(",","")
		ulke1=str(ulkea).replace("[","").replace("]","").replace("\'","").replace(",","")
		ulke2=str(ulkeismi).replace("[","").replace("]","").replace("\'","").replace(",","")

		if "No Global Rank  = dunya siralamasi  /" in str(dunya1) and "None  = ulke siralamasi /" in str(ulke1):
			print "url siralamada yok",i
			
		
		else:
			#print dunya1+ulke1+ulke2
			try:
				if int(sildunya2) <=3000000 and int(silulke1) <=3000000 :
					ekle=dunya1+ulke1+ulke2+" "
					#tolu.append()
					print ekle,i
					dex5=str(ekle)+" site = "+ str(i).replace("\n","").replace("\r","")
					
					yaz=open("alexsasiralama.txt","a")
					yaz.write(str(dex5)+"\n")
					yaz.close()
				else:
					ekle=dunya1+ulke1+ulke2+" "
					dex56=str(ekle)+" site = "+ str(i).replace("\n","").replace("\r","")
					print "alexasi 3m dan yuksek =",i
					yaz=open("3m-ustu-alexsasiralama.txt","a")
					yaz.write(str(dex56)+"\n")
					yaz.close()
			except ValueError:
				
				pass	
			except IndexError:
				pass
	except IndexError:
		pass	
def gdr():
	for i in range(len(urller)):
		dex(i)
	print "sonuclar alexsasiralama.txt dosyasina yazildi."	

gdr()


