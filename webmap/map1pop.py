import folium
import pandas as pd 

data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
 
html = """<h4>Volcano information:</h4>
Height: %s m
"""
 
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tile="Mapbox Bright")
fg = folium.FeatureGroup(name = "My Map")
 
for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=300, height=150)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "purple")))
 
 
map.add_child(fg)
map.save("map3.html")