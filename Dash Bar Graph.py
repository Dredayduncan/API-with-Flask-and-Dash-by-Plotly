import dash
import dash_core_components as dcc
import dash_html_components as html


myfile = open("rainfall.txt", "r")
info = myfile.readlines()
data = [info[i].split(",") for i in range(len(info))]
head = [i[0] for i in data]
body = [i[1] for i in data]


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(style={"textAlign": "center", "background": "black", "color": "Orange"},
            children=["Cities and their Respective Rainfall Measurements",
    dcc.Graph(
        figure={
            "data": [
                {"x": [i for i in head], "y": [i for i in body], "type": "bar", "name": [i for i in head]}
            ],
            "layout": {
                "plot_bgcolor": "Black",
                "paper_bgcolor": "Black",
                "font": {
                    "color": "Orange"
                }
            }
        }
    )

])
    ])


app.run_server(debug=True)
