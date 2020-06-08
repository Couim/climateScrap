import Day

class Month:
    def __init__ (self, url=None, numeroMois=None, year=None, days=None, avg_tmpMin=None, avg_tmpMax=None, cumulated_rain=None) :
        self.numeroMois=numeroMois or 0
        self.days = days or [] #list of days from Day class
        self.avg_tmpMin = avg_tmpMin or 0
        self.avg_tmpMax = avg_tmpMax or 0
        self.cumulated_rain = cumulated_rain or 0
        self.year = year or 0
        self.url = url or ''

    def displayMonth(self):
        print ('url : ', self.url)
        print('nombre de jours : ', len(self.days))
        print ('numero du mois : ', self.numeroMois)
        print ('annee du mois : ', self.year)
        for day in self.days:
            day.displayDay()