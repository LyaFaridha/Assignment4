from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)
server = app.server

app.title = "MCM7003 Data Visualization Interactive Demo"

# Load data from the provided URL
data_url = "https://raw.githubusercontent.com/LyaFaridha/Assignment3/main/df_arabica_clean.csv"
df = pd.read_csv(data_url)

# Create a bar chart for the 'Country of Origin' counts
country_counts = df['Country of Origin'].value_counts()
fig_country_counts = px.bar(country_counts, x=country_counts.index, y=country_counts.values)

fig_country_counts.update_layout(
    xaxis_title='Country of Origin',
    yaxis_title='Count',
    title={'text': 'Distribution of Country of Origins', 'x': 0.5}
)

app.layout = html.Div(
    [
        html.H1("Data Visualization"),
        dcc.RadioItems(id='my-radio', options=['Country Counts'], value='Country Counts', inline=True),
        dcc.Graph(id='graph-output', figure={}),
        html.Br(),
        dcc.Checklist(
            id='my-checkbox',
            options=[
                {'label': 'Show Data Table', 'value': 'show-table'},
                # Add more options if needed
            ],
            value=[],  # Initialize with no selected options
        ),
        dcc.Tabs(id='tabs', value='tab-1', children=[
            dcc.Tab(label='Tab 1', value='tab-1'),
            dcc.Tab(label='Tab 2', value='tab-2'),
            # Add more tabs if needed
        ]),
        html.Div(id='tabs-content'),
    ]
)

@app.callback(
    Output(component_id='graph-output', component_property='figure'),
    Output('tabs-content', 'children'),
    Input(component_id='my-radio', component_property='value'),
    Input('my-checkbox', 'value'),
    Input('tabs', 'value')
)
def update_my_graph(val_chosen, checkbox_value, tab_value):
    graphs = []  # List to hold the selected graphs
    if val_chosen == 'Country Counts':
        graphs.append(fig_country_counts)

    tabs_content = []  # List to hold tab content
    if 'show-table' in checkbox_value:
        # Display data table when the 'Show Data Table' checkbox is selected
        tabs_content.append(
            html.Div([
                html.H3('Data Table'),
                dcc.DataTable(
                    id='datatable',
                    columns=[{"name": i, "id": i} for i in df.columns],
                    data=df.to_dict('records'),
                )
            ])
        )

    if tab_value == 'tab-1':
        # Add content for Tab 1
        tabs_content.append(
            html.Div([
                html.H3('Tab 1 Content'),
                # Add your content here
            ])
        )
    elif tab_value == 'tab-2':
        # Add content for Tab 2
        tabs_content.append(
            html.Div([
                html.H3('Tab 2 Content'),
                # Add your content here
            ])
        )

    return graphs, tabs_content

if __name__ == '__main__':
    app.run_server(debug=True)
