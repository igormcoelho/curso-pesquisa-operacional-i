import plotly.express as px
import plotly as plotly
import plotly.graph_objects as go
import pandas as pd

def draw_fig(filename):
	#x= [1, 2, 3, 4]
	#y= [1, 2, 3, 4]
	#xy = pd.DataFrame({'vx':x, 'vy': y})
	#fig = px.line(xy, x="vx", y="vy", title='Test', height=300)
	#fig.update_layout( margin=dict(l=0, r=0, t=50, b=0) )
	#fig = go.Figure(go.Scatter(x=[0,0,1500,1500,0], y=[0,3125, 1250, 0,0], fill="toself"))
	x=[0,    1500, 1500]
	y=[3125, 1250, 0]
	px.width = 100
	px.height = 100
	xy = pd.DataFrame({'x1':x, 'x2': y})
	fig = px.area(xy, x="x1", y="x2") 
	fig.add_shape(
        dict(type="line",
			x0=0, y0=0, x1=0, y1=7000,
            line=dict(color="Black", width=3)
	))
	fig.add_shape(
        dict(type="line",
			x0=0, y0=0, x1=3000, y1=0,
            line=dict(color="Black", width=3)
	))
	fig.add_shape(
        dict(type="line",
			x0=1500, y0=0, x1=1500, y1=7000,
            line=dict(color="RoyalBlue", width=3)
	))
	fig.add_shape(
        dict(type="line",
			x0=0, y0=6000, x1=3000, y1=6000,
            line=dict(color="Gray", width=3)
	))
	fig.add_shape(
        dict(type="line",
			x0=0, y0=4500, x1=4500, y1=0,
            line=dict(color="Gray", width=3)
	))
	fig.add_shape(
        dict(type="line",
			x0=0, y0=3125, x1=2500, y1=0,
            line=dict(color="RoyalBlue", width=3)
	))
	fig.add_shape(
        dict(type="line",
			x0=0, y0=4250, x1=2125, y1=0,
            line=dict(color="Red", width=3)
	))
	fig.add_shape(
        dict(type="line",
			x0=0, y0=2000, x1=1000, y1=0,
            line=dict(color="Red", width=3)
	))
	fig.add_shape(
        dict(type="line",
			x0=0, y0=5400, x1=2700, y1=0,
            line=dict(color="Red", width=3)
	))
	fig.update_layout( margin=dict(l=0, r=0, t=50, b=0) )
	fig.write_image(filename)
	return fig
