def lisa_sõna(Pealinnad:dict, a:str)->dict:
	"""
	"""
	a=input("Введите значение слова: ") #просим ввести значение
	Capitals.update({a.title():b.title()}) #добавляем 
	return Pealinnad
def lisa_sse(sonastik:dict)->dict:
    """
	"""
    riik = input("Введите страну: ")
    linn = input("Введите столицу: ")
    sonastik[riik] = linn
    sonastik[linn] = riik
    return sonastik
print("Добро пожаловать в словарь стран, столиц!")
Capitals=["Tallinn","Tirana","Brussels","Prague","Warsaw","Lisbon","Helsinki","Paris","Berlin"]
Countries=["Estonia","Albania","Belgium","Czechia","Poland","Portugal","Finland","France","Germany"]
sonastik = {'Estonia': 'Tallinn', 'Russia' : 'Moscow', 'Tallinn' : 'Estonia', 'Moscow' : 'Russia', 'Riga': 'Latvia', 'Latvia': 'Riga', 'Finland': 'Helsinki', 'Helsinki': 'Finland', 'Sweden': 'Stockholm', 'Stockholm': 'Sweden', 'Germany': 'Berlin', 'Berlin': 'Germany', 'France': 'Paris', 'Paris': 'France','Italy': 'Rome', 'Rome': 'Italy','Belarus': 'Minsk','Minsk': 'Belarus','China': 'Pekin','Pekin': 'China','Japan': 'Tokyo','Tokyo': 'Japan','USA': 'Washington', 'Wasgington':'USA','Brasilia': 'Brasilia','Portugal': 'Lissabon', 'Lissabon': 'Portugal'}
Capitals={} 
Capitals = dict() 
Capital={} 
Capital = dict()
Capitals['Albaania'] = 'Tirana'
Capitals['Andorra'] = 'Andorra la Vella'
Capitals['Armeenia'] = 'Jerevan'
Capitals['Aserbaidžaan'] = 'Bakuu'
Capitals['Austria'] = 'Viin'
Capitals['Belgia'] = 'Brüssel'
Capitals['Bosnia ja Hertsegoviina'] = 'Sarajevo'
Capitals['Bulgaaria'] = 'Sofia'
Capitals['Eesti'] = 'Tallinn'
Capitals['Gruusia'] = 'Thbilisi'
Capitals['Hispaania'] = 'Madrid'
Capitals['Horvaatia'] = 'Zagreb'
Capitals['Iirimaa'] = 'Dublin'
Capitals['Island'] = 'Reykjavík'
Capitals['Itaalia'] = 'Rooma'
Capitals['Kasahstan'] = 'Astana'
Capitals['Kreeka'] = 'Ateena'
Capitals['Küpros'] = 'Nikosia'
Capitals['Leedu'] = '	Vilnius'
Capitals['Liechtenstein'] = 'Vaduz'
Capitals['Luksemburg'] = 'Luxembourg'
Capitals['Läti'] = 'Riia'
Capitals['Madalmaad'] = 'Amsterdam'
Capitals['Makedoonia'] = 'Skopje'
Capitals['Malta'] = 'Valletta'
Capitals['Moldova'] = 'Chisinau'
Capitals['Monaco'] = 'Monaco'
Capitals['Montenegro'] = 'Podgorica'
Capitals['Norra'] = 'Oslo'
Capitals['Poola'] = 'Varssavi'
Capitals['Portugal'] = 'Lissabon'
Capitals['Prantsusmaa'] = 'Pariis'
Capitals['Rootsi'] = 'Stockholm'
Capitals['Rumeenia'] = 'Bukarest'
Capitals['Saksamaa'] = 'Berliin'
Capitals['San Marino'] = 'San Marino'
Capitals['Serbia'] = 'Belgrad'
Capitals['Slovakkia'] = 'Bratislava'
Capitals['Sloveenia'] = 'Ljubljana'
Capitals['Soome'] = 'Helsingi'
Capitals['Suurbritannia'] = 'London'
Capitals['Šveits'] = 'Bern'
Capitals['Taani'] = 'Kopenhaagen'
Capitals['Tšehhi'] = 'Praha'
Capitals['Türgi'] = 'Ankara'
Capitals['Ukraina'] = 'Kiiev'
Capitals['Ungari'] = 'Budapest'
Capitals['Valgevene'] = 'Minsk'
Capitals['Vatikan'] = 'Vatican'
Capitals['Venemaa'] = 'Moskva'
Capital['Tirana'] = 'Albaania'
Capital['Andorra la Vella'] = 'Andorra'
Capital['Jerevan'] = 'Armeenia'
Capital['Bakuu'] = 'Aserbaidžaan'
Capital['Viin'] = 'Austria'
Capital['Brüssel'] = 'Belgia'
Capital['Sarajevo'] = 'Bosnia ja Hertsegoviina'
Capital['Sofia'] = 'Bulgaaria'
Capital['Tallinn'] = 'Eesti'
Capital['Thbilisi'] = 'Gruusia'
Capital['Madrid'] = 'Hispaania'
Capital['Zagreb'] = 'Horvaatia'
Capital['Dublin'] = 'Iirimaa'
Capital['Reykjavík'] = 'Island'
Capital['Rooma'] = 'Itaalia'
Capital['Astana'] = 'Kasahstan'
Capital['Ateena'] = 'Kreeka'
Capital['Nikosia'] = 'Küpros'
Capital['Vilnius'] = '	Leedu'
Capital['Vaduz'] = 'Liechtenstein'
Capital['Luxembourg'] = 'Luksemburg'
Capital['Riia'] = 'Läti'
Capital['Amsterdam'] = 'Madalmaad'
Capital['Skopje'] = 'Makedoonia'
Capital['Valletta'] = 'Malta'
Capital['Chisinau'] = 'Moldova'
Capital['Monaco'] = 'Monaco'
Capital['Podgorica'] = 'Montenegro'
Capital['Oslo'] = 'Norra'
Capital['Varssavi'] = 'Poola'
Capital['Lissabon'] = 'Portugal'
Capital['Pariis'] = 'Prantsusmaa'
Capital['Stockholm'] = 'Rootsi'
Capital['Bukarest'] = 'Rumeenia'
Capital['Berliin'] = 'Saksamaa'
Capital['San Marino'] = 'San Marino'
Capital['Belgrad'] = 'Serbia'
Capital['Bratislava'] = 'Slovakkia'
Capital['Ljubljana'] = 'Sloveenia'
Capital['Helsingi'] = 'Soome'
Capital['London'] = 'Suurbritannia'
Capital['Bern'] = 'Šveits'
Capital['Kopenhaagen'] = 'Taani'
Capital['Praha'] = 'Tšehhi'
Capital['Ankara'] = 'Türgi'
Capital['Kiiev'] = 'Ukraina'
Capital['Budapest'] = 'Ungari'
Capital['Minsk'] = 'Valgevene'
Capital['Vatican'] = 'Vatikan'
Capital['Moskva'] = 'Venemaa'
Countries=input("Введи страну или город: ") 
countries=Countries.title()
if countries in Capitals:
    print('Столица страны ' + Countries + ': ' + Capitals[countries])
elif countries in Capital:
    print('Страна столицы ' + Countries + ': ' + Capital[countries])
else:
    print('В базе нет страны c названием ' + countries)
p=input("Хотите ли пройти тест на знания столиц Европы? 1-Да или 2-Нет? ")
if p=="1":
        Countries.sort()
        Countries.reverse()
        m=0
        for i in range(10):
            print(choices(Countries))
            st=input("Введите столицу: ")
            if st in Capitals:
                    print("Правильно!")
                    m+=1
            else:
                print("Неправильно!")
        if m==0:
            print("0%")
        elif m==1:
            print("10%")
        elif m==2:
            print("20%")
        elif m==3:
            print("30%")
        elif m==4:
            print("40%")
        elif m==5:
            print("50%")
        elif m==6:
            print("60%")
        elif m==7:
            print("70%")
        elif m==8:
            print("80%")
        elif m==9:
            print("90%")
        elif m==10:
            print("100%")
if p=="2":
        print("Пока!")
while True:
    print("Хочешь что-то исправить? \n1-Да \n2 - Нет")
    valik_=input()
    if valik_=="1":
        l_=input("Напиши столицу или страну на английском языке: ").title()
        if l_ in sonastik.keys():
            vast=sonastik[l_]
            print(vast)  
        else:
            print("Такого нету в словаре")
            print("Напиши 1 если хочешь добавить в словарь")
            print("Напиши 2 если ничего не хочешь изменять")
            valik=input()
            while True:
                if valik=="1":
                    lisa_sse(sonastik)
                    print(sonastik)
                elif valik=="2":
                    break
                else:
                    print("")
                   


