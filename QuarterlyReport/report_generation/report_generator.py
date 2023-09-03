# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 19:19:40 2023

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

filtered_df=0
class MonthlyReportGenerator:
    def __init__(self, excel_file, sheet_name='Data'):
        self.excel_file = excel_file
        self.sheet_name = sheet_name

    def read_data(self):
        self.df = pd.read_excel(self.excel_file, sheet_name=self.sheet_name)

    def configure_plot(self):
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = 'Arial Narrow'

    def generate_plots(self):
        # Your code to generate and show plots goes here
        # For example: plt.plot(self.df['Date'], self.df['Value'])
        plt.show()

    def filter_data(self, date_start, date_end):
        self.df = self.df[(self.df['Date'] >= date_start) & (self.df['Date'] <= date_end)]

    def format_dates(self):
        self.df['Date'] = self.df['Date'].dt.strftime('%b %y')

    def generate_report(self):
        self.read_data()
        self.configure_plot()
        self.generate_plots()
        self.filter_data(date_start='2023-04-01', date_end='2023-06-01')
        self.format_dates()
        return self.df  # Return the filtered and formatted DataFrame

if __name__ == "__main__":
    report_generator = MonthlyReportGenerator(excel_file='Monthly report.xlsm')
    filtered_df = report_generator.generate_report()
    