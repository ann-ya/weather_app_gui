import requests


API_KEY = "aea7b1cdeec34d358df131021220807"


class Weather:

    def __init__(self, location:str="RG302XB"):
        self.weatherData = {}
        self.fetch(location)


    #---- Location ----

    def getLocationData(self, name):
        data = self.weatherData["location"][name]
        return str(data)


    def getCity(self):
        return self.getLocationData("name")


    def getCountry(self):
        return self.getLocationData("country")


    def getLocalTime(self):
        return self.getLocationData("localtime")


    def getTimeZone(self):
        return self.getLocationData("tz_id")


    def getLocation(self):
        return f"{self.getCity()}, {self.getCountry()}"


    #---- Current ----

    def getCurrentData(self, name):
        data = self.weatherData["current"][name]
        return data if name == "condition" else str(data)


    def getCurrentTempF(self):
        return self.getCurrentData("temp_f")+" \u00B0F"


    def getCurrentTempC(self):
        return self.getCurrentData("temp_c")+" \u00B0C"


    def getFeelsLikeF(self):
        return self.getCurrentData("feelslike_f")+" \u00B0F"


    def getFeelsLikeC(self):
        return self.getCurrentData("feelslike_c")+" \u00B0C"


    def getConditionText(self):
        condition = self.getCurrentData("condition")
        return str(condition["text"])


    def getConditionsIcon(self):
        pass


    def getPrecipitationMM(self):
        return self.getCurrentData("precip_mm")+" mm"


    def getHumidity(self):
        return self.getCurrentData("humidity")+"%"


    def getWindSpeedKPH(self):
        return self.getCurrentData("wind_kph")+" km/h"


    def getWindDirection(self):
        return self.getCurrentData("wind_dir")


    def getPressure(self):
        return self.getCurrentData("pressure_mb")+" hPa"


    def fetch(self, query):
        try:
            url = f"http://api.weatherapi.com/v1/current.json" + \
                f"?key={API_KEY}&q={query}&aqi=no"
            self.weatherData = requests.get(url).json()
        except:
            self.weatherData = {"error": []}