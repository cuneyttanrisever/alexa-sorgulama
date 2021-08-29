#coding:utf-8
import re
import requests
coder= "* Cüneyt TANRISEVER *"
print ("*"*len(coder))
print (coder)
print ("*"*len(coder))
yaz=open("4milyon_alti_siteler.txt","w")
yaz1=open("4milyon_ustu_siteler.txt","w")
sor=input("Dosya adini gir = ")
oku=open(sor,"r").readlines()
urller=[]
_4_m_alti=[]
_4_m_ustu=[]
for i in oku:
	site=i.replace("http://","").replace("https://","").replace("/","").replace("\r","").replace("\n","")
	urller.append(site)
def cektir(domain):
    try:
        i=urller[domain]
        url="http://data.alexa.com/data?cli=10&url={}".format(i)
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
        rq=requests.session()
        rq.headers.update(headers)
        dex=rq.get(url).content
        globalrank= re.findall("TEXT=\"(.*?)\"",str(dex))
        ulkealexsa=re.findall("RANK=\"(.*?)\"",str(dex))
        ulkeadi=re.findall("NAME=\"(.*?)\"",str(dex))
        siteadi=re.findall("IDN=\"(.*?)\"",str(dex))
        if globalrank != [] and ulkealexsa != []:
            gbrank=int(str(globalrank).replace("\'","").replace("[","").replace("]",""))
            ulkerank=int(str(ulkealexsa[1]).replace("\'","").replace("[","").replace("]",""))
###################################################################################
            globalrank1=int(str(globalrank).replace("\'","").replace("[","").replace("]",""))," = dunya alexasi // "
            ulkealexsa1=" ulke alexasi = ",int(str(ulkealexsa[1]).replace("\'","").replace("[","").replace("]",""))
            ulkeadi1=" // ulke adi = ",str(ulkeadi).replace("\'","").replace("[","").replace("]","")
            sitead=" // site adi = ",str(siteadi).replace("\'","").replace("[","").replace("]","").replace("/","")
##################################################################################
            if gbrank and ulkerank !=[]:
                if gbrank <=4000000 and ulkerank <=4000000:
                    duzen=globalrank1+ulkealexsa1+ulkeadi1+sitead
                    _4_m_alti.append(duzen)
                    print (duzen)
                else:
                    duzen=globalrank1+ulkealexsa1+ulkeadi1+sitead
                    _4_m_ustu.append(duzen)
                    print (duzen)
        
        else:
            print ("Site Siralamada yok")
    except ValueError:
        pass	
    except IndexError:
        pass
def sirala():
    dex1= sorted(_4_m_alti)  
    dex2= sorted(_4_m_ustu)
    for i in dex1:
        d=str(i).replace("[","").replace("\'","").replace("]","").replace(",","")
        dd=d.replace("(","").replace(")","")
        yaz.write(str(dd)+"\n")

    for i in dex2:
        d=str(i).replace("[","").replace("\'","").replace("]","").replace(",","")
        dd=d.replace("(","").replace(")","")
        yaz1.write(str(dd)+"\n")

    print ("sonuclar = 4milyon_alti_siteler.txt ve 4milyon_ustu_siteler.txt dosyalarina yazilmistir")
    yaz.close()
    yaz1.close()

def gonder():
	for i in range(len(urller)):
		cektir(i)
	sirala()

gonder()

        
