from sklearn.svm import LinearSVC  
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report 
import joblib

def machineLearningSVM(xTrain, xTest, yTrain, yTest):
    # 5. Melatih Model SVM  
    model = LinearSVC()
    model.fit(xTrain, yTrain)

    # 6. Prediksi dan Evaluasi  
    yPred = model.predict(xTest)  
    print(classification_report(yTest, yPred, zero_division=0))  

    
    joblib.dump(model, 'model_svm.pkl')
    return model

def machineLearningNaiveBayes(xTrain, xTest, yTrain, yTest):
    # 5. Melatih Model Naive Bayes  
    model = MultinomialNB(alpha=0.01)
    model.fit(xTrain, yTrain)

    # 6. Prediksi dan Evaluasi  
    yPred = model.predict(xTest)  
    print(classification_report(yTest, yPred, zero_division=0))  

    
    joblib.dump(model, 'model_naive_bayes.pkl')
    return model