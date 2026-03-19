import folium
import os
import geopandas as gpd

processed_path = os.path.join('data', 'processed')
figures_path = os.path.join('report', 'figures')

filtered_parks_buff = gpd.read_file(os.path.join(processed_path, 'filtered_parks_buff.gpkg'))
near_parks = gpd.read_file(os.path.join(processed_path, 'near_parks.gpkg'))
admin_boundaries = gpd.read_file(os.path.join(processed_path, 'metro_van_admin.gpkg'))

filtered_parks_buff = filtered_parks_buff.set_crs(epsg=3005, allow_override=True)
filtered_parks_buff = filtered_parks_buff.to_crs(epsg=4326)
near_parks = near_parks.to_crs(epsg=4326)

near_parks['access_rate'] = near_parks['access_rate'].round(2) 

south, west = 48.8, -123.9
north, east = 49.7, -121.9

m = folium.Map(
    (49.2057, -122.9110), 
    zoom_start=10,
    min_zoom=10,
    max_zoom=13,
    max_bounds=True,
    min_lat=south,
    max_lat=north,
    min_lon=west,
    max_lon=east,
    zoom_control=True,
    tiles="cartodb positron"
)

choropleth = folium.Choropleth(
    geo_data=near_parks,
    data=near_parks,
    name='Dissemination Areas',
    columns=['DGUID', 'access_rate'],
    key_on='feature.properties.DGUID',
    fill_color='Greens',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Access Rate to Parks',
    highlight=True
).add_to(m)

folium.features.GeoJsonTooltip(
    fields=['DGUID', 'access_rate', 'municipality'],
    aliases=['DGUID', 'Park Access Rate:', 'Municipality:'],
    style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
).add_to(choropleth.geojson)

folium.GeoJson(
    filtered_parks_buff, 
    name="400m Park Buffer",
    show = False,
    style_function=lambda feature: {
        "fillColor": "red",
        "color": "red",
        "weight": 1
        }
).add_to(m)

folium.GeoJson(
    admin_boundaries, 
    name="Administrative Boundaries",
    show = False,
    style_function=lambda feature: {
        "fillColor": "orange",
        "color": "orange",
        "weight": 1
        }
).add_to(m)

folium.LayerControl().add_to(m)

m.save(os.path.join(figures_path, "map.html"))