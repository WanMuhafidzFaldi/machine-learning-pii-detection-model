from data_processing import dataProcessing
from data_set import loadDataTraining
from machine_learning import machineLearningNaiveBayes

filePathDataSet = 'dataset1.json'
dataSet = loadDataTraining(filePathDataSet)
print(f"Jumlah Data Set: {len(dataSet)}")

xTrain, xTest, yTrain, yTest, vectorizer = dataProcessing(dataSet)

modelNaiveBayes = machineLearningNaiveBayes(xTrain, xTest, yTrain, yTest)
