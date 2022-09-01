
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 18:49:40 2022

@author: mutali
"""

import win32com.client as win32
from win32com.client import Dispatch
import os
import os, sys  # Standard Python Libraries
import xlwings as xw  # pip install xlwings
from docxtpl import DocxTemplate  # pip install docxtpl
import pandas as pd  # pip install pandas
import matplotlib.pyplot as plt  # pip install matplotlib
import win32com.client as win32  # pip install pywin32



xlApp = Dispatch('Excel.Application')
workbook = xlApp.Workbooks.Open("Moshesh Perfomance.xlsm")
xlApp.Sheets("Generation").Select()
xlSheet1 = xlApp.Sheets(1)
#WARNING: The following line will cause the script to discard any unsaved changes in your workbook
#Ensure to save any work before running scrip
xlApp.DisplayAlerts = False
i = 0
for chart in xlSheet1.ChartObjects():
    print(chart.Name)
    chart.CopyPicture()
    #Create new temporary sheet
xlApp.ActiveWorkbook.Sheets.Add(After=xlApp.ActiveWorkbook.Sheets(3)).Name="temp_sheet" + str(i)
temp_sheet = xlApp.ActiveSheet
#Add chart object to new sheet.
cht = xlApp.ActiveSheet.ChartObjects().Add(0,0,800, 600)
#Paste copied chart into new object
cht.Chart.Paste()
#Export image
cht.Chart.Export("chart" + str(i) + ".png")

#This line is not entirely neccessary since script currently exits without saving
temp_sheet.Delete()
i = i+1
xlApp.ActiveWorkbook.Close()
#Restore default behaviour
xlApp.DisplayAlerts = True