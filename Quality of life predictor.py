#Quality of life predictor
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import sklearn.linear_model


BLI = pd.read("BLI_02092023235650521.csv")
gdp_per_capita = pd.read_csv("gdp_per_capita.csv", delimiter = "\t", encoding='latin1', na_values = "n/a")
