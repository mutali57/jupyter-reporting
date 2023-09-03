# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 19:24:23 2023

@author: mutali
"""
import pandas as pd
import matplotlib.pyplot as plt
from docx.shared import Cm
from datetime import datetime
import datetime
import numpy as np
import os
from docxtpl import DocxTemplate, InlineImage
from QuarterlyReport.data_visualization.data_visualizer import DataVisualizer
from QuarterlyReport.report_generation.report_generator import MonthlyReportGenerator

def docRender():
    plant_names = ['HIG', 'VER', 'MID', 'DUR', 'TZA', 'HER']  # Add other plant names here
    combined_context = generate_combined_context(plant_names, filtered_df)

    template.render(combined_context)
    template.save('Combined_Automated_report.docx')
    print('Combined report generated')
    os.startfile('Combined_Automated_report.docx')

def generate_combined_context(plant_names, df):
    combined_context = {}

    for plant_name in plant_names:
        plant_context = plant(plant_name, df, plant_name)
        combined_context.update(plant_context)

    return combined_context


def figureImage(template,figName, measure):
    
     #Import saved figure
    image = InlineImage(template,figName,Cm(measure))
    #Declare template variables
    return image 

def docTable(dfPr, name, actual, forecast):
   
    table = []
    for i in range(0, len(dfPr['Date'].tolist())):
        try:
            var = round(((dfPr[actual].tolist()[i]-dfPr[forecast].tolist()[i])/dfPr[forecast].tolist()[i])*100, 2)
        except ZeroDivisionError:
            var=0 
        table.append({'Date':dfPr['Date'].tolist()[i],
         name+'A':int(round(dfPr[actual].tolist()[i],0)),
         name+'F':int(round(dfPr[forecast].tolist()[i],0)),
         name+'V':var
            
        })
    return table

def docTableProd(dfPr, name, actual, forecast,weather):
   
    table = []
    for i in range(0, len(dfPr['Date'].tolist())):
        try:
            var = round(((dfPr[actual].tolist()[i]-dfPr[forecast].tolist()[i])/dfPr[forecast].tolist()[i])*100, 2)
            varW = round(((dfPr[actual].tolist()[i]-dfPr[weather].tolist()[i])/dfPr[weather].tolist()[i])*100, 2)
        
        except ZeroDivisionError:
            var=0
            varW=0
        table.append({'Date':dfPr['Date'].tolist()[i],
         name+'A':int(round(dfPr[actual].tolist()[i],0)),
         name+'F':int(round(dfPr[forecast].tolist()[i],0)),
         name+'W':int(round(dfPr[weather].tolist()[i],0)),           
         name+'V':var,
         name+'WV':varW
                      
            
        })
    return table
        
def variance(dfPr,actual, forecast):
    try:
            var =  round(((dfPr[actual].iloc[-1]-dfPr[forecast].iloc[-1])/dfPr[forecast].iloc[-1])*100, 2)
            
    except ZeroDivisionError:
            var=0 
    return var
def var_sum(dfPr,actual, forecast):
    try:
            var =  round(((dfPr[actual].sum()-dfPr[forecast].sum())/dfPr[forecast].sum())*100, 2)
            
    except ZeroDivisionError:
            var=0 
    return var
def var_mean(dfPr,actual, forecast):
    try:
            var =  round(((dfPr[actual].mean()-dfPr[forecast].mean())/dfPr[forecast].mean())*100, 2)
            
    except ZeroDivisionError:
            var=0 
    return var
template = DocxTemplate('Template.Docx') 

def plant(name, df, plantName):
    m=16
    n=16
    dd=0
    x,y=(10,4)
    today = datetime.date.today()
    first = today.replace(day=1)
    last_month = first - datetime.timedelta(days=1)
    context= {
        
       name+'ZARLT':round(df[name+'_Total_(ZAR)'].iloc[-1],2),
       name+'ZARVLT':variance(df,name+'_Total_(ZAR)','Forecast'+'_'+name+'_'+'Total_ZAR'),
       name+'ZARTOT': int(round(df[name+'_Total_(ZAR)'].sum())),
       name+'ZARFOR': int(round(df['Forecast'+'_'+name+'_'+'Total_ZAR'].sum())),
       name+'ZARV':var_sum(df,name+'_Total_(ZAR)','Forecast'+'_'+name+'_'+'Total_ZAR'),
       name+'PATOT':int(round(df[name+'_Energy_(kWh)'].sum(),dd)),
       name+'PFTOT':int(round(df[name+'_P50_(kWh)'].sum(),dd)),
       name+'PWTOT':int(round(df[name+'_W_kWh'].sum(),dd)),
       name+'PVTOT':var_sum(df,name+'_Energy_(kWh)',name+'_P50_(kWh)'),
       name+'PWVTOT':var_sum(df,name+'_Energy_(kWh)',name+'_W_kWh'),
       name+'PATOT':int(round(df[name+'_Energy_(kWh)'].sum(),dd)),
       name+'P':int(round(df[name+'_Energy_(kWh)'].iloc[-1],dd)),
       
       name+'I':int(round(df[name+'_Irradiated_(kWh/m²)'].iloc[-1],dd)),
       name+'IATOT':int(round(df[name+'_Irradiated_(kWh/m²)'].sum(),dd)),
       name+'IFTOT':int(round(df[name+'_estimatedPOA'].sum(),dd)),
       name+'IVTOT':var_mean(df,name+'_Irradiated_(kWh/m²)',name+'_estimatedPOA'),
        
       name+'PR':int(round(df[name+'_PR_(%)'].iloc[-1],dd)),
       name+'PRAAVR':int(round(df[name+'_PR_(%)'].mean(),dd)),
       name+'PRFAVR':int(round(df[name+'_PRP50'].mean(),dd)),
       name+'PRVAVR':var_mean(df,name+'_PR_(%)',name+'_PRP50'),
        
       name+'A':int(round(df[name+'_Availability_(%)'].iloc[-1],2)),
       name+'AAAVR':int(round(df[name+'_Availability_(%)'].mean(),dd)),
       name+'AFAVR':int(round(df[name+'_Availability'].mean(),dd)),
       name+'AVAVR':var_mean(df,name+'_Availability_(%)',name+'_Availability'), 
        
        
       name+'PV':variance(df,name+'_Energy_(kWh)',name+'_P50_(kWh)'),
       name+'IV':variance(df,name+'_Irradiated_(kWh/m²)',name+'_estimatedPOA'),
       name+'AV':variance(df,name+'_Availability_(%)',name+'_Availability'),
       name+'PRV':variance(df,name+'_PR_(%)',name+'_PRP50'),
        'title': 'Automated Report',
        'day': datetime.datetime.now().strftime('%d'),
        
        'month':last_month.strftime("%B"),
        'year':last_month.strftime('%Y'),
       name+'Ptable_contents': docTableProd(df,name+'P',name+'_Energy_(kWh)',name+'_P50_(kWh)',name+'_W_kWh'),
       name+'Itable_contents': docTable(df,name+'I',name+'_Irradiated_(kWh/m²)',name+'_estimatedPOA'),
       name+'PRtable_contents': docTable(df,name+'PR',name+'_PR_(%)',name+'_PRP50'),
       name+'Atable_contents': docTable(df,name+'A',name+'_Availability_(%)',name+'_Availability'),
       name+'PImage':figureImage(template,data_visualizer.production(plantName,name+'_Energy_(kWh)',name+'_P50_(kWh)',name+'_W_kWh'),m),
       name+'IImage':figureImage(template,data_visualizer.irradiation(plantName,name+'_Irradiated_(kWh/m²)',name+'_estimatedPOA'),n),
       name+'AImage':figureImage(template,data_visualizer.availability(plantName,name+'_Availability_(%)',name+'_Availability'),n),
       name+'PRImage':figureImage(template,data_visualizer.PR(plantName,name+'_PR_(%)',name+'_PRP50'),n),
       
}
    return context

# Main script
if __name__ == "__main__":
    report_generator = MonthlyReportGenerator(excel_file='Monthly report.xlsm')
    filtered_df = report_generator.generate_report()
    print(filtered_df)
    data_visualizer = DataVisualizer(filtered_df)
    data_visualizer.revenue()

    docRender()
