import re
import Constants
from bs4 import BeautifulSoup
import sys
import Day, Month

#récupération jour du mois
def setDaysFromPage(soup):
    joursDuMois = []
    try:
        table = soup.select('tbody')[0].findAll('a', attrs={'style' : 'vertical-align: top; font-size:1.5em; line-height:1.5em; font-weight:normal'})
        for elem in table : 
            joursDuMois.append(re.sub(r'^(\n)+|\n$|(?!\b)( )+' , '' , elem.get_text())) #on scrap que le jour et le numéro, pas les espaces inutiles ni les \n

        # nbJoursMois = len(joursDuMois)
        # print(nbJoursMois)
        # print(joursDuMois)
    except IndexError:
        print ('index error on page, no tbody[0] in the html')
        return []

    return joursDuMois

#récupération températures du mois

def setCompleteTableMonths(soup):
    joursDuMois = setDaysFromPage(soup)
    nbJoursMois = len(joursDuMois)
    tempMinMois = []
    tempMaxMois = []
    completeTableMonth = []

    try:
        table = soup.select('tbody')[0].find_all('tr', class_='', limit=nbJoursMois) #all tr

        for elem in table : 
            tempMinMois.append(re.sub(r'^(\n)+|\n|(?!\b)( )+' , '' , elem.find_all('td')[0].get_text())) #first td is tempMin
            tempMaxMois.append(re.sub(r'^(\n)+|\n|(?!\b)( )+', '', elem.find_all('td')[1].get_text())) #second td is tempMax

    # print (len(tempMinMois))
    # print(tempMinMois)
    # print(len(tempMaxMois))
    # print(tempMaxMois)

        completeTableMonth = [joursDuMois, tempMinMois, tempMaxMois]
    except:
        print('Erreur')
        return[]
    
    return completeTableMonth

def generateURLs() : 
    for month in Constants.MONTHSYEAR :
        # print(month)
        Constants.URLS.append(Constants.DEPARTUREURLS + month + '/' + str(Constants.YEARDEPARTURE) + '/' + Constants.POSTFIXURLS)

def generateMonth(completeTableMonth) : 
    i=0
    day = Day.Day()
    day_list = []
    for i in range(0, len(completeTableMonth[0])):
        # print (completeTableMonth[0][i], ' ', completeTableMonth[1][i], ' ' , completeTableMonth[2][i])
        day = Day.Day(i+1, completeTableMonth[0][i], completeTableMonth[1][i], completeTableMonth[2][i])
        day_list.append(day)
    return Month.Month(0, '', 0, day_list, 0, 0, 0)