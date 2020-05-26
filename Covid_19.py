import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
df = pd.read_csv("https://github.com/Inodesain/COVID-19/blob/master/COVID_19_HISTORICAL_RECORD.csv?raw=True")
#df = df[df['COUNTRY_REGION']=='US']

pv = pd.pivot_table(df, index=['LAST_UPDATE'], columns=["COUNTRY_REGION"], values=['CONFIRMED'], aggfunc=sum, fill_value=0)
app = dash.Dash()
trace1 = go.Bar(x=pv.index, y=pv[('CONFIRMED', 'China')], name='China')
trace2 = go.Bar(x=pv.index, y=pv[('CONFIRMED', 'Italy')], name='Italy')
trace3 = go.Bar(x=pv.index, y=pv[('CONFIRMED', 'Spain')], name='Spain')
trace4 = go.Bar(x=pv.index, y=pv[('CONFIRMED', 'US')], name='United States')
trace5 = go.Bar(x=pv.index, y=pv[('CONFIRMED', 'France')], name='France')
trace6 = go.Bar(x=pv.index, y=pv[('CONFIRMED', 'Germany')], name='Germany')
trace7 = go.Bar(x=pv.index, y=pv[('CONFIRMED', 'Korea, South')], name='South Korea')
trace8 = go.Bar(x=pv.index, y=pv[('CONFIRMED', 'Thailand')], name='Thailand')
trace9 = go.Bar(x=pv.index, y=pv[('CONFIRMED', 'Iran')], name='Iran')
trace10 = go.Bar(x=pv.index, y=pv[('CONFIRMED', 'India')], name='India')
trace11 = go.Bar(x=pv.index, y=pv[('CONFIRMED', 'Singapore')], name='Singapore')
trace12 = go.Bar(x=pv.index, y=pv[('CONFIRMED', 'Indonesia')], name='Indonesia')
trace13 = go.Bar(x=pv.index, y=pv[('CONFIRMED', 'Malaysia')], name='Malaysia')

app.layout = html.Div(children=[
    html.H1(children='COVID 19 - SELECTED COUNTRIES'),
    html.Div(children='''Province/State Data'''),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11, trace12, trace13],
#            'data': [trace1],
            'layout':
            go.Layout(title='Confirmed Case', barmode='stack', height=900)
        })
])
if __name__ == '__main__':
    app.run_server(debug=True)



#import matplotlib.pyplot as plt
#import pandas as pd
#from ibmdbpy import IdaDataBase, IdaDataFrame

# @hidden_cell
# This connection object is used to access your data and contains your credentials.
# You might want to remove those credentials before you share your notebook.
#idadb_a47b5ab5614a45378ef30b10f44ef107 = IdaDataBase(dsn='DASHDB;Database=BLUDB;Hostname=dashdb-txn-sbox-yp-dal09-08.services.dal.bluemix.net;Port=50000;PROTOCOL=TCPIP;UID=nkf97195;PWD=nqk-4wr46m06v557')

#history = IdaDataFrame(idadb_a47b5ab5614a45378ef30b10f44ef107, 'NKF97195.COVID_19_HISTORICAL_RECORD').as_dataframe()
#history = pd.read_csv("https://github.com/Inodesain/COVID-19/blob/master/COVID_19_HISTORICAL_RECORD.csv?raw=True")
#history.sort_values(by=['LAST_UPDATE','COUNTRY_REGION','SEQ_NO'], inplace=True)
#history['LAST_UPDATE'] = pd.to_datetime(history['LAST_UPDATE'])
#history['DATE'] = history['LAST_UPDATE'].dt.day
#history.sort_values(by=['COUNTRY_REGION','LAST_UPDATE','SEQ_NO'])
#pd.set_option('display.max_columns', None)  
##pd.set_option('display.expand_frame_repr', False)
#pd.set_option('max_colwidth', -1)
#history1 = history[history['COUNTRY_REGION']=='US']
#history2 = history1[history1['CONFIRMED'] > 0]
#history2 = history2[history2['LAST_UPDATE'] >= '2020-03-01']
#history = history2[history2['LAST_UPDATE'] <= '2020-03-31']
#history2.sort_values(by=['COUNTRY_REGION'])
#history

