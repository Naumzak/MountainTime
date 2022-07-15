import folium
m = folium.Map(location=[48.3497, 24.2563], zoom_start=13)
m.add_child(folium.ClickForMarker())
folium.Marker(
    [45.3288, -121.6625], popup="<i>Mt. Hood Meadows</i>"
).add_to(m)
m.save('osm_version.html')