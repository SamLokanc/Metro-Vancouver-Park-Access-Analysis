from src.download_url import download_url

download_files = {
    'vancouver_parks.zip': ("https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/par"
                            "ks-polygon-representation/exports/shp?lang=en&timezone=America%2FLo"
                            "s_Angeles&use_labels=true"),
    'metro_van_parks.zip': ("https://stg-arcgisazurecdataprod6.az.arcgis.com/exportfiles-86184-4" 
                            "88/RegionalParksBoundaries_OpenData_4384382056109619585.zip?sv=2025" 
                            "-05-05&st=2026-02-07T22%3A56%3A50Z&se=2026-02-08T00%3A01%3A50Z&sr=c" 
                            "&sp=r&sig=DrlJBz3kNGYXDsu%2BAnyZ3wWFocNL6nVeqrF6QaTasRE%3D"),
    'burnaby_parks.zip': ("https://hub.arcgis.com/api/v3/datasets/a1a896a4209d4325bacacea417ffc4" 
                          "00_6/downloads/data?format=shp&spatialRefId=26910&where=1%3D1"),
    'coquitlam_parks.zip': ("https://stg-arcgisazurecdataprod2.az.arcgis.com/exportfiles-9198-32" 
                            "63/Parks%20Recreation%20and%20Culture_6851935831780887332.zip?sv=20" 
                            "25-05-05&st=2026-02-07T23%3A02%3A31Z&se=2026-02-08T00%3A07%3A31Z&sr" 
                            "=c&sp=r&sig=mFep8XVMQRZp0pJE%2FYi907hv15JBfK7VA9tJ1yr1NHQ%3D"),
    'surrey_parks.zip': ("https://stg-arcgisazurecdataprod5.az.arcgis.com/exportfiles-32735-4963" 
                         "/Park%20Locations_-1122571421545015697.zip?sv=2025-05-05&st=2026-02-07" 
                         "T23%3A06%3A38Z&se=2026-02-08T00%3A11%3A38Z&sr=c&sp=r&sig=kFeiFUiZa1Ndq" 
                         "fpXYIecTRz8nRj%2FI4yRw%2Fqqp1F4kzg%3D"),
    'bowen_island_parks.zip': ("https://islandstrust.bc.ca/DATA/BM/Shapefile/BM_PROTECTED_AREAS." 
                               "ZIP"),
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
    'port_coquitlam_parks.zip': ("https://stg-arcgisazurecdataprod9.az.arcgis.com/exportfiles-56" 
                                 "866-32/Parks_5959397222314580324.zip?sv=2025-05-05&st=2026-02-" 
                                 "07T23%3A28%3A16Z&se=2026-02-08T00%3A33%3A16Z&sr=c&sp=r&sig=p7P" 
                                 "uP00fQ0a%2Bv1o7rIUSgeN59AalIF8s%2Fb%2FEMjtmSU4%3D"),
    'port_moody_parks.zip':("https://hub.arcgis.com/api/v3/datasets/e4b3e90da06645ab8db11eb7c79" 
                            "7b939_105/downloads/data?format=shp&spatialRefId=26910&where=park_"
                            "type <> 'Future Parks'"),
    'west_van_parks.zip': ("https://mapping.westvancouver.ca/PRODUCTS/OPEN/PARKS/PARKS_SHP.ZIP"), 
    'administrative_boundaries.zip' : ("https://services6.arcgis.com/56eqCzQ5SZhBaDST/arcgis/r" 
                                       "est/services/Administrative_Boundaries/FeatureServer/r" 
                                       "eplicafilescache/Administrative_Boundaries_-6445306865" 
                                       "161621642.zip"),
    'census.zip' : ("https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/do" 
                    "wnload-telecharger/comp/GetFile.cfm?Lang=E&FILETYPE=CSV&GEONO=006_BC_CB")
}

for filename, url in download_files.items():        
    download_url(url=url, filename=filename)