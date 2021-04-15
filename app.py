import folium

m = folium.Map(location=[41.2995, 69.2401], zoom_start=14)

tooltip = "Home"

folium.Marker(
  [41.291763, 69.202404], 
  popup="<i>Dom, milliy Dom<i>", 
  tooltip=tooltip,
  icon=folium.Icon(color="green")
).add_to(m)










m.save("index.html")
