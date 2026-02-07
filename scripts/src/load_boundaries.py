import geopandas as gpd
from shapely import make_valid

def load_boundaries(file_path, name_col, new_name='park', geom_col='geometry', query=None) -> gpd.GeoDataFrame:
    """
    Loads data from downloaded boundary files to a geo dataframe

    Accepts the path to a zip file as the input. Will automatically rename
    the id column so that the output formats match. Optional querys can be 
    supplied to allow for easy filtering.
    
    Parameters
    ----------
    file_path : str
        path to zipfile containing the boundary data
    name_col: str
        name of identifier column in bouindary data
    new_name: str
        new name of identifier, defaults to "park"
    geom_col: str
        name of geometry column in boundary data, defaults to "geometry"
    query: str
        query statement to apply to boundary data, defaults to None

    Returns
    -------
    gpd.GeoDataFrame:
        GeoDataFrame containing the queried identifier and geometry

    Examples
    --------
    vancity_parks_gdf = load_boundaries(vancity_parks_path, 'PARK_NAME')
    """
    
    try:
        gdf = gpd.read_file(file_path)
    except Exception as e:
        raise IOError(f"Could not read boundary file: {file_path}") from e

    if query is not None:
        try:
            gdf = gdf.query(query)
        except Exception as e:
            raise ValueError(f"Invalid query: {query}") from e

    missing = {name_col, geom_col} - set(gdf.columns)
    if missing:
        raise ValueError(
            f"Missing required columns: {missing}. "
            f"Available columns: {list(gdf.columns)}"
        )

    gdf = (
        gdf[[name_col, geom_col]]
        .to_crs("EPSG:26910")
        .rename(columns={name_col: new_name})
        .dropna()
        .drop_duplicates(subset=[geom_col])
    )

    gdf["geometry"] = gdf.geometry.apply(make_valid)

    return gdf