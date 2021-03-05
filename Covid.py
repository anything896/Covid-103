import csv
import plotly.express as px

with open("Copy+of+data+-+data.csv") as csv_file:
    ANYTHING=csv.DictReader(csv_file)
    fig=px.scatter(ANYTHING,x="date",y="cases",color=("country"))
    fig.show()