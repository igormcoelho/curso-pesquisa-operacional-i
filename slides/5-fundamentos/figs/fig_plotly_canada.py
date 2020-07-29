import plotly.express as px
import plotly as plotly

def draw_fig(filename):
	data_canada = px.data.gapminder().query("country == 'Canada'")
	fig = px.bar(data_canada, x='year', y='pop', height=200)
	fig.update_layout( margin=dict(l=0, r=0, t=50, b=0) )
	#fig.update_yaxes(automargin=True)
	fig.write_image(filename)
	return fig
