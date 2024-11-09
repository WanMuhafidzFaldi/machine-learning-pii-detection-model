import json

def loadDataTraining(filePath):
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
    print("Jumlah DataSet:", x)
    return dataSet
