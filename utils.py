import sys
import pandas as pd
import matplotlib.pyplot as plt

#Create a function called loadAndCleanData that takes as an argument a filename
#and returns a Pandas dataframe.

def loadAndCleanData (filename):
    filename = pd.read_csv(filename)
    newData = filename.fillna("0")
    print (newData)
    return newData

def computePDF(target_feature, DataFrame):
    dataframe = DataFrame[target_feature].plot.kde()
    plt.show(dataframe)

def viewDistribution(target_feature, dataframe):
    dist = dataframe.hist(column=target_feature, log=True)
    plt.show(dist)

def viewLogDistribution(target_feature, dataframe):
    log_dist = dataframe.hist(column=target_feature, log=True)
    plt.show(log_dist)

def computeProbability(target_feature, bin, dataframe):
#Count the number of datapoints in the bin
    count = 0.0

    for i,datapoint in dataframe.interrows():
        #see if the data is in the right bin
        if datapoint[target_feature] >= bin[0] and datapoint[target_feature] < bin[1]:
            count += 1

#Count the total number of datasets
    totalData = len(dataframe)

 # Divide the number of people in the bun by the total number of people
    probability = count / totalData

 # return the result
    return (probability)
# This data could be used to determine risk information on someone should be accepted for a loan
def computeDefaultRisk(column, target_feature, bin, dataframe):
    count = 0.0
    counts = 0.0
    for i,datapoint in dataframe.interrows():
        if datapoint [target_feature] >= bin[0] and datapoint[target_feature]<bin[1]:
            count += 1
            if datapoint[column]==1:
                counts=1
    totalData = len(dataframe)
    probability = count/totalData
    probability_two = counts/totalData
    print(probability_two/probability)
    return (probability_two/probability)


#def predictDefaultRisk(target_feature, ):
#for g in range(len(rate)):
#   rate[g] = rate[g] * amount[g] / sum(amount)
#rate = sum(rate)


# Using DataFrame.insert() to add a column
newloans_data_df = loadAndCleanData("newLoans.csv")
df = pd.DataFrame(newloans_data_df)
df.insert(2, "AbsoluteRating", "DistributedRating", True)
df.insert(3, "DistributedRating", True)


#def rateLoanDistribution(group, weight, data):
