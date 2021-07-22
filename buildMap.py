import pandas
import folium
from folium import plugins


map = folium.Map(location=[32.07478587906301, 34.78359362573951], zoom_start=15, control_scale=True)
map.add_child(plugins.Draw(export=False))
map.add_child(plugins.LocateControl())
map.add_child(plugins.MeasureControl(position='topleft', active_color='red', completed_color='red'))
fg = folium.FeatureGroup(name= "hvr foodcard")
map.get_root().add_child(folium.Element("מסעדות חבר - כרטיס כחול"))


data = pandas.read_json("foodcard_branches.json", encoding="utf-8-sig")

for index, row in data.iterrows():
    name = row["name"]
    desc = row["desc"]
    phone = row["phone"]
    category = row["category"]
    type = row["type"]
    latitude = float(row["latitude"])
    longitude = float(row["longitude"])
    pop = name +"\n"+ desc +"\n"+ phone +"\n"+ category +"\n"+ type
    fg.add_child(folium.Marker(location=[latitude,longitude], popup=pop, tooltip=name))

map.add_child(fg)

map.save("Map2.html")