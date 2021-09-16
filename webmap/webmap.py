import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")

lat = list(data["LAT"]) #Extractng latitude values to display multiple locations
lon =  list(data["LON"]) #Extractng longitude values to display multiple locations
name = list(data["NAME"]) #Extractng name values to display multiple locations
elev = list(data["ELEV"]) #Extractng eleveation values to display multiple locations

'''To assign different colors for diff location based on elevation'''

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "blue"
    else:
        return "red"

'''Configuring map'''

map = folium.Map(location=[34.22,-90.23], zoom_start=6, tiles="Stamen Terrain")

'''For different locations and lan long, Layer-1 Volcaneos, 'Layer-2 Popolation'''

fgv = folium.FeatureGroup(name = 'Volcaneos')

for lt, ln, el,na in zip(lat, lon, elev, name):
    fgv.add_child(folium.Marker(location=[lt, ln], popup=str(na)+ str(el)+ " m", icon=folium.Icon(color=color_producer(el))))

fgp = folium.FeatureGroup(name= "Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),style_function=lambda x: {"fillColor":"red" if x["properties"]["POP2005"] <10000000 else 'orang' if 1000000 <=x ['properties']['POP2005']<2000000 else 'green'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
'''For saving the map with name Map1'''

map.save("map1.html")

