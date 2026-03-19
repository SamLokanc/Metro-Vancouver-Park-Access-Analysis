from src.download_url import download_url

download_files = {
    'vancouver_parks.zip': ("https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/par"
                            "ks-polygon-representation/exports/shp?lang=en&timezone=America%2FLo"
                            "s_Angeles&use_labels=true"),
    'metro_van_parks.zip': ("https://services6.arcgis.com/56eqCzQ5SZhBaDST/arcgis/rest/services/" 
                            "RegionalParksBoundaries_OpenData/FeatureServer/replicafilescache/Re" 
                            "gionalParksBoundaries_OpenData_4384382056109619585.zip"),
    'burnaby_parks.zip': ("https://hub.arcgis.com/api/v3/datasets/a1a896a4209d4325bacacea417ffc4" 
                          "00_6/downloads/data?format=shp&spatialRefId=26910&where=1%3D1"),
    'coquitlam_parks.zip': ("https://services2.arcgis.com/Q6Lq3evZUGfPrN7o/arcgis/rest/services/" 
                            "Parks%20Recreation%20and%20Culture/FeatureServer/replicafilescache/" 
                            "Parks%20Recreation%20and%20Culture_6851935831780887332.zip"),
    'surrey_parks.geojson': ("https://services5.arcgis.com/YRpe0VKTJytZSSIB/arcgis/rest/services" 
                             "/Park%20Locations/FeatureServer/replicafilescache/Park%20Locations" 
                             "_2731771217122842592.geojson"),
    'langley_city_parks.zip': ("https://hub.arcgis.com/api/v3/datasets/c4c1e34f0552400f853e7424b" 
                               "29f32a6_187/downloads/data?format=shp&spatialRefId=26910&where=1" 
                               "%3D1"),
    'langley_township_parks.zip': ("https://hub.arcgis.com/api/v3/datasets/93ae11e4d5f240ccad638" 
                                   "7154ce8f685_0/downloads/data?format=shp&spatialRefId=26910&w" 
                                   "here=1%3D1"),
    'maple_ridge_parks.zip': ("https://hub.arcgis.com/api/v3/datasets/d26dbc17c18f4a199ce667d441" 
                              "786149_4/downloads/data?format=shp&spatialRefId=26910&where=ParkN" 
                              "ame+IS+NOT+NULL"),
    'north_van_district_parks.zip': ("https://geoweb.dnv.org/Products/Data/SHP/PrkPark_shp.zip"),
    'port_coquitlam_parks.zip': ("https://services9.arcgis.com/nz97KciUs5nOw64q/arcgis/rest/se" 
                                 "rvices/Parks/FeatureServer/replicafilescache/Parks_595939722" 
                                 "2314580324.zip"),
    'port_moody_parks.zip':("https://hub.arcgis.com/api/v3/datasets/e4b3e90da06645ab8db11eb7c79" 
                            "7b939_105/downloads/data?format=shp&spatialRefId=26910&where=park_"
                            "type <> 'Future Parks'"),
    'administrative_boundaries.zip' : ("https://services6.arcgis.com/56eqCzQ5SZhBaDST/arcgis/r" 
                                       "est/services/Administrative_Boundaries/FeatureServer/r" 
                                       "eplicafilescache/Administrative_Boundaries_-6445306865" 
                                       "161621642.zip"),
    'census.zip' : ("https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/do" 
                    "wnload-telecharger/comp/GetFile.cfm?Lang=E&FILETYPE=CSV&GEONO=006_BC_CB"),
    'DA_boundaries.zip' : ("https://www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/bo" 
                           "undary-limites/files-fichiers/lda_000b21a_e.zip")
}

for filename, url in download_files.items():        
    download_url(url=url, filename=filename)