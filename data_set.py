import json
import db_connection   

def loadDataTraining():
    scoreData = [0, 1, 2]
    dataLogs = []
    dataSet = []
    for score in scoreData:
        dataLogs.append(db_connection.dataUjiScore(score))
        print(f"Jumlah Data From DB Score {score}: {len(dataLogs[-1])}")
        limitDataSet = min([len(data) for data in dataLogs])
    print("Max Count Data Set:", limitDataSet)
    for score in scoreData:
        dataProcess = dataLogs[score][:limitDataSet]
        print (f"Data Score {score}: {len(dataProcess)}")
        for dp in dataProcess:
            keyValueLabels = dp.get('keyValueLabels', [])
            responseData = {keyValueLabels[0]: keyValueLabels[1]}
            scoringData = keyValueLabels[2]
            dataSet.append({
                'responseData': json.dumps(responseData),
                'scoringData': scoringData
            })

    return dataSet
