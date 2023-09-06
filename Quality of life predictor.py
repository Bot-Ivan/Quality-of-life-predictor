#Quality of life predictor
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import sklearn.linear_model
import os

def prepare_country_stats(LSF, GPCF): #Life Satisfaction File, GDP Per Capita File
    LSF = LSF[LSF["INEQUALITY"]=="TOT"]
    LSF = LSF[LSF["Indicator"] == "Life satisfaction"]
    LSF = LSF.pivot(index = "Country", columns = "Indicator", values = "Value")
    print(LSF)

    

BLI = pd.read_csv("BLI.csv")
gdp_per_capita = pd.read_csv("gdp_per_capita.csv", delimiter = "\t")
prepare_country_stats(BLI, gdp_per_capita)
