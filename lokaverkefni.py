#Þröstur
#Hér importa ég random til að nota random tölur
import random
#Hér opna ég skrána og splitta henni
with open("spil.txt","r",encoding="utf-8") as skra:
    faersla = skra.read().split("\n")
#Hér er ég að byrja að stokka
stokka = random.sample(range(52),52)
#Hér gerui ég lista með númerum á spilunum sem tölvan og leikmaðurinn fær
leikmannaSpilTala = []
tolvaSpilaTala = []
#Hér klára ég að stokka spilin
for i in stokka:
    if i%2==0:
        tolvaSpilaTala.append(i)
    else:
        leikmannaSpilTala.append(i)
#Hér bý til lista fyrir spilinn
leikmadur = []
tolva = []
jafntefli = []
#Hér fara tölurnar í færsluna hjá Leikmanninum og Tölvuni
for i in leikmannaSpilTala:
    leikmadur.append(faersla[i])
for i in tolvaSpilaTala:
    tolva.append(faersla[i])
#Hér er While lykkjan sem heldur leiknum gangandi
while len(leikmadur)>0 and len(tolva)>0:
#Hér er prentað út að Leikmaður á leik og einnig spilið hanns

    print("Leikmaður á leik")
#Hér er verið að splitta spilinu í nafn og flokka
    spil1 = leikmadur[0].split(":")
    spil2 = tolva[0].split(":")
#Hér er prentað út flokkana svo að leikmaðurinn geti valið flokk
    print("Flokkarnir")
    print("1. Þyngd (kg)")
    print("2. Mjólkurlagni (dætra)")
    print("3. Einkunn ullar")
    print("4. Fjöldi afkvæma")
    print("5. Einkunn læris")
    print("6. Frjósemi")
    print("7. Gerð/þykkt bakvöðva")
    print("8. Einkun fyrir malir")
    print("Þetta er spilið þitt")
#Hér er prentað út efsta spilið
    print(spil1)
#Hér fær notandinn að velja hvaða flokk hann ætlar að nota
    val = int(input("Hvaða flokk vilt þú nota? "))

    flokkarspil1 = spil1[1].split(",")
    print(flokkarspil1[val-1])
    flokkarspil2 = spil2[1].split(",")
#Ef notandi vinnur þá fer forritið hingað
    if float(flokkarspil1[val-1]) > float(flokkarspil2[val-1]):
        print("Þú vannst")
        if len(jafntefli)>0:
            for spil in jafntefli:
                leikmadur.append(spil)
            jafntefli.clear()
        leikmadur.append(leikmadur[0])
        leikmadur.remove(leikmadur[0])
        leikmadur.append(tolva[0])
        tolva.remove(tolva[0])
#Ef talvan vinnur fer forritið hingað
    elif float(flokkarspil2[val-1]) > float(flokkarspil1[val-1]):
        print("Talvan vann")
        if len(jafntefli)>0:
            for spil in jafntefli:
                tolva.append(spil)
            jafntefli.clear()
        tolva.append(tolva[0])
        tolva.remove(tolva[0])
        tolva.append(leikmadur[0])
        leikmadur.remove(leikmadur[0])
#Ef það verður jafntefli fer forritið hingað
    else:
        print("Jafntefli")
        jafntefli.append(leikmadur[0])
        jafntefli.append(tolva[0])
        leikmadur.remove(leikmadur[0])
        tolva.remove(tolva[0])
        print(jafntefli)

#Þegar tölvan á leik fer forritið hingað
    print("Talvan á leik")
    val = random.randint(0,7)
    flokkarspil1 = spil1[1].split(",")
    flokkarspil2 = spil2[1].split(",")
    jafntefli = []
#Ef notandi vinnur fer forritið hingað
    if float(flokkarspil1[val]) > float(flokkarspil2[val]):
        print("Þú vannst")
        if len(jafntefli)>0:
            for spil in jafntefli:
                leikmadur.append(spil)
            jafntefli.clear()
        leikmadur.append(leikmadur[0])
        leikmadur.remove(leikmadur[0])
        leikmadur.append(tolva[0])
        tolva.remove(tolva[0])
#Ef talvan vinnur fer forritið hingað
    elif float(flokkarspil2[val]) > float(flokkarspil1[val]):
        print("Talvan vann")
        if len(jafntefli)>0:
            for spil in jafntefli:
                tolva.append(spil)
            jafntefli.clear()
        tolva.append(jafntefli)
        tolva.append(tolva[0])
        tolva.remove(tolva[0])
        tolva.append(leikmadur[0])
        leikmadur.remove(leikmadur[0])
#Ef það verður jafntefli fer forritið hingað
    else:
        print("Jafntefli")
        jafntefli.append(leikmadur[0])
        jafntefli.append(tolva[0])
        print(jafntefli)

#þegar sigurvegari er kominn upp þá er prentað út hérna hver vann
if len(leikmadur) == 0:
    print("Talvan vann leikinn!")
    print("Takk fyrir leikinn :)")
elif len(tolva) == 0:
    print("Þú vannst leikinn!")
    print("Takk fyrir leikinn :)")