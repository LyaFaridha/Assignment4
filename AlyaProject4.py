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
    [html.H1("Data Visualization"),
     dcc.RadioItems(id='my-radio', options=['Country Counts'], value='Country Counts', inline=True),
     dcc.Graph(id='graph-output', figure={})]
)

@app.callback(
    Output(component_id='graph-output', component_property='figure'),
    Input(component_id='my-radio', component_property='value')
)
def update_my_graph(val_chosen):
    if val_chosen == 'Country Counts':
        return fig_country_counts

if __name__ == '__main__':
    app.run_server(debug=True)
