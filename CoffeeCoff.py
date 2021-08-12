import csv
import plotly.express as px
import numpy as n

def getDataSource(dataPath):
    coffee = []
    sleep = []
    with open(dataPath) as f:
        df = csv.DictReader(f)
        for row in df:
            coffee.append(float(row["Coffee"]))
            sleep.append(float(row["sleep"]))
    return {"x": coffee, "y" : sleep}

def findCorrelation(dataSource) : 
    correlation = n.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation Between Coffee And Sleep Is",correlation[0,1])

def main():
    dataPath = "Coffee.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

main()            