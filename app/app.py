from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from preprocessing import predict_text_class

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

app.layout = html.Div(
    children = [
        html.Div("Input Text",style={
            "font-size":"30px"
        }),
        html.Div(style={
            'height':'20px',
            # 'border':'1px solid #ffffff'
        }),
        dcc.Textarea(id="input_text",
                  style={
                        'width':'40%',
                        'height':'200px',
                    }),
        html.Div(style={
            'height':'20px',
            # 'border':'1px solid #ffffff'
        }),
        html.Div("Prediction:",id = "output")
    ],
    # style = {
    #     'border':'1px solid #ffffff',
    # }
)

@app.callback(
    Output("output", "children"),
    Input("input_text", "value"),
)
def predict_class(input_text):
    # input_vec = preprocessText(input_text)
    if type(input_text) == str:
        article_class = predict_text_class(input_text)
        return 'The given new report belong to {} section.'.format(article_class)
    else:
        return 'No text entered'

if __name__ == "__main__":
    # app.run_server(debug=True)
    app.run_server(host='0.0.0.0',debug=True, port=8050)
    # app.run_server(host='0.0.0.0',port=8050)