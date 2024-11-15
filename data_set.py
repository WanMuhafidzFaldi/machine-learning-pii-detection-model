import json
import db_connection   

def loadDataTraining(filePath):
    if filePath != '':
        with open(filePath, 'r') as file:
            data = json.load(file)
        
        dataSet = []
        x = 0
        for entry in data:
            logs = entry.get('logs', {})
            keyValueLabels = logs.get('keyValueLabels', [])
            x += 1
            for kv in keyValueLabels:
                if len(kv) >= 3:
                    responseData = {kv[0]: kv[1]}
                    scoringData = kv[2]
                    dataSet.append({
                        'responseData': json.dumps(responseData),
                        'scoringData': scoringData
                    })
    else:
        data = db_connection.loadDataUji()

        dataSet = []
        x = 0
        for entry in data:
            keyValueLabels = entry.get('keyValueLabels', [])
            x += 1
            for kv in keyValueLabels:
                if len(kv) >= 3:
                    responseData = {kv[0]: kv[1]}
                    scoringData = kv[2]
                    dataSet.append({
                        'responseData': json.dumps(responseData),
                        'scoringData': scoringData
                    })
    
   
    print("Jumlah Data:", x)
    return dataSet
