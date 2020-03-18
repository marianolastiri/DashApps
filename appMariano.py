import dash
import dash_core_components as dcc
import dash_html_components as html
import yfinance as yf

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

colors = {
    'background': '#eee',
    'text': '#557'
}

def get_data(ticker):
    datos = yf.download(ticker)
    return datos

ggal = get_data('ggal')

app.layout = html.Div(style = {'backgroundColor': colors['background']},
children = [
    html.H1(
        children = "Datos bursátiles",
        style = {
        'textAlign': 'center',
        'color': colors['text']
        }
    ),
    dcc.Graph(
        figure = {
            'data': [
                dict(
                    y = ggal['Close']
                )
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        },
    ),

    html.Label('Ingrese ticker'),
    dcc.Input(value = 'GGAL', type = 'text'),

])

if __name__ == '__main__':
    app.run_server(debug = True)
