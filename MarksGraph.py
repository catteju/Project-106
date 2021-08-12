import csv
import plotly.express as px

with open("Marks.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x="Marks", y="Present", color="RollNo")
    fig.show()