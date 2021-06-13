class ListOfVisitors:
    def __init__ (self,name,city,status):
        self.name = name
        self.city = city
        self.status = status
    def getName(self):
        return self.name
    def getCity(self):
        return self.city
    def getStatus(self):
        return self.status
    def visitors_dates(self):
        return self.name + ", " + self.city + ", " + self.status


