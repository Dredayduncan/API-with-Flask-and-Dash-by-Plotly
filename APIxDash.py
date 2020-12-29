import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
from flask import *

source = open("rainfall.txt", "r")

info = source.readlines()
general_info = [i.split(",") for i in info if i != "\n"]
head = [i[0] for i in general_info]
body = [i[-1] for i in general_info]
data = [{i[0]: i[-1]} for i in general_info]
alldata = []
a = 1
for i in data:
    info = {a: i}
    alldata.append(info)
    a += 1
update = open("rainfall.txt", "a")

server = Flask(__name__)

app1 = dash.Dash(__name__, server=server, url_base_pathname="/scatter/")
app2 = dash.Dash(__name__, server=server, url_base_pathname="/bar/")

app1.layout = html.Div([html.H1(style={"textAlign": "center", "background": "black", "color": "brown"},
                               children=["Cities and their Respective Rainfall",
    dcc.Graph(id="Cities-Rainfall",
              figure={
                  "data": [
                      go.Scatter(
                          x=[i for i in range(1, len(alldata))],
                          y=[i for i in body],
                          text=[i for i in head],
                          mode="lines+markers",
                          opacity=0.7,
                          marker={
                              "size": 15,
                              "line": {"width": 0.5, "color": "white"},
                          },
                          name=i
                      )for i in head
                  ],
                  "layout": go.Layout(
                        plot_bgcolor="Black",
                        paper_bgcolor="Black",
                        xaxis={'type': 'log', 'title': 'City', "color": "white"},
                        yaxis={'title': 'Rainfall', "color": "white"},
                        margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                        legend={'x': 0, 'y': 1},
                        hovermode='closest',
                        font={"color": "brown"}
                    )

              }
        )
    ])
])

app2.layout = html.Div(children=[
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


@server.route("/", methods=['GET', 'POST'])
def homepage():
    return jsonify(alldata)

@server.route("/add", methods=["POST"])
def requests():
    data = request.json.items()
    for i in data:
        info = i[0] + ", " + i[1] + "\n"
        update.write(info)
    update.close()
    return str(list(data))


@server.route("/city/<int:id>", methods=['GET', 'POST'])
def city(id):
    for i in alldata:
        for num, info in i.items():
            if id == num:
                return jsonify(info)
    else:
        return "ID not found"


@server.route("/cities", methods=['GET', 'POST'])
def cities():
    return jsonify(head)


@server.route("/rainfall", methods=['GET', 'POST'])
def rainfall():
    return jsonify(body)


@server.route("/dash/scatter", methods=["GET"])
def scatter():
    return app1.index()


@server.route("/dash/bar", methods=["GET"])
def bar():
    return app2.index()


server.run(debug=True)