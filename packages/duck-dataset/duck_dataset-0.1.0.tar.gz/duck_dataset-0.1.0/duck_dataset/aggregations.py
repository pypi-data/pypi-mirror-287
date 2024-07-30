from typing import List

import rioxarray
import duckdb


def spatial(resolution: int, db_path: str, function_name: str, limit: int | None = None, columns: str | List[str] = 'mean', long_format: bool = False):
    """
    Perform a spatial aggregation for the given dataset.

    This function executes a spatial aggregation query on a DuckDB database and returns the result either as a pandas DataFrame or a rioxarray Dataset.

    Parameters:
    resolution (int): The resolution for the spatial aggregation.
    db_path (str): The path to the DuckDB database file.
    function_name (str): The name of the function to perform the aggregation.
    limit (int, optional): The maximum number of rows to return. Defaults to None.
    columns (str or List[str], optional): The columns to include in the aggregation. Defaults to 'mean'.
    long_format (bool, optional): Whether to return the result in long format (pandas DataFrame) or wide format (rioxarray Dataset). Defaults to False.

    Returns:
    pandas.DataFrame or rioxarray.Dataset: The result of the spatial aggregation. If long_format is True, a pandas DataFrame is returned. Otherwise, a rioxarray Dataset is returned.
    """
    # make columns a list
    if isinstance(columns, str):
        columns = [columns]

    # build the query
    sql = f"SELECT y, x, {','.join(columns)} FROM {function_name}({resolution})"
    if limit is not None:
        sql += f" LIMIT {limit}"
    sql += ";"

    # execute the query
    with duckdb.connect(db_path, read_only=True) as duck:
        duck.install_extension('spatial')
        duck.load_extension('spatial')
        df = duck.execute(sql).df()
    
    if long_format:
        return df
    
    # otherwise transform to a rioxarray dataset
    ds = df.set_index(['y', 'x']).to_xarray()
    ds.rio.write_crs(3857, inplace=True)

    return ds


def temporal(precision: str, db_path: str, function_name: str, limit: int | None = None, columns: str | List[str] = 'mean'):
    """
    Perform a temporal aggregation for the given dataset.

    This function executes a temporal aggregation query on a DuckDB database and returns the result as a pandas DataFrame.

    Parameters:
    precision (str): The precision for the temporal aggregation (e.g., 'day', 'month', 'year').
    db_path (str): The path to the DuckDB database file.
    function_name (str): The name of the function to perform the aggregation.
    limit (int, optional): The maximum number of rows to return. Defaults to None.
    columns (str or List[str], optional): The columns to include in the aggregation. Defaults to 'mean'.

    Returns:
    pandas.DataFrame: The result of the temporal aggregation.
    """
    # make columns a list
    if isinstance(columns, str):
        columns = [columns]
    
    # build the query
    sql = f"SELECT time, {','.join(columns)} FROM {function_name}('{precision}')"
    if limit is not None:
        sql += f" LIMIT {limit}"
    sql += ";"

    # execute the query
    with duckdb.connect(db_path, read_only=True) as duck:
        return duck.execute(sql).df()


def spatiotemporal(precision: str, resolution: int, db_path: str, function_name: str, limit: int | None = None, columns: str | List[str] = 'mean', long_format: bool = False):
    """
    Perform a spatiotemporal aggregation for the given dataset.

    This function executes a spatiotemporal aggregation query on a DuckDB database and returns the result either as a pandas DataFrame or a rioxarray Dataset.

    Parameters:
    resolution (int): The resolution for the spatial aggregation.
    precision (str): The precision for the temporal aggregation (e.g., 'day', 'month', 'year').
    db_path (str): The path to the DuckDB database file.
    function_name (str): The name of the function to perform the aggregation.
    limit (int, optional): The maximum number of rows to return. Defaults to None.
    columns (str or List[str], optional): The columns to include in the aggregation. Defaults to 'mean'.
    long_format (bool, optional): Whether to return the result in long format (pandas DataFrame) or wide format (rioxarray Dataset). Defaults to False.

    Returns:
    pandas.DataFrame or rioxarray.Dataset: The result of the spatiotemporal aggregation. If long_format is True, a pandas DataFrame is returned. Otherwise, a rioxarray Dataset is returned.
    """
    # make columns a list
    if isinstance(columns, str):
        columns = [columns]
    
    # build the query
    sql = f"SELECT time, y, x, {','.join(columns)} FROM {function_name}({resolution}, '{precision}')"
    if limit is not None:
        sql += f" LIMIT {limit}"
    sql += ";"

    # execute the query
    with duckdb.connect(db_path, read_only=True) as duck:
        duck.install_extension('spatial')
        duck.load_extension('spatial')
        df = duck.execute(sql).df()
    
    if long_format:
        return df

    # otherwise transform to a rioxarray dataset
    ds = df.set_index(['y', 'x', 'time']).to_xarray()
    ds.rio.write_crs(3857, inplace=True)

    return ds
