#coding:utf-8
import re
import requests
coder= "* Cüneyt TANRISEVER *"
print "*"*len(coder)
print coder
print "*"*len(coder)
yaz=open("4milyon_alti_siteler.txt","w")
yaz.close()
yaz=open("4milyon_ustu_siteler.txt","w")
yaz.close()
oku=raw_input("Dosya adini gir = ")
oku1=open(oku,"r").readlines()
urller=[]
ekle=[]
alexsa=[]
def cektir(domain):
    try:
        i=urller[domain]
        url="http://data.alexa.com/data?cli=10&url=%s"%(i)


        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
        rq=requests.session()
        rq.headers.update(headers)
        dex=rq.get(url).content
        globalrank= re.findall("TEXT=\"(.*?)\"",dex)
        ulkealexsa=re.findall("RANK=\"(.*?)\"",dex)
        ulkeadi=re.findall("NAME=\"(.*?)\"",dex)
        siteadi=re.findall("IDN=\"(.*?)\"",dex)
        
        
        if globalrank != [] and ulkealexsa != []:
            gbrank=int(str(globalrank).replace("\'","").replace("[","").replace("]",""))
            ulkerank=int(str(ulkealexsa[1]).replace("\'","").replace("[","").replace("]",""))
###################################################################################
            globalrank1=int(str(globalrank).replace("\'","").replace("[","").replace("]",""))," = dunya alexasi // "
            ulkealexsa1=int(str(ulkealexsa[1]).replace("\'","").replace("[","").replace("]","")), " = ulke alexasi "
            ulkeadi1=" // ulke adi = ",str(ulkeadi).replace("\'","").replace("[","").replace("]","")
            sitead=" // site adi = ",str(siteadi).replace("\'","").replace("[","").replace("]","")
##################################################################################
#print globalrank1 ,ulkealexsa1,ulkeadi1
            if gbrank and ulkerank !=[]:
                if gbrank <=4000000 and ulkerank <=4000000:
                    duzen=globalrank1+ulkealexsa1+ulkeadi1+sitead
                    ekle.append(duzen)
                    print duzen
                else:
                    duzen1=globalrank1+ulkealexsa1+ulkeadi1+sitead
                    alexsa.append(duzen1)
                    print duzen1
        
        else:
            print "Site Siralamada yok"
    except ValueError:
        pass	
    except IndexError:
        pass
def sirala():
    dex1= sorted(ekle)  
    dex2= sorted(alexsa)
    for i in dex1:
        d=str(i).replace("[","").replace("\'","").replace("]","").replace(",","")
        dd=d.replace("(","").replace(")","")
        yaz=open("4milyon_alti_siteler.txt","a")
        yaz.write(str(dd)+"\n")
        yaz.close()
    for i in dex2:
        d=str(i).replace("[","").replace("\'","").replace("]","").replace(",","")
        dd=d.replace("(","").replace(")","")
        yaz=open("4milyon_ustu_siteler.txt","a")
        yaz.write(str(dd)+"\n")
        yaz.close()
    print "sonuclar = 4milyon_alti_siteler.txt ve 4milyon_ustu_siteler.txt dosyalarina yazilmistir"

for i in oku1:
	dd=i.replace("http://","").replace("https://","").replace("/","").replace("\r","").replace("\n","")
	urller.append(dd)
def gdr():
	for i in range(len(urller)):
		cektir(i)
	sirala()

gdr()

        
