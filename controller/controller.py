from view.view import View
from model.weather import Weather


class Controller:

    def __init__(self) -> None:
        self.view = View(self)
        self.weather = Weather()

        self.updateGUI()


    def main(self):
        self.view.main()


    def updateGUI(self):
        if "error" not in self.weather.weatherData:
            self.view.varLocation.set(self.weather.getLocation())
            self.view.varLocalTime.set(self.weather.getLocalTime())
            self.view.varConditionText.set(self.weather.getConditionText())
            self.view.varPrecipitation.set(self.weather.getPrecipitationMM())
            self.view.varHumidity.set(self.weather.getHumidity())
            self.view.varWind.set(self.weather.getWind())
            self.view.varPressure.set(self.weather.getPressure())

            if self.view.varUnits.get() == 1:
                self.view.varTemp.set(self.weather.getCurrentTempF())
                self.view.varFeelsLike.set(self.weather.getFeelsLikeF())
            else:
                self.view.varTemp.set(self.weather.getCurrentTempC())
                self.view.varFeelsLike.set(self.weather.getFeelsLikeC())



    def handleButtonSearch(self, event=None):
        location = self.view.varSearch.get()
        if location != "":
            self.weather = Weather(location)
            self.updateGUI()


    def handleComboLocation():
        pass