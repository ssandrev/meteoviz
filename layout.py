from dash import dcc, html
import dash_bootstrap_components as dbc
from styles import custom_css

def create_layout():
    return dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("MeteoViz", style=custom_css['header']), className="text-center mb-4")
        ]),
        dbc.Row([
            dbc.Col(
                html.Button("Add Tab", id='add-tab-button', n_clicks=0, style=custom_css['button']),
                width=2
            ),
            dbc.Col(
                dcc.Input(id='new-tab-name', type='text', placeholder='Enter tab name', style=custom_css['input']),
                width=3
            ),
            dbc.Col(
                html.Button("Rename Tab", id='rename-tab-button', n_clicks=0, style=custom_css['button']),
                width=2
            ),
            dbc.Col(
                dcc.Input(id='rename-tab-name', type='text', placeholder='Enter new tab name', style=custom_css['input']),
                width=3
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Tabs(id='tabs', value='tab-0', children=[
                    dcc.Tab(label='Upload Data', value='tab-0', children=[
                        html.Div(id='upload-container', children=[
                            dcc.Upload(
                                id={'type': 'upload-data', 'index': '0'},
                                children=html.Div([
                                    'Drag and Drop or ',
                                    html.A('Select a CSV or Excel File')
                                ]),
                                style=custom_css['upload'],
                                multiple=False
                            ),
                            html.Div(id={'type': 'upload-feedback', 'index': '0'}, style={'color': 'red', 'fontSize': '12px', 'margin': '10px'})
                        ]),
                        dbc.Row([
                            dbc.Col(
                                html.Div([
                                    dcc.Dropdown(
                                        id={'type': 'graph-type', 'index': '0'},
                                        options=[
                                            {'label': 'Temporal Series', 'value': 'line'},
                                            {'label': 'Scatter Plot', 'value': 'scatter'},
                                            {'label': 'Histogram', 'value': 'histogram'},
                                            {'label': 'Map', 'value': 'map'}
                                        ],
                                        value='line',
                                        style=custom_css['dropdown']
                                    ),
                                    html.Button("Toggle Axis Selection", id={'type': 'toggle-button', 'index': '0'}, n_clicks=0, style=custom_css['toggle-button']),
                                    html.Div(id={'type': 'axis-selection', 'index': '0'}, style={'display': 'none'}, children=[
                                        html.Label('Select X-axis:', style=custom_css['axis-selection']),
                                        dcc.Dropdown(
                                            id={'type': 'xaxis-column', 'index': '0'},
                                            style=custom_css['dropdown']
                                        ),
                                        html.Br(),
                                        html.Label('Select Y-axis:', style=custom_css['axis-selection']),
                                        dcc.Dropdown(
                                            id={'type': 'yaxis-column', 'index': '0'},
                                            multi=True,
                                            style=custom_css['dropdown']
                                        )
                                    ])
                                ], style={'width': '100%'})
                            , width=3),
                            dbc.Col(
                                html.Div(id={'type': 'tabs-container', 'index': '0'}, style={'display': 'block'}, children=[
                                    dcc.Tabs(id={'type': 'inner-tabs', 'index': '0'}, children=[
                                        dcc.Tab(label='Graph', children=[
                                            dcc.Graph(id={'type': 'graph', 'index': '0'}, config={'displayModeBar': True}, style=custom_css['graph'])
                                        ]),
                                        dcc.Tab(label='Summary Statistics', children=[
                                            html.Div([
                                                html.Div(id={'type': 'summary-statistics', 'index': '0'}, style=custom_css['small-text']),
                                                html.Button("Export Summary Statistics", id={'type': 'export-summary', 'index': '0'}, style=custom_css['button']),
                                                dcc.Download(id={'type': 'download-summary', 'index': '0'})
                                            ])
                                        ]),
                                        dcc.Tab(label='Correlation Matrix', children=[
                                            html.Div([
                                                html.Div(id={'type': 'correlation-matrix', 'index': '0'}, style=custom_css['small-text']),
                                                html.Button("Export Correlation Matrix", id={'type': 'export-correlation', 'index': '0'}, style=custom_css['button']),
                                                dcc.Download(id={'type': 'download-correlation', 'index': '0'})
                                            ])
                                        ])
                                    ])
                                ])
                            , width=9)
                        ], id={'type': 'data-section', 'index': '0'})
                    ])
                ]),
                width=12
            )
        ])
    ], fluid=True)
