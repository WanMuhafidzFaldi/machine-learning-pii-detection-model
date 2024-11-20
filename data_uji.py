import json

def loadDataTest(filePath):
    with open(filePath, 'r') as file:
        data = json.load(file)
  
    dataTest = []
    for entry in data:
        logs = entry.get('logs', {})
        responseData = logs.get('data', {})
        keyValueLabels = logs.get('keyValueLabels', [])
  
        maxScoringData = max((kv[2] for kv in keyValueLabels if len(kv) > 2), default=None)
  
        # Ubah responseData menjadi string JSON
        if isinstance(responseData, (list, dict)):
          responseData = json.dumps(responseData)
  
        dataTest.append({
          'responseData': responseData,
          'scoringData': maxScoringData
        })

    return dataTest

def flattenDict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flattenDict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def loadDataTestFlatten(filePath):
    with open(filePath, 'r') as file:
        data = json.load(file)
  
    dataTest = []
    for entry in data:
        logs = entry.get('logs', {})
        responseData = logs.get('data', {})
        keyValueLabels = logs.get('keyValueLabels', [])

        maxScoringData = max((kv[2] for kv in keyValueLabels if len(kv) > 2), default=None)
        # Ubah responseData menjadi string JSON
        if isinstance(responseData, (list, dict)):
          responseData = json.dumps(responseData)

        # Parse responseData back to a dictionary if it's a JSON string
        responseData = json.loads(responseData)
        
                # Flatten the responseData
        flattenedResponseData = flattenDict(responseData)
        flattenedList = []
        for key, value in flattenedResponseData.items():
            flattenedList.append({
                'responseDataFlatten': json.dumps({key: value})
            })
          
        dataTest.append({
            'responseData': json.dumps(responseData),
            'scoringData': maxScoringData,
            'dataFlatten': flattenedList
        })

    return dataTest
