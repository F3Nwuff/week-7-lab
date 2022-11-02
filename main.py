class temp:
    def __init__(self,celcius=0):
        self.__celcius = celcius
    def setcel(self,celcius):
        cel = str(round((self.__celcius), 2))
        return cel
    def setfah(self,celcius):
        fah = str(round(((self.__celcius * 1.8) + 32), 2))
        return fah
    def setkel(self,celcius):
        kel = str(round((self.__celcius + 273.15), 2))
        return kel
    def settemp(self,celcius):
        if celcius > 273.15:
            self.__celsius = celcius
        else:
            print("it is over 273.15")
    def tocel(self):
        return "celcius:"+self.setcel(self)
    def tofah(self):
        return "fahrenheit:"+self.setfah(self)
    def tokel(self):
        return "kelvin:"+self.setkel(self)
    def __str__(self):
        return "celcius:"+self.setcel(self)+"\nfahrenheit:"+self.setfah(self)+"\nkelvin:"+self.setkel(self)

