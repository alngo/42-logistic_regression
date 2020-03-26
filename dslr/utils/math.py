def normalize(list):
    minValue = min(list)
    maxValue = max(list)
    newList = (list - minValue) / (maxValue - minValue)
    return [newList, minValue, maxValue]
