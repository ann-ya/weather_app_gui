import tkinter
from tkinter.constants import *
from tkinter import PhotoImage, StringVar, IntVar
from tkinter.ttk import *
from tkinter import font


class View(tkinter.Tk):

    def __init__(self, controller):
        super().__init__()
        self.geometry("600x550")

        self.controller = controller
        self.bind("<Return>", self.controller.handleButtonSearch)
        
        #---- Variables ----
        self.varSearch = StringVar()
        self.varLocation = StringVar()
        self.varLocalTime = StringVar()
        self.varTemp = StringVar()
        self.varFeelsLike = StringVar()
        self.varConditionText = StringVar()
        self.varPrecipitation = StringVar()
        self.varHumidity = StringVar()
        self.varWind = StringVar()
        self.varPressure = StringVar()
        self.varUnits = IntVar()

        self.varTemp.set("28")
        self.varLocation.set("Seoul")

        #---- Frames ----
        self.mainframe = Frame(self, width= 600, height=600)
        self.mainframe.pack()
        self._createFrameSearchBar()
        self._createFrameInfo()
        self._createFrameDetails()
        self._createFrameControls()

        
    def _createFrameSearchBar(self):
        self.frameSearchBar = Frame(self.mainframe)

        helv13 = font.Font(family="Velveteen", size=13)

        entry = Entry(self.frameSearchBar, textvariable=self.varSearch, font=helv13)
        entry.place(relwidth=0.65, relheight=1)
        # comboSearch = Combobox(self.frameSearchBar, textvariable=self.varSearch, font=helv13)
        buttonSearch = Button(self.frameSearchBar, text="Search", command=self.controller.handleButtonSearch)

        entry.pack(padx=10, pady=20, side=LEFT)
        # comboSearch.pack(padx=10, pady=20, side=LEFT)
        buttonSearch.pack(side=RIGHT)
        self.frameSearchBar.pack()


    def _createFrameInfo(self):
        self.frameInfo = Frame(self.mainframe)
    
        loc_font = font.Font(family="Velveteen", size=21)
        temp_font = font.Font(family="Velveteen", size=22)
        time_font = font.Font(family="Velveteen", size=20)

        labelLocation = Label(self.frameInfo, textvariable=self.varLocation, font=loc_font, width=25, anchor=CENTER)
        labelTemp = Label(self.frameInfo, textvariable=self.varTemp, font=temp_font, width=25, anchor=CENTER)
        labelLocalTime = Label(self.frameInfo, textvariable=self.varLocalTime, font=time_font, width=25, anchor=CENTER)
        
    
        labelLocation.pack(pady=8)
        labelTemp.pack(pady=5, side=RIGHT)
        labelLocalTime.pack(pady=5, side=LEFT)
        self.frameInfo.pack(pady=20)


    def _createFrameDetails(self):
        self.frameDetails = Frame(self.mainframe)

        d_font = font.Font(family="Velveteen", size=15)

        labelFeelsLikeLeft = Label(self.frameDetails, text="Feels like", font=d_font, width=20)
        labelConditionsLeft = Label(self.frameDetails, text="Conditions", font=d_font, width=20)
        labelHumidityLeft = Label(self.frameDetails, text="Humidity", font=d_font, width=20)
        labelPrecipitationLeft = Label(self.frameDetails, text="Precipitation", font=d_font, width=20)
        labelWindLeft = Label(self.frameDetails, text="Wind", font=d_font, width=20)
        labelPressureLeft = Label(self.frameDetails, text="Pressure", font=d_font, width=20)

        labelFeelsLikeRight = Label(self.frameDetails, textvariable=self.varFeelsLike, font=d_font)
        labelConditionsRight = Label(self.frameDetails, textvariable=self.varConditionText, font=d_font)
        labelHumidityRight = Label(self.frameDetails, textvariable=self.varHumidity, font=d_font)
        labelPrecipitationRight = Label(self.frameDetails, textvariable=self.varPrecipitation, font=d_font)
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
        labelWindLeft.grid(row=4, column=0, pady=8, sticky=W)
        labelWindRight.grid(row=4,column=1, pady=8,sticky=W)
        labelPressureLeft.grid(row=5, column=0, pady=8, sticky=W)
        labelPressureRight.grid(row=5, column=1, pady=8,sticky=W)
        self.frameDetails.pack(pady=20)


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