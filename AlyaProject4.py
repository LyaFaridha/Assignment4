from dash import Dash, html, dcc, Input, Output, State
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
        
        # Radio Items
        dcc.RadioItems(id='my-radio', options=['Country Counts', 'Aroma vs Flavor', 'Processing Method Comparison'], value='Country Counts', inline=True),
        
        # Graph Output
        dcc.Graph(id='graph-output', figure={}),
        
        # Checkbox
        dcc.Checklist(id='checkbox', options=[{'label': 'Show Data Table', 'value': 'show-data-table'}], value=[]),
        
        # Tabs
        dcc.Tabs(id="tabs", value='tab-1', children=[
            dcc.Tab(label='Tab 1', value='tab-1'),
            dcc.Tab(label='Tab 2', value='tab-2'),
        ]),
        
        # Tab content
        html.Div(id='tabs-content')
    ]
)

@app.callback(
    Output(component_id='graph-output', component_property='figure'),
    Output('tabs-content', 'children'),
    Input(component_id='my-radio', component_property='value'),
    State('checkbox', 'value')
)
def update_my_graph(val_chosen, checkbox_value):
    if val_chosen == 'Country Counts':
        return fig_country_counts, None
    elif val_chosen == 'Aroma vs Flavor':
        # Add your aroma vs flavor scatter plot here
        return None, "You selected Aroma vs Flavor tab"
    elif val_chosen == 'Processing Method Comparison':
        # Add your processing method comparison plot here
        return None, "You selected Processing Method Comparison tab"

if __name__ == '__main__':
    app.run_server(debug=True)
