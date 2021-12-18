import pandas as pd
import plotly.figure_factory as ff

chart=pd.read_csv('data.csv')

fig=ff.create_distplot([chart["Avg Rating"].tolist()],['Average Rating'], show_hist= False)

fig.show()