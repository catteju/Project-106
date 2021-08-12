import csv
import plotly.express as px
import numpy as n

def getDataSource(dataPath):
    marks = []
    present = []
    with open(dataPath) as f:
        df = csv.DictReader(f)
        for row in df:
            marks.append(float(row["Marks"]))
            present.append(float(row["Present"]))
    return {"x": marks, "y" : present}

def findCorrelation(dataSource) : 
    correlation = n.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation Between Marks And Attendance Is",correlation[0,1])

def main():
    dataPath = "Marks.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

main()            