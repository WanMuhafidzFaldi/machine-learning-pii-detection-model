from data_uji import loadDataTest
from predict_pii import predictPii
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, confusion_matrix
import joblib

# List untuk menyimpan hasil prediksi dan label sebenarnya
yTrue = []
yPred = []

# Load the trained model
# change the file name to model_naive_bayes.pkl if you want to use the Naive Bayes model
# Load the trained model
try:
    model = joblib.load('model_naive_bayes.pkl')
except FileNotFoundError:
    print("Error: The model file was not found. Please train the model first.")
    exit(1)

# Load the vectorizer
try:
    vectorizer = joblib.load('vectorizer.pkl')
except FileNotFoundError:
    print("Error: The vectorizer file was not found. Please train the model first.")
    exit(1)

filePathDataTest = 'datauji1.json'
dataTest = loadDataTest(filePathDataTest)
for data in dataTest:
    print("Data Uji: ", data['responseData'])
    print("Scoring Seharusnya: ", data['scoringData'])
    predict, textReport = predictPii(model, vectorizer, data['responseData'])  # Output: Does not contain PII
    print("Hasil Prediksi: ", predict)
    print("Text Report: ", textReport)
    print("\n")

    # Simpan hasil prediksi dan label sebenarnya
    yTrue.append(data['scoringData'])
    yPred.append(predict)

# Hitung metrik-metrik
totalData = len(dataTest)  
accuracy = accuracy_score(yTrue, yPred)
f1 = f1_score(yTrue, yPred, average='weighted')
precision = precision_score(yTrue, yPred, average='weighted')
recall = recall_score(yTrue, yPred, average='weighted')
conf_matrix = confusion_matrix(yTrue, yPred)

print(f"Jumlah Data Uji: {totalData}")
print(f"Akurasi: {accuracy}")
print(f"F1-score: {f1}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"Confusion Matrix: \n{conf_matrix}")