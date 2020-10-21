import csv 
import json

def make_json(csvFilePath):
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader=csv.DictReader(csvf)
        i = 0
        for rows in csvReader:
            key=str(i)
            data[key]=rows
            for column in data:
                if column is None:
                    data[key][column]=""
            i+=1
    return data