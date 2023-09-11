from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)
server = app.server

app.title = "MCM7003 Data Visualization Interactive Demo"

# Load data from the provided URL
data_url = "https://raw.githubusercontent.com/LyaFaridha/Assignment4/main/df_arabica_clean.csv"
df = pd.read_csv(data_url)

# Create a bar chart for the 'Country of Origin' counts

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
        dcc.Checklist(
            id='show-chart',
            options=[
                {'label': 'Show Country Counts Chart', 'value': 'show-chart'}
            ],
            value=[],  # Initialize with no selected options
        ),
        dcc.Graph(id='graph-output'),
    ]
)

@app.callback(
    Output(component_id='graph-output', component_property='figure'),
    Input(component_id='show-chart', component_property='value')
)
def update_chart(show_chart):
    if 'show-chart' in show_chart:
        return fig_country_counts
    else:
        return {}

if __name__ == '__main__':
    app.run_server(debug=True)
In this modified code, a checklist (dcc.Checklist) is added to toggle the visibility of the fig_country_counts bar chart. When the "Show Country Counts Chart" checkbox is selected, the chart is displayed; otherwise, it is hidden.







if __name__ == '__main__':
    app.run_server(debug=True)
