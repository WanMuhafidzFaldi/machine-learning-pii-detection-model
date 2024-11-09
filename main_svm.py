from data_processing import dataProcessing
from data_set import loadDataTraining
from machine_learning import machineLearningSVM

filePathDataSet = 'dataset1.json'
dataSet = loadDataTraining(filePathDataSet)
print(f"Jumlah Data Set: {len(dataSet)}")

xTrain, xTest, yTrain, yTest, vectorizer = dataProcessing(dataSet)

modelSVM = machineLearningSVM(xTrain, xTest, yTrain, yTest)