from data_processing import dataProcessing
from data_set import loadDataTraining
from machine_learning import machineLearningSVM

# Load the training data with filePathDataSet
# filePathDataSet = 'dataset1.json' optional
# dataSet = loadDataTraining(filePathDataSet)

# Load the training data with database connection
dataSet = loadDataTraining('')
print(f"Jumlah Data Set Flatten: {len(dataSet)}")

xTrain, xTest, yTrain, yTest, vectorizer = dataProcessing(dataSet)

modelSVM = machineLearningSVM(xTrain, xTest, yTrain, yTest)