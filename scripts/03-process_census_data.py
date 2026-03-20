import os
import zipfile
import pandas as pd
import geopandas as gpd

raw_path = os.path.join('data', 'raw')
processed_path = os.path.join('data', 'processed')

census_path = os.path.join(raw_path, 'census.zip')
csv_name = '98-401-X2021006_English_CSV_data_BritishColumbia.csv'

characteristic_ids = {
    1, # Population 2021
    6, # Population density per square kilometre

    8, # Total - Age groups of the population - 100% data
    9, # 0 to 14 years -> divide by total age for % children
    24, # 65 years and over -> divide by total age for % senior

    41, # Total - Occupied private dwellings by structural type of dwelling - 100% data
    42, # Single-detached house
    43, # Semi-detached house
    44, # Row house
    45, # Apartment or flat in a duplex
    46, # Apartment in a building that has fewer than five storeys
    47, # Apartment in a building that has five or more storeys
    48, # Other single-attached house
    49, # Movable dwelling (4) -> can get % for all of the above

    350, # Total - LICO low-income status in 2020 for the population -> NEED TO CONVERT TO PERCENTAGE (/ population)
    
    1683, # Total - Visible minority for the population in private households - 25% sample data (117)
    1684, # Total visible minority population (118) -> divide this by last to get percent visible minority

    1529, # Immigrants (81)
    1534, # Immigrants from 2011 to 2021 (82) -> divide this by last to get % recent immigrant

    1414, # Total - Private households by tenure - 25% sample data (50)
    1415, # Owner 
    1416, # Renter -> divide this by last to get % renter
}

usecols = [
    "DGUID",
    "GEO_LEVEL",
    "CHARACTERISTIC_ID",
    "CHARACTERISTIC_NAME",
    "C1_COUNT_TOTAL",
]

dtypes = {
    "DGUID": "string",
    "GEO_LEVEL": "category",
    "CHARACTERISTIC_ID": "int32",
    "C1_COUNT_TOTAL": "float32",
}

with zipfile.ZipFile(census_path) as z:
    with z.open(csv_name) as f:
        census_df = (
            pd.read_csv(f, 
                        usecols=usecols, 
                        dtype=dtypes, 
                        encoding='ISO-8859-1')
                        .query('`GEO_LEVEL` == "Dissemination area" & `CHARACTERISTIC_ID` in @characteristic_ids')
        )

census_pivot_df = (
    census_df
    .pivot(columns = "CHARACTERISTIC_ID", 
           values = "C1_COUNT_TOTAL",
           index = 'DGUID')
)

da_boundary_path = os.path.join('data', 'raw', 'DA_boundaries.zip')

census_da_geo_gdf = (
    gpd.read_file(da_boundary_path,
                  columns=['DGUID', 
                           'geometry'])
).to_crs("EPSG:3005")

census_da_gdf = (
    census_da_geo_gdf
    .join(census_pivot_df,
          on=['DGUID'],
          how='inner')
    .rename(columns={
        1:"total_population",
        6:"population_density",

        8:"total_age_groups",
        9:"age_0_to_14",
        24:"age_65+",

        41:"total_occupied_private_dwellings",
        42:"single_detached_house",
        43:"semi_detached_house",
        44:"row_house",
        45:"apartment_or_flat_in_duplex",
        46:"apartment_in_building_less_than_five_storeys",
        47:"apartment_in_building_five_or_more_storeys",
        48:"other_single_attached_house",
        49:"movable_dwelling",

        350:"total_lico",

        1414:"total_private_households_by_tenure",
        1415:"owner",
        1416:"renter",

        1529:"total_immigrants",
        1534:"immigrants_from_2011_to_2021",

        1683:"total_minority_and_non_minority",
        1684:"visible_minority"
    })
)
census_da_gdf['children_pct'] = census_da_gdf["age_0_to_14"] / census_da_gdf["total_age_groups"]
census_da_gdf['senior_pct'] = census_da_gdf["age_65+"] / census_da_gdf["total_age_groups"]

census_da_gdf['attached_house'] = census_da_gdf["semi_detached_house"] + census_da_gdf['row_house'] + census_da_gdf["other_single_attached_house"]
census_da_gdf['apartment'] = census_da_gdf["apartment_or_flat_in_duplex"] + census_da_gdf["apartment_in_building_less_than_five_storeys"] + census_da_gdf["apartment_in_building_five_or_more_storeys"]

census_da_gdf['single_detached_house_pct'] = census_da_gdf["single_detached_house"] / census_da_gdf["total_occupied_private_dwellings"]
census_da_gdf['attached_house_pct'] = census_da_gdf["attached_house"] / census_da_gdf["total_occupied_private_dwellings"]
census_da_gdf['apartment_pct'] = census_da_gdf["apartment"] / census_da_gdf["total_occupied_private_dwellings"]
census_da_gdf['movable_dwelling pct'] = census_da_gdf["movable_dwelling"] / census_da_gdf["total_occupied_private_dwellings"]

census_da_gdf['lico_pct'] =  census_da_gdf['total_lico'] / census_da_gdf['total_population']

census_da_gdf['renter_pct'] = census_da_gdf['renter'] / census_da_gdf["total_private_households_by_tenure"]
census_da_gdf['owner_pct'] = census_da_gdf['owner'] / census_da_gdf["total_private_households_by_tenure"]

census_da_gdf['recent_immigrants_pct'] = census_da_gdf["immigrants_from_2011_to_2021"] / census_da_gdf["total_immigrants"]

census_da_gdf['visible_minority_pct'] = census_da_gdf["visible_minority"] / census_da_gdf["total_minority_and_non_minority"]

census_da_gdf = census_da_gdf.drop(columns=["total_age_groups",
                                            "age_0_to_14",
                                            "age_65+",
                                            "total_occupied_private_dwellings",
                                            "single_detached_house",
                                            "semi_detached_house",
                                            "row_house",
                                            "apartment_or_flat_in_duplex",
                                            "apartment_in_building_less_than_five_storeys",
                                            "apartment_in_building_five_or_more_storeys",
                                            "other_single_attached_house",
                                            "movable_dwelling",
                                            "attached_house",
                                            "apartment",
                                            'total_lico',
                                            "total_private_households_by_tenure",
                                            'renter',
                                            'owner',
                                            'total_immigrants',
                                            'immigrants_from_2011_to_2021',
                                            'visible_minority',
                                            "total_minority_and_non_minority"])

metro_van_admin_gdf = gpd.read_file(os.path.join(processed_path, 'metro_van_admin.gpkg'))

metro_van_census_da_gdf = gpd.sjoin(
    census_da_gdf,
    metro_van_admin_gdf.dissolve(),
    how="inner",
    predicate="within"
)

metro_van_census_da_gdf['centroid'] = metro_van_census_da_gdf.geometry.centroid

centroids_gdf = metro_van_census_da_gdf.copy()
centroids_gdf = centroids_gdf.set_geometry('centroid')

centroids_gdf = centroids_gdf.drop(columns=['index_right'], errors='ignore')

da_with_municipality = gpd.sjoin(
    centroids_gdf.drop(columns=['municipality'], errors='ignore'),
    metro_van_admin_gdf[['geometry', 'municipality']],
    how="left",
    predicate="within"
)

metro_van_census_da_gdf['municipality'] = da_with_municipality['municipality']

filtered_parks_buff_gdf = gpd.read_file(os.path.join(processed_path, 'filtered_parks_buff.gpkg'))
park_buff_geom = filtered_parks_buff_gdf.geometry.iloc[0]

metro_van_census_da_gdf["access_rate"] = (
    metro_van_census_da_gdf.geometry.intersection(park_buff_geom).area
    / metro_van_census_da_gdf.geometry.area
)

(metro_van_census_da_gdf
 .drop(columns=['geometry', 'centroid', 'index_right'])
 .to_csv(os.path.join(processed_path, 'near_parks.csv'))
)

(metro_van_census_da_gdf
 .drop(columns=['centroid', 'index_right'], errors='ignore')
 .to_file(
    os.path.join(processed_path, 'near_parks.gpkg'), driver="GPKG")
)