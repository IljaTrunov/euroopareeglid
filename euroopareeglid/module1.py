from gtts import gTTS
import os
def sonastik():
        sonastik={}
        countries=[]
        capitals=[]
        file=open("reeglid.txt","r")
        for line in file:
            k, v=line.strip().split("-")
            sonastik[k.strip()]=v.strip()
            countries.append(k)
            capitals.append(sonastik[k.strip()])
        file.close()
        print(sonastik)
        print("Countries: ")
        print(countries)
        print("Capitals:")
        print(capitals)
        s=gTTS(text=capitals[6],lang="en",slow=True).save("reeglid.mp3")
        os.system("reeglid.mp3")
        a=input()



def country ():
	countries=input("Введите страну - ")
	capitals=input("Введите столицу - ")
	with open("reeglid.txt", "a") as countries:
		countries.write(country+"\n")
	with open("capitals.txt", "a") as capitals: 
		capitals.write(capital+"\n")
def count():
    for country in Countries:
        country=input("Enter your country:")
    if Countries in Capitals:
        print("The capital of country:" +country +" - "+Capitals[country])
