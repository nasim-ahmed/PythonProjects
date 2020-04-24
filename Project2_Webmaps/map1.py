import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    if 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'
 

map=folium.Map(location=[52.153848, 12.206929], zoom_start=6, tiles="Stamen Terrain")
 
fgv= folium.FeatureGroup(name="Volcanoes")

for lt,ln, el in zip(lat,lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius = 6, popup=folium.Popup(str(el) + "m", parse_html=True), fill_color=color_producer(el), color= 'grey', fill_opacity = 0.7, fill=True ))

fgp= folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005']< 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())
  
map.save("Map1.html")