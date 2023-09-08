#Quality of life predictor
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import sklearn.linear_model
import os

def prepare_country_stats(LSF, GPCF): #Life Satisfaction File, GDP Per Capita File
    LSF = LSF[LSF["Indicator"] == "Life satisfaction"]
    LSF = LSF[LSF["Type of indicator"] == "Average"]
    LSF = LSF[LSF["TIME"] == 2013]
    LSF = LSF.pivot(index = "Country", columns = "Indicator", values = "Value")
    print(LSF)

    GPCF.rename(columns = {"2013": "GDP per capita"}, inplace = True)
    GPCF.set_index("Country", inplace = True)

    columns_to_remove = [str(year) for year in range(1990, 2020) if year != 2013]
    columns_to_remove.append("Country Code")

    GPCF.drop(columns = columns_to_remove, inplace = True)
    full_country_stats = pd.merge(left = LSF, right = GPCF, left_index = True, right_index = True)
    print(full_country_stats)

BLI = pd.read_csv("BLI.csv")
gdp_per_capita = pd.read_csv("gdp_per_capita.csv")
prepare_country_stats(BLI, gdp_per_capita)
