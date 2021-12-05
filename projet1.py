
# get language from audio
def det(tx):
   from langdetect import DetectorFactory, detect
   d=detect(tx)
   return print(d)

# get country 
def country():
 import socket  
 
 hostname = socket.gethostname()   
 IPAddr = socket.gethostbyname(hostname)   
 print("Your Computer Name is:" + hostname)   
 my_country : get("IPAddr")
 print(my_country)
 
# get country from IP address
def get(ip):
    import requests
    import json
    import ipinfo
    endpoint = f'https://ipinfo.io/{ip}/json'
    response = requests.get(endpoint, verify = True)

    if response.status_code != 200:
        return 'Status:', response.status_code, 'Problem with the request. Exiting.'
        exit()
    
   
    data = response.json()

    countryname= data['country']
    import pycountry

    input_countries = ['countryname']

    countries = {}
    for country in pycountry.countries:
        countries[country.name] = country.alpha_3

        codes = [countries.get(country, 'Unknown code') for country in input_countries]

        return print(codes) 


# get official language of the country
def getlang(country):
 import mysql.connector

 mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="Mariem220587",
 database="world_x"
  
 )
 mycursor = mydb.cursor()

 mycursor.execute("select language from countrylanguage where countrycode ='country'")
 myresult = mycursor.fetchall()

 for x in myresult:
  return print(x)
  

  

# transalte the audio into the offical lanuguage of the country
def trans(phrase,lg):
 from googletrans import Translator, constants
 from pprint import pprint
 translator = Translator()
 translation = translator.translate("phrase", dest="lg")
 print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


# main
def main():
 import speech_recognition as sr
 r = sr.Recognizer()
 with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        det("{}".format(text))
        location=country()
        oglang=getlang(location)
        trad=trans("{}".format(text),oglang)
        print("you said:" +trad)
        
    except:
        print("Sorry could not recognize what you said")
main()
      
 


