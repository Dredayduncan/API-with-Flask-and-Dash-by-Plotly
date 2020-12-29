import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

stats = open("rainfall.txt", "r")
info = stats.readlines()
data = [info[i].split(",") for i in range(len(info))]
head = [i[0] for i in data]
body = [i[1] for i in data]
match = [{head[i]: body[i]} for i in range(len(info))]

app.layout = html.Div([html.H1(style={"textAlign": "center", "background": "black", "color": "skyblue"},
                               children=["Cities and their Respective Rainfall",
                                         dcc.RadioItems(id="Cities",
                                                        options=[{"label": i, "value": i} for i in head],
                                                        labelStyle={"display": "inline-block"},
                                                        style={"fontSize": 30}
                                                        ),
                                         dcc.RadioItems(
                                             id="appearance",
                                             options=[{"label": "Light Mode", "value": "LM"},
                                                      {"label": "Dark Mode", "value": "DM"}
                                                      ],
                                             value="LM",
                                             style={"fontSize": 20},
                                             labelStyle={"display": "flex"}
                                         ),
                                         dcc.Graph(id="Cities-Rainfall",
                                                   figure={
                                                       "data": [
                                                           go.Scatter(
                                                               x=[i for i in range(1, len(data))],
                                                               y=[i for i in body],
                                                               text=[i for i in head],
                                                               mode="lines+markers",
                                                               opacity=0.7,
                                                               marker={
                                                                   "size": 15,
                                                                   "line": {"width": 0.5, "color": "white"},
                                                               },
                                                               name=i
                                                           ) for i in head
                                                       ],
                                                       "layout": go.Layout(
                                                           plot_bgcolor="white",
                                                           paper_bgcolor="white",
                                                           xaxis={'type': 'log', 'title': 'City', "color": "black"},
                                                           yaxis={'title': 'Rainfall', "color": "black"},
                                                           margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                                                           legend={'x': 0, 'y': 1},
                                                           hovermode='closest',
                                                           font={"color": "brown"}
                                                       )
                                                   }
                                                   )
                                         ])
                       ])


@app.callback(Output("Cities-Rainfall", "figure"), [Input("Cities", "value"), Input("appearance", "value")])
def selection(choice1, choice2):
    newdata = []
    color = ""
    linecolor = ""
    if choice2 == "LM":
        color += "white"
        linecolor += "black"
    elif choice2 == "DM":
        color += "Black"
        linecolor += "White"

    for i in match:
        for m, n in i.items():
            if choice1 == m:
                newdata.append(go.Scatter(x=[len(m)], y=[n], text=m, mode="markers", opacity=0.7,
                                          marker={"size": 15, "line": {"width": 0.5, "color": "white"}},
                                          name=m), )
                figure = {
                    "data": newdata,
                    "layout": go.Layout(
                        plot_bgcolor=color,
                        paper_bgcolor=color,
                        xaxis={'type': 'log', 'title': 'City', "color": linecolor},
                        yaxis={'title': 'Rainfall', "color": linecolor},
                        margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                        legend={'x': 0, 'y': 1},
                        hovermode='closest',
                        font={"color": "brown"}
                    )
                }
                return figure
    else:
        figure = {
            "data": [
                go.Scatter(
                    x=[i for i in range(1, len(data))],
                    y=[i for i in body],
                    text=[i for i in head],
                    mode="lines+markers",
                    opacity=0.7,
                    marker={
                        "size": 15,
                        "line": {"width": 0.5, "color": "white"},
                    },
                    name=i
                ) for i in head
            ],
            "layout": go.Layout(
                plot_bgcolor=color,
                paper_bgcolor=color,
                xaxis={'type': 'log', 'title': 'City', "color": linecolor},
                yaxis={'title': 'Rainfall', "color": linecolor},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest',
                font={"color": "brown"}
            )
        }

        return figure


app.run_server(debug=True)
