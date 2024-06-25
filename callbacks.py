from dash import dcc, html, Input, Output, State, MATCH, ctx, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import base64
import io
import uuid
import plotly.graph_objects as go
from styles import custom_css

def register_callbacks(app):

    @app.callback(
        Output('tabs', 'children'),
        [Input('add-tab-button', 'n_clicks'),
         Input('rename-tab-button', 'n_clicks')],
        [State('tabs', 'children'),
         State('tabs', 'value'),
         State('new-tab-name', 'value'),
         State('rename-tab-name', 'value')]
    )
    def manage_tabs(add_clicks, rename_clicks, children, active_tab, new_tab_name, rename_tab_name):
        triggered_id = ctx.triggered_id
        if triggered_id == 'add-tab-button' and add_clicks > 0:
            new_tab_index = str(uuid.uuid4())
            tab_label = new_tab_name if new_tab_name else f'Upload Data {add_clicks}'
            children.append(
                dcc.Tab(label=tab_label, value=f'tab-{new_tab_index}', children=[
                    html.Div(id='upload-container', children=[
                        dcc.Upload(
                            id={'type': 'upload-data', 'index': new_tab_index},
                            children=html.Div([
                                'Drag and Drop or ',
                                html.A('Select a CSV or Excel File')
                            ]),
                            style=custom_css['upload'],
                            multiple=False
                        ),
                        html.Div(id={'type': 'upload-feedback', 'index': new_tab_index}, style={'color': 'red', 'fontSize': '12px', 'margin': '10px'})
                    ]),
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                dcc.Dropdown(
                                    id={'type': 'graph-type', 'index': new_tab_index},
                                    options=[
                                        {'label': 'Temporal Series', 'value': 'line'},
                                        {'label': 'Scatter Plot', 'value': 'scatter'},
                                        {'label': 'Histogram', 'value': 'histogram'},
                                        {'label': 'Map', 'value': 'map'}
                                    ],
                                    value='line',
                                    style=custom_css['dropdown']
                                ),
                                html.Button("Toggle Axis Selection", id={'type': 'toggle-button', 'index': new_tab_index}, n_clicks=0, style=custom_css['toggle-button']),
                                html.Div(id={'type': 'axis-selection', 'index': new_tab_index}, style={'display': 'none'}, children=[
                                    html.Label('Select X-axis:', style=custom_css['axis-selection']),
                                    dcc.Dropdown(
                                        id={'type': 'xaxis-column', 'index': new_tab_index},
                                        style=custom_css['dropdown']
                                    ),
                                    html.Br(),
                                    html.Label('Select Y-axis:', style=custom_css['axis-selection']),
                                    dcc.Dropdown(
                                        id={'type': 'yaxis-column', 'index': new_tab_index},
                                        multi=True,
                                        style=custom_css['dropdown']
                                    )
                                ])
                            ], style={'width': '100%'})
                        , width=3),
                        dbc.Col(
                            html.Div(id={'type': 'tabs-container', 'index': new_tab_index}, style={'display': 'block'}, children=[
                                dcc.Tabs(id={'type': 'inner-tabs', 'index': new_tab_index}, children=[
                                    dcc.Tab(label='Graph', children=[
                                        dcc.Graph(id={'type': 'graph', 'index': new_tab_index}, config={'displayModeBar': True}, style=custom_css['graph'])
                                    ]),
                                    dcc.Tab(label='Summary Statistics', children=[
                                        html.Div(id={'type': 'summary-statistics', 'index': new_tab_index}, style=custom_css['graph']),
                                        html.Button("Export Summary Statistics", id={'type': 'export-summary', 'index': new_tab_index}, style=custom_css['button']),
                                        dcc.Download(id={'type': 'download-summary', 'index': new_tab_index})
                                    ]),
                                    dcc.Tab(label='Correlation Matrix', children=[
                                        html.Div(id={'type': 'correlation-matrix', 'index': new_tab_index}, style=custom_css['graph']),
                                        html.Button("Export Correlation Matrix", id={'type': 'export-correlation', 'index': new_tab_index}, style=custom_css['button']),
                                        dcc.Download(id={'type': 'download-correlation', 'index': new_tab_index})
                                    ])
                                ])
                            ])
                        , width=9)
                    ], id={'type': 'data-section', 'index': new_tab_index})
                ])
            )
        elif triggered_id == 'rename-tab-button' and rename_clicks > 0 and rename_tab_name:
            for tab in children:
                if tab['props']['value'] == active_tab:
                    tab['props']['label'] = rename_tab_name
                    break
        return children

    @app.callback(
        [Output({'type': 'upload-data', 'index': MATCH}, 'style'),
         Output({'type': 'data-section', 'index': MATCH}, 'style'),
         Output({'type': 'toggle-button', 'index': MATCH}, 'style'),
         Output({'type': 'upload-feedback', 'index': MATCH}, 'children')],
        Input({'type': 'upload-data', 'index': MATCH}, 'contents')
    )
    def show_elements(contents):
        if contents:
            return {'display': 'none'}, {'display': 'flex'}, custom_css['toggle-button'], ''
        return custom_css['upload'], {'display': 'none'}, {'display': 'none'}, 'Please upload a CSV or Excel file.'

    @app.callback(
        Output({'type': 'axis-selection', 'index': MATCH}, 'style'),
        Input({'type': 'toggle-button', 'index': MATCH}, 'n_clicks')
    )
    def toggle_axis_selection(n_clicks):
        if n_clicks % 2 == 1:
            return {**custom_css['axis-selection'], 'display': 'block'}
        return {'display': 'none'}

    @app.callback(
        [Output({'type': 'xaxis-column', 'index': MATCH}, 'options'),
         Output({'type': 'yaxis-column', 'index': MATCH}, 'options'),
         Output({'type': 'summary-statistics', 'index': MATCH}, 'children'),
         Output({'type': 'correlation-matrix', 'index': MATCH}, 'children')],
        Input({'type': 'upload-data', 'index': MATCH}, 'contents')
    )
    def update_dropdown(contents):
        if contents is None:
            return [], [], "", ""

        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        
        try:
            if 'csv' in content_type:
                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')), delimiter=';')
            elif 'excel' in content_type or 'spreadsheet' in content_type:
                df = pd.read_excel(io.BytesIO(decoded))
            else:
                return [], [], "Unsupported file format. Please upload a CSV or Excel file.", ""

        except Exception as e:
            return [], [], f"Error processing file: {e}", ""

        options = [{'label': col, 'value': col} for col in df.columns]

        summary_stats = df.describe().transpose()
        summary_stats.reset_index(inplace=True)
        summary_table = dash_table.DataTable(
            columns=[{"name": i, "id": i} for i in summary_stats.columns],
            data=summary_stats.to_dict('records'),
            style_table={'overflowX': 'auto'}
        )

        numeric_df = df.select_dtypes(include=[float, int])
        corr_matrix = numeric_df.corr().reset_index()
        corr_table = dash_table.DataTable(
            columns=[{"name": i, "id": i} for i in corr_matrix.columns],
            data=corr_matrix.to_dict('records'),
            style_table={'overflowX': 'auto'}
        )

        return options, options, summary_table, corr_table

    @app.callback(
        Output({'type': 'graph', 'index': MATCH}, 'figure'),
        [Input({'type': 'xaxis-column', 'index': MATCH}, 'value'),
         Input({'type': 'yaxis-column', 'index': MATCH}, 'value'),
         Input({'type': 'graph-type', 'index': MATCH}, 'value')],
        [State({'type': 'upload-data', 'index': MATCH}, 'contents')]
    )
    def update_graph(xaxis_column_name, yaxis_column_names, graph_type, contents):
        if contents is None or xaxis_column_name is None or not yaxis_column_names:
            return {}

        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        
        try:
            if 'csv' in content_type:
                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')), delimiter=';')
            elif 'excel' in content_type or 'spreadsheet' in content_type:
                df = pd.read_excel(io.BytesIO(decoded))
            else:
                return {}
        except Exception as e:
            return {}

        fig = go.Figure()

        if graph_type == 'line':
            for y in yaxis_column_names:
                fig.add_trace(go.Scatter(x=df[xaxis_column_name], y=df[y], mode='lines', name=y))
        elif graph_type == 'scatter':
            for y in yaxis_column_names:
                fig.add_trace(go.Scatter(x=df[xaxis_column_name], y=df[y], mode='markers', name=y))
        elif graph_type == 'histogram':
            fig.add_trace(go.Histogram(x=df[xaxis_column_name]))
        elif graph_type == 'map':
            if 'LATITUDE' in df.columns and 'LONGITUDE' in df.columns:
                fig.add_trace(go.Scattergeo(
                    lat=df['LATITUDE'],
                    lon=df['LONGITUDE'],
                    text=df['ESTACAO'],
                    mode='markers'
                ))
                fig.update_layout(
                    geo=dict(
                        projection_type='natural earth',
                        showland=True,
                        landcolor='rgb(217, 217, 217)',
                        subunitwidth=1,
                        countrywidth=1,
                        subunitcolor='rgb(255, 255, 255)',
                        countrycolor='rgb(255, 255, 255)'
                    )
                )
            else:
                return {}
        else:
            return {}

        fig.update_layout(
            xaxis_title=xaxis_column_name,
            yaxis_title='Values' if graph_type != 'histogram' else 'Count',
            font=dict(size=10),
            hovermode='closest'
        )

        return fig

    @app.callback(
        [Output('new-tab-name', 'value'),
         Output('rename-tab-name', 'value')],
        [Input('add-tab-button', 'n_clicks'),
         Input('rename-tab-button', 'n_clicks')]
    )
    def clear_input_fields(add_clicks, rename_clicks):
        return "", ""

    @app.callback(
        Output({'type': 'download-summary', 'index': MATCH}, 'data'),
        Input({'type': 'export-summary', 'index': MATCH}, 'n_clicks'),
        State({'type': 'upload-data', 'index': MATCH}, 'contents'),
        prevent_initial_call=True
    )
    def download_summary_statistics(n_clicks, contents):
        if contents:
            content_type, content_string = contents.split(',')
            decoded = base64.b64decode(content_string)
            try:
                if 'csv' in content_type:
                    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')), delimiter=';')
                elif 'excel' in content_type or 'spreadsheet' in content_type:
                    df = pd.read_excel(io.BytesIO(decoded))
                else:
                    return None
            except Exception as e:
                return None

            summary_stats = df.describe().transpose()
            return dcc.send_data_frame(summary_stats.to_csv, "summary_statistics.csv")

    @app.callback(
        Output({'type': 'download-correlation', 'index': MATCH}, 'data'),
        Input({'type': 'export-correlation', 'index': MATCH}, 'n_clicks'),
        State({'type': 'upload-data', 'index': MATCH}, 'contents'),
        prevent_initial_call=True
    )
    def download_correlation_matrix(n_clicks, contents):
        if contents:
            content_type, content_string = contents.split(',')
            decoded = base64.b64decode(content_string)
            try:
                if 'csv' in content_type:
                    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')), delimiter=';')
                elif 'excel' in content_type or 'spreadsheet' in content_type:
                    df = pd.read_excel(io.BytesIO(decoded))
                else:
                    return None
            except Exception as e:
                return None

            numeric_df = df.select_dtypes(include=[float, int])
            corr_matrix = numeric_df.corr()
            return dcc.send_data_frame(corr_matrix.to_csv, "correlation_matrix.csv")
