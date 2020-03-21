import os

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import yfinance as yf

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = app.server

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

colors = {
    'background': '#eee',
    'text': '#557'
}

app.layout = html.Div(style = {'backgroundColor': colors['background'], 'textAlign': 'center'},
children = [
    html.H1(
        children = "Datos bursátiles",
        style = {
        'color': colors['text']
        }
    ),
    dcc.Graph(id = 'grafico'),

    html.Label('Ingrese ticker'),
    dcc.Input(id = 'ticker', value = None, type = 'text', debounce = True),
    #html.Button(id = 'submit-button', type = 'submit', children = 'Submit')

]
)

@app.callback(
    Output('grafico', 'figure'),
    [Input('ticker', 'value')]
)

def get_data(ticker):
    if ticker is None:
        raise dash.exceptions.PreventUpdate

    datos = yf.download(ticker)
    return {'data': [dict(y = datos['Close'])], 'layout': {'plot_bgcolor': colors['background'], 'paper_bgcolor': colors['background'], 'font': {'color': colors['text']}}}

if __name__ == '__main__':
    app.run_server(debug = True)
