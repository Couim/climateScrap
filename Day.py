#Day contains informations relative to a day
class Day : 
    def __init__(self, numeroJour=None, day=None, tempMin=None, tempMax=None, pluie=None, canonicForm=None, month=None) :
        self.numeroJour = numeroJour or 0
        self.tempMin = tempMin or 0
        self.tempMax = tempMax or 0
        self.day=day or '' #ex 31/01/2020
        self.canonicForm = canonicForm or ''
        self.month=month
        self.pluie = pluie or 0

    def displayDay(self):
        print(self.day, self.tempMin, ' ', self.tempMax)