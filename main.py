from utils import *
import pandas as pd
import matplotlib.pyplot as plt

#helloWorld() Load and clean the data
data_df = loadAndCleanData("creditData.csv")
data_pdf = computePDF("age", data_df)
data_dist = viewDistribution("age", data_df)
data_logdist = viewLogDistribution("age", data_df)
data_defaultrisk = computeDefaultRisk("creditData.csv")
print (computeProbability("age", [0,40], data_df))
print (computeDefaultRisk("SeriousDlqin2yrs", "age", [0, 40], data_df))
newloans_data_df = loadAndCleanData("newLoans.csv")
df.info()
