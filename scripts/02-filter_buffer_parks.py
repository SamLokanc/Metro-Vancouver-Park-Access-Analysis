import os
import pandas as pd
import geopandas as gpd
from src.load_boundaries import load_boundaries

in_path = os.path.join('data', 'raw')
out_path = os.path.join('data', 'processed')
os.makedirs(out_path, exist_ok=True)

vancity_parks_path = os.path.join(in_path, 'vancouver_parks.zip')
metro_van_parks_path = os.path.join(in_path, 'metro_van_parks.zip')
burnaby_parks_path = os.path.join(in_path, 'burnaby_parks.zip')
coquitlam_parks_path = os.path.join(in_path, 'coquitlam_parks.zip')
surrey_parks_path = os.path.join(in_path, 'surrey_parks.geojson')
bowen_island_parks_path = os.path.join(in_path, 'bowen_island_parks.zip')
langley_city_parks_path = os.path.join(in_path, 'langley_city_parks.zip')
langley_township_parks_path = os.path.join(in_path, 'langley_township_parks.zip')
maple_ridge_parks_path = os.path.join(in_path, 'maple_ridge_parks.zip')
north_van_district_parks_path = os.path.join(in_path, 'north_van_district_parks.zip')
port_coquitlam_parks_path = os.path.join(in_path, 'port_coquitlam_parks.zip')
port_moody_parks_path = os.path.join(in_path, 'port_moody_parks.zip')
west_van_parks_path = os.path.join(in_path, 'west_van_parks.zip')
metro_van_admin_path = os.path.join(in_path, 'administrative_boundaries.zip')

vancity_parks_gdf = load_boundaries(vancity_parks_path, 'PARK_NAME')
metro_van_parks_gdf = load_boundaries(metro_van_parks_path, 'parkname')
burnaby_parks_gdf = load_boundaries(burnaby_parks_path, 'NAME', query='`CLASSIFICA` == "MAJ" or `CLASSIFICA` == "DIS" or `CLASSIFICA` == "NEI"')
coquitlam_parks_gdf = load_boundaries(coquitlam_parks_path, 'PARKNAME', query='`PARKTYPE` == "Civic Facility Grounds" or `PARKTYPE` == "Parks and Natural Areas"')
surrey_parks_gdf = load_boundaries(surrey_parks_path, 'PARK_NAME')
bowen_island_parks_gdf = load_boundaries(bowen_island_parks_path, 'NAME', query='`IUCN_DES` == "Park"')
langley_city_parks_gdf = load_boundaries(langley_city_parks_path, 'NAME')
langley_township_parks_gdf = load_boundaries(langley_township_parks_path, 'ParkName', query='`ParkStatus`=="Complete"')
maple_ridge_parks_gdf = load_boundaries(maple_ridge_parks_path, 'ParkName')
north_van_district_parks_gdf = load_boundaries(north_van_district_parks_path, 'PARK_NAME')
port_coquitlam_parks_gdf = load_boundaries(port_coquitlam_parks_path, 'Park_Name')
port_moody_parks_gdf = load_boundaries(port_moody_parks_path, 'park_name')
west_van_parks_gdf = load_boundaries(west_van_parks_path, 'PARK_NAME')

all_parks_gdf = pd.concat([vancity_parks_gdf,
                           metro_van_parks_gdf, 
                           burnaby_parks_gdf,
                           coquitlam_parks_gdf,
                           surrey_parks_gdf,
                           bowen_island_parks_gdf,
                           langley_city_parks_gdf,
                           langley_township_parks_gdf,
                           maple_ridge_parks_gdf,
                           north_van_district_parks_gdf,
                           port_coquitlam_parks_gdf,
                           port_moody_parks_gdf,
                           west_van_parks_gdf], ignore_index=True)

metro_van_admin_gdf = load_boundaries(metro_van_admin_path, 'FullName', 'municipality')

metro_van_admin_gdf = (metro_van_admin_gdf[metro_van_admin_gdf['municipality']
                       .isin([
                           'City of Coquitlam', 
                           'City of Vancouver', 
                           'City of Burnaby',
                           'City of Surrey',
                           'Bowen Island Municipality',
                           'City of Langley',
                           'Township of Langley',
                           'City of Maple Ridge',
                           'District of North Vancouver',
                           'City of Port Coquitlam',
                           'City of Port Moody',
                           'District of West Vancouver'
                           ])]
)

metro_van_admin_gdf.to_file(os.path.join(out_path, "metro_van_admin.gpkg"), driver="GPKG")

filtered_parks_gdf = (
    gpd.sjoin(
    all_parks_gdf,
    metro_van_admin_gdf,
    how='inner',
    predicate='within')
    .drop_duplicates(subset=['park'])
    .drop(columns=['index_right'])
)

buff_dist_meters = 400

filtered_parks_buff = filtered_parks_gdf.buffer(buff_dist_meters).union_all()
filtered_parks_buff_gdf = gpd.GeoDataFrame({'geometry':[filtered_parks_buff]}, crs="EPSG:26910")
filtered_parks_buff_gdf

filtered_parks_buff_gdf.to_file(os.path.join(out_path, "filtered_parks_buff.gpkg"), driver="GPKG")