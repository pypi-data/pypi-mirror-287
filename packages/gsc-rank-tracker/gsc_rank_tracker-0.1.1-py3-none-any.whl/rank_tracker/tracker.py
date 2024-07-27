import datetime
import os
import pickle
import pandas as pd
import plotly.graph_objs as go
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from statsmodels.nonparametric.smoothers_lowess import lowess

# Configuration parameters
API_VERSION = 'v1'
SITE_URL = 'https://example.co.uk'  # Replace with the actual site URL

# Function to get credentials file from the 'secret' folder
def get_credentials_file_from_secret_folder():
    """Retrieve the credentials file from the 'secret' directory."""
    for filename in os.listdir('secret'):
        if filename.endswith('.json'):
            return os.path.join('secret', filename)
    raise FileNotFoundError("No JSON file found in the 'secret' folder.")

# Authenticate with Google Search Console
def authenticate_gsc():
    """Authenticate with Google Search Console."""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        CREDENTIALS_FILE = get_credentials_file_from_secret_folder()
        flow = InstalledAppFlow.from_client_secrets_file(
            CREDENTIALS_FILE,
            scopes=['https://www.googleapis.com/auth/webmasters.readonly']
        )
        creds = flow.run_local_server(port=8080)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('searchconsole', API_VERSION, credentials=creds)

# Array of keywords
QUERIES = [
    'query 1',
    'query keyword 2',
    'query term 3',
    'and so on 4',
    'final query without comma'
    # FYI - continue as needed, anything 30 looks messy
]

# Function to fetch query data
def fetch_query_data(service, queries, start_date, end_date):
    all_data = []
    for query in queries:
        request = {
            'startDate': start_date,
            'endDate': end_date,
            'dimensions': ['query', 'date'],
            'dimensionFilterGroups': [{
                'filters': [{
                    'dimension': 'query',
                    'operator': 'equals',
                    'expression': query
                }]
            }],
            'rowLimit': 25000
        }
        response = service.searchanalytics().query(siteUrl=SITE_URL, body=request).execute()
        for row in response.get('rows', []):
            all_data.append({
                'query': row['keys'][0],
                'date': datetime.datetime.strptime(row['keys'][1], '%Y-%m-%d'),
                'position': row['position']
            })
    df = pd.DataFrame(all_data)
    df['date'] = pd.to_datetime(df['date'])
    # Resample to weekly frequency, taking the mean position for the week
    df.set_index('date', inplace=True)
    weekly_df = df.groupby('query').resample('W').mean().reset_index()
    return weekly_df

# Function to visualise insights with smoother lines
def visualize_insights(df):
    fig = go.Figure()
    for query in df['query'].unique():
        query_df = df[df['query'] == query]
        fig.add_trace(go.Scatter(
            x=query_df['date'],
            y=query_df['position'],
            mode='lines',
            name=query,
            line=dict(shape='spline')  # Spline shape for smooth line
        ))

    # Update layout
    fig.update_layout(
        title='Search Query Positions Over Time - Aggregated Weekly',
        xaxis_title='Date',
        yaxis_title='Position',
        yaxis=dict(autorange='reversed'),
        hovermode='x unified',
        template='plotly_white'
    )

    fig.show()

# Main execution logic
def main():
    service = authenticate_gsc()
    end_date = datetime.datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.datetime.now() - datetime.timedelta(days=180)).strftime('%Y-%m-%d')
    query_data = fetch_query_data(service, QUERIES, start_date, end_date)
    query_data['date'] = pd.to_datetime(query_data['date'])
    visualize_insights(query_data)

if __name__ == '__main__':
    main()
