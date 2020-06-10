from bs4 import BeautifulSoup
import requests
import re
import Month, Day
import utils, exportData
import Constants
import datetime

#variables
nbJoursMois = 0
joursDuMois = []
tempMinMois = []
tempMaxMois = []
completeTableMonth=[]
months = []
current_month = Month.Month()

utils.generateURLs()
i=1
for url in Constants.URLS:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    print ('month for url : ', url)
    completeTableMonth =  utils.setCompleteTableMonths(soup)
    current_month = utils.generateMonth(completeTableMonth)
    current_month.numeroMois = i
    current_month.year = Constants.YEARDEPARTURE
    current_month.url=url
    for day in current_month.days:
        day.month = current_month  # we affiliate the current month for the day.
        day.canonicForm = datetime.date(Constants.YEARDEPARTURE, day.month.numeroMois, day.numeroJour) 
    months.append(current_month)
    i=i+1

for month in months:
    month.displayMonth()

exportData.toXLSX(months)
