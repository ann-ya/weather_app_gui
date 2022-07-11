import tkinter
from tkinter.constants import *
from tkinter import StringVar, IntVar
from tkinter.ttk import *


class View(tkinter.Tk):

    def __init__(self, controller):
        super().__init__()
        self.geometry("700x500")

        self.controller = controller
        self.bind("<Return>", self.controller.handleButtonSearch)
        
        #---- Variables ----
        self.varSearch = StringVar()
        self.varLocation = StringVar()
        self.varLocalTime = StringVar()
        self.varTimeZone = StringVar()
        self.varTemp = StringVar()
        self.varFeelsLike = StringVar()
        self.varConditions = StringVar()
        self.varPrecipitation = StringVar()
        self.varHumidity = StringVar()
        self.varWindSpeed = StringVar()
        self.varWindDirection = StringVar()
        self.varPressure = StringVar()
        self.varUnits = IntVar()

        self.varTemp.set("28")
        self.varLocation.set("Seoul")

        #---- Frames ----
        self.mainframe = Frame(self)
        self.mainframe.pack()
        self._createFrameSearchBar()
        self._createFrameInfo()
        self._createFrameDetails()
        self._createFrameControls()


    def _createFrameSearchBar(self):
        self.frameSearchBar = Frame(self.mainframe)

        comboSearch = Combobox(self.frameSearchBar, textvariable=self.varSearch)
        buttonSearch = Button(self.frameSearchBar, text="Search", command=self.controller.handleButtonSearch)

        comboSearch.pack(padx=10, side=LEFT)
        buttonSearch.pack(side=RIGHT)
        self.frameSearchBar.pack()


    def _createFrameInfo(self):
        self.frameInfo = Frame(self.mainframe)

        labelLocation = Label(self.frameInfo, textvariable=self.varLocation)
        labelTemp =Label(self.frameInfo, textvariable=self.varTemp)
        labelIcon = Label(self.frameInfo, text='image')

        labelLocation.pack(pady=5)
        labelTemp.pack(pady=5)
        labelIcon.pack(pady=5)
        self.frameInfo.pack()


    def _createFrameDetails(self):
        self.frameDetails = Frame(self.mainframe)

        labelFeelsLikeLeft = Label(self.frameDetails, text="Feels like: ")
        labelConditionsLeft = Label(self.frameDetails, text="Current conditions:")
        labelHumidityLeft = Label(self.frameDetails, text="Humidity: ")
        labelPrecipitationLeft = Label(self.frameDetails, text="Precipitation: ")
        labelWindSpeedLeft = Label(self.frameDetails, text= "Wind speed: ")
        labelWindDirectionLeft =Label(self.frameDetails, text="Wind direction: ")
        labelPressureLeft = Label(self.frameDetails, text="Pressure: ")

        labelFeelsLikeRight = Label(self.frameDetails, textvariable=self.varFeelsLike)
        labelConditionsRight = Label(self.frameDetails, textvariable=self.varConditions)
        labelHumidityRight = Label(self.frameDetails, textvariable=self.varHumidity)
        labelPrecipitationRight = Label(self.frameDetails, textvariable=self.varPrecipitation)
        labelWindSpeedRight = Label(self.frameDetails, textvariable=self.varWindSpeed)
        labelWindDirectionRight = Label(self.frameDetails, textvariable=self.varWindDirection)
        labelPressureRight = Label(self.frameDetails, textvariable=self.varPressure)

        labelFeelsLikeLeft.grid(row=0, column=0, pady=8, sticky=W)
        labelFeelsLikeRight.grid(row=0,column=1, pady=8, sticky=E)
        labelConditionsLeft.grid(row=1, column=0, pady=8, sticky=W)
        labelConditionsRight.grid(row=1,column=1, pady=8, sticky=E)
        labelHumidityLeft.grid(row=2, column=0, pady=8, sticky=W)
        labelHumidityRight.grid(row=2,column=1, pady=8, sticky=E)
        labelPrecipitationLeft.grid(row=3, column=0, pady=8, sticky=W)
        labelPrecipitationRight.grid(row=3,column=1, pady=8, sticky=E)
        labelWindSpeedLeft.grid(row=4, column=0, pady=8, sticky=W)
        labelWindSpeedRight.grid(row=4,column=1, pady=8, sticky=E)
        labelWindDirectionLeft.grid(row=5, column=0, pady=8, sticky=W)
        labelWindDirectionRight.grid(row=5,column=1, pady=8, sticky=E)
        labelPressureLeft.grid(row=6, column=0, pady=8, sticky=W)
        labelPressureRight.grid(row=6,column=1, pady=8, sticky=E)
        self.frameDetails.pack()


    def _createFrameControls(self):
        self.frameControls = Frame(self.mainframe)

        radioFahrenheit = Radiobutton(self.frameControls, text="Fahrenheit", variable=self.varUnits, value=1, command=self.controller.updateGUI)
        radioCelsius = Radiobutton(self.frameControls, text="Celsius", variable=self.varUnits, value=2, command=self.controller.updateGUI)

        radioCelsius.invoke()

        radioFahrenheit.pack(side=LEFT, padx=7.5, pady=5)
        radioCelsius.pack(side=RIGHT, padx=7.5, pady=5)
        self.frameControls.pack()


    def main(self):
        self.mainloop()