import tkinter
from tkinter.constants import *
from tkinter import StringVar, IntVar
from tkinter.ttk import *
from tkinter import font


class View(tkinter.Tk):

    def __init__(self, controller):
        super().__init__()
        self.geometry("500x500")

        self.controller = controller
        self.bind("<Return>", self.controller.handleButtonSearch)
        
        #---- Variables ----
        self.varSearch = StringVar()
        self.varLocation = StringVar()
        self.varLocalTime = StringVar()
        self.varTimeZone = StringVar()
        self.varTemp = StringVar()
        self.varFeelsLike = StringVar()
        self.varConditionText = StringVar()
        # self.varConditionIcon = StringVar()
        self.varPrecipitation = StringVar()
        self.varHumidity = StringVar()
        # self.varWindSpeed = StringVar()
        # self.varWindDirection = StringVar()
        self.varWind = StringVar()
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

        helv13 = font.Font(family="Velveteen", size=13)

        comboSearch = Combobox(self.frameSearchBar, textvariable=self.varSearch, font=helv13)
        buttonSearch = Button(self.frameSearchBar, text="Search", command=self.controller.handleButtonSearch)

        comboSearch.pack(padx=10, pady=20, side=LEFT)
        buttonSearch.pack(side=RIGHT)
        self.frameSearchBar.pack()


    def _createFrameInfo(self):
        self.frameInfo = Frame(self.mainframe)

        info_font = font.Font(family="Velveteen", size=17)

        labelLocation = Label(self.frameInfo, textvariable=self.varLocation, font=info_font)
        labelTemp =Label(self.frameInfo, textvariable=self.varTemp, font=info_font)
        # labelIcon = Label(self.frameInfo, textvariable=self.varConditionIcon)

        labelLocation.pack(pady=10)
        labelTemp.pack(pady=5)
        # labelIcon.pack(pady=5)
        self.frameInfo.pack()


    def _createFrameDetails(self):
        self.frameDetails = Frame(self.mainframe)

        # self.frameDetails.columnconfigure(2, weight=3)
        d_font = font.Font(family="Velveteen", size=14)

        labelFeelsLikeLeft = Label(self.frameDetails, text="Feels like", font=d_font, width=20)
        labelConditionsLeft = Label(self.frameDetails, text="Conditions", font=d_font, width=20)
        labelHumidityLeft = Label(self.frameDetails, text="Humidity", font=d_font, width=20)
        labelPrecipitationLeft = Label(self.frameDetails, text="Precipitation", font=d_font, width=20)
        # labelWindSpeedLeft = Label(self.frameDetails, text= "Wind speed")
        # labelWindDirectionLeft =Label(self.frameDetails, text="Wind direction")
        labelWindLeft = Label(self.frameDetails, text="Wind", font=d_font, width=20)
        labelPressureLeft = Label(self.frameDetails, text="Pressure", font=d_font, width=20)

        labelFeelsLikeRight = Label(self.frameDetails, textvariable=self.varFeelsLike, font=d_font)
        labelConditionsRight = Label(self.frameDetails, textvariable=self.varConditionText, font=d_font)
        labelHumidityRight = Label(self.frameDetails, textvariable=self.varHumidity, font=d_font)
        labelPrecipitationRight = Label(self.frameDetails, textvariable=self.varPrecipitation, font=d_font)
        # labelWindSpeedRight = Label(self.frameDetails, textvariable=self.varWindSpeed)
        # labelWindDirectionRight = Label(self.frameDetails, textvariable=self.varWindDirection)
        labelWindRight = Label(self.frameDetails, textvariable=self.varWind, font=d_font)
        labelPressureRight = Label(self.frameDetails, textvariable=self.varPressure, font=d_font)

        labelFeelsLikeLeft.grid(row=0, column=0, pady=8, sticky=W)
        labelFeelsLikeRight.grid(row=0,column=1, pady=8, sticky=W)
        labelConditionsLeft.grid(row=1, column=0, pady=8, sticky=W)
        labelConditionsRight.grid(row=1,column=1, pady=8,sticky=W)
        labelHumidityLeft.grid(row=2, column=0, pady=8, sticky=W)
        labelHumidityRight.grid(row=2,column=1, pady=8,sticky=W)
        labelPrecipitationLeft.grid(row=3, column=0, pady=8, sticky=W)
        labelPrecipitationRight.grid(row=3,column=1, pady=8,sticky=W)
        # labelWindSpeedLeft.grid(row=4, column=0, pady=8, sticky=W)
        # labelWindSpeedRight.grid(row=4,column=1, pady=8, sticky=E)
        # labelWindDirectionLeft.grid(row=5, column=0, pady=8, sticky=W)
        # labelWindDirectionRight.grid(row=5,column=1, pady=8, sticky=E)
        labelWindLeft.grid(row=4, column=0, pady=8, sticky=W)
        labelWindRight.grid(row=4,column=1, pady=8,sticky=W)
        labelPressureLeft.grid(row=5, column=0, pady=8, sticky=W)
        labelPressureRight.grid(row=5, column=1, pady=8,sticky=W)
        self.frameDetails.pack(pady=15)


    def _createFrameControls(self):
        self.frameControls = Frame(self.mainframe)

        rb_font = font.Font(family="Velveteen", size=13)

        radioFahrenheit = Radiobutton(self.frameControls, text="Fahrenheit", variable=self.varUnits, value=1, command=self.controller.updateGUI)
        radioCelsius = Radiobutton(self.frameControls, text="Celsius", variable=self.varUnits, value=2, command=self.controller.updateGUI)

        radioCelsius.invoke()

        radioFahrenheit.pack(side=LEFT, padx=7.5, pady=25)
        radioCelsius.pack(side=RIGHT, padx=7.5, pady=25)
        self.frameControls.pack()


    def main(self):
        self.mainloop()