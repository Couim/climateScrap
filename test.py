from bs4 import BeautifulSoup
import requests
import re

URL = "https://www.infoclimat.fr/climatologie-mensuelle/27612/fevrier/2020/moskva-moscou.html"
r = requests.get(URL)


soup = BeautifulSoup(r.content, 'html.parser')
nbJoursMois = 0
joursDuMois = []
tempMinMois = []
tempMaxMois = []
tabeauMoisComplet=[]

#récupération jour du mois


table = soup.select('tbody')[0].findAll('a', attrs={'style' : 'vertical-align: top; font-size:1.5em; line-height:1.5em; font-weight:normal'})

for elem in table : 
    joursDuMois.append(re.sub(r'^(\n)+|\n$|(?!\b)( )+' , '' , elem.get_text())) #on scrap que le jour et le numéro, pas les espaces inutiles ni les \n
nbJoursMois = len(joursDuMois)
print(nbJoursMois)
print(joursDuMois)

#récupération températures du mois

table = soup.select('tbody')[0].find_all('tr', class_='', limit=nbJoursMois)

for elem in table : 
    tempMinMois.append(re.sub(r'^(\n)+|\n|(?!\b)( )+' , '' , elem.find_all('td')[0].get_text()))
    tempMaxMois.append(re.sub(r'^(\n)+|\n|(?!\b)( )+', '', elem.find_all('td')[1].get_text()))

# print (len(tempMinMois))
# print(tempMinMois)
# print(len(tempMaxMois))
# print(tempMaxMois)

tabeauMoisComplet = [joursDuMois, tempMinMois, tempMaxMois]
print (tabeauMoisComplet)

i=0
for i in range(0, nbJoursMois):
    print (tabeauMoisComplet[0][i], ' ', tabeauMoisComplet[1][i], ' ' , tabeauMoisComplet[2][i])