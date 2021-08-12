import csv
import plotly.express as px

with open("Coffee.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x="Coffee", y="sleep", color="week")
    fig.show()