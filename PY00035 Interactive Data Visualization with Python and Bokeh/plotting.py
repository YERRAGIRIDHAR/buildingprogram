from bokeh.models import HoverTool, ColumnDataSource # For adding hover and for hover we are adding columns of our data
from motion_detection import df
from bokeh.plotting import figure, show, output_file



df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds=ColumnDataSource(df)

p = figure(x_axis_type ='datetime', height = 100, width = 500, sizing_mode= "stretch_both", title="Motion Graph") # for better view of graph use  'sizing_mode= "stretch_both"'
p.yaxis.minor_tick_line_color=None
# p.ygrid[0].ticker.desired_num_ticks=1

hover = HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
p.add_tools(hover)

q = p.quad(left ="Start", right ="End", bottom = 0, top = 1, color = "green", source=cds)

output_file("Motion.graph.html")

show(p)