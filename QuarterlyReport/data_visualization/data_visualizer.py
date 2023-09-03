# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 19:16:20 2023

@author: mutali
"""

import numpy as np
import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, dfPr, x=10, y=4, font=14.3, dpisize=100):
        self.dfPr = dfPr
        self.x = x
        self.y = y
        self.font = font
        self.dpisize = dpisize

    def _save_plot(self, fig, figname):
        fig.savefig(figname, bbox_inches='tight', dpi=self.dpisize)
        plt.close(fig)

    def _create_bar_chart(self, x_values, female_values, male_values, x_labels, x_label, y_label, colors, legend_location):
        fig, ax = plt.subplots()
        x_axis = np.arange(len(x_values))
        
        ax.bar(x_axis - 0.2, female_values, width=0.4, label='Actual', color=colors[0])
        ax.bar(x_axis + 0.2, male_values, width=0.4, label='Forecast', color=colors[1])
        
        ax.set_xticks(x_axis)
        ax.set_xticklabels(x_values, rotation='vertical')
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        
        ax.legend(loc='upper left', bbox_to_anchor=legend_location, ncol=2)
        ax.grid(axis='y')
        
        plt.rcParams.update({'font.size': self.font})
        plt.rcParams["figure.figsize"] = (self.x, self.y)
        #plt.show()
        
        return fig

    def revenue(self):
        
        actual_columns = ['MID_Total_(ZAR)', 'HIG_Total_(ZAR)', 'VER_Total_(ZAR)', 'DUR_Total_(ZAR)', 'HER_Total_(ZAR)', 'TZA_Total_(ZAR)']
        forecast_columns = ['Forecast_MID_Total_ZAR', 'Forecast_HIG_Total_ZAR', 'Forecast_VER_Total_ZAR', 'Forecast_DUR_Total_ZAR', 'Forecast_HER_Total_ZAR', 'Forecast_TZA_Total_ZAR']
        team = ['Midstream', 'Highveld', 'Vergelegen', 'Durbanville', 'Hermanus', 'Tzaneen']
        colors = ['#5F0505', '#D9D9D9']
        legend_location = (0.50, 1.18)
        
        female = self.dfPr[actual_columns].sum()
        male = self.dfPr[forecast_columns].sum()
        
        fig = self._create_bar_chart(team, female, male, team, "Plants", "Revenue ZAR", colors, legend_location)
        figname = 'Revenue.jpg'
        self._save_plot(fig, figname)
        
        return figname

    def irradiation(self, name, actual, forecast):
        team = self.dfPr['Date']
        colors = ['#5F0505', '#D9D9D9']
        legend_location = (0.53, 1.18)

        female = self.dfPr[actual]
        male = self.dfPr[forecast]
        
        fig = self._create_bar_chart(team, female, male, team, "Month", "Irradiation kWh/m²", colors, legend_location)
        figname = f'Mediclinic {name} Irradiation.jpg'
        self._save_plot(fig, figname)
        return figname

    def availability(self, name, actual, forecast):
        team = self.dfPr['Date']
        colors = ['#5F0505', '#D9D9D9']
        legend_location = (0.58, 1.18)

        female = self.dfPr[actual]
        male = self.dfPr[forecast]

        fig = self._create_bar_chart(team, female, male, team, "Month", "Availability %", colors, legend_location)
        figname = f'Mediclinic {name} Availability.jpg'
        self._save_plot(fig, figname)
        return figname

    def PR(self, name, actual, forecast):
        team = self.dfPr['Date']
        colors = ['#5F0505', '#D9D9D9']
        legend_location = (0.4, 1.18)

        female = self.dfPr[actual]
        male = self.dfPr[forecast]

        fig = self._create_bar_chart(team, female, male, team, "Month", "Performance Ratio %", colors, legend_location)
        figname = f'Mediclinic {name} Perfomance Ratio.jpg'
        self._save_plot(fig, figname)
        return figname

    def production(self, name, actual, forecast, weather):
        team = self.dfPr['Date']
        colors = ['#5F0505', '#D9D9D9', '#FFC000']
        legend_location = (-0.02, 1.18)

        female = self.dfPr[actual]
        male = self.dfPr[forecast]
        weather_values = self.dfPr[weather]

        fig = self._create_bar_chart(team, female, male, team, "Month", "Production kWh", colors, legend_location)
        ax = fig.gca()
        ax.bar(team, weather_values, width=0.25, label='Weather Adjusted Predicted kWh', color=colors[2])
        ax.legend(loc='upper left')
        
        figname = f'Mediclinic {name} Production.jpg'
        self._save_plot(fig, figname)
        return figname

    def irradiation_Availability(self, name, actual_irradiation, forecast_irradiation, actual_availability, forecast_availability):
        team = self.dfPr['Date']
        colors = ['#5F0505', '#D9D9D9']
        legend_location = (0.63, 1.02)

        female_irradiation = self.dfPr[actual_irradiation]
        male_irradiation = self.dfPr[forecast_irradiation]
        female_availability = self.dfPr[actual_availability]
        male_availability = self.dfPr[forecast_availability]

        fig, ax1 = plt.subplots()
        ax1.set_xlabel('Month')
        ax1.set_ylabel('Irradiation kWh/m²')
        ax1.bar(team - 0.2, female_irradiation, width=0.4, label='Actual Irradiation kWh/m²', color=colors[0])
        ax1.tick_params(axis='y')
        ax1.set_xticklabels(team, rotation=90)
        ax1.tick_params(axis="x", direction="in", pad=4)

        ax2 = ax1.twinx()
        ax2.set_ylabel('Availability %')
        ax2.bar(team + 0.2, male_availability, width=0.4, label='Actual Availability %', color=colors[1])
        ax2.tick_params(axis='y')

        fig.legend(bbox_to_anchor=legend_location, ncol=2)
        plt.grid(axis='y')
        plt.rcParams.update({'font.size': self.font})
        plt.rcParams["figure.figsize"] = (self.x, self.y)
        
        figname = f'Mediclinic {name} Availability_Irradiation.jpg'
        self._save_plot(fig, figname)
        
        return figname
