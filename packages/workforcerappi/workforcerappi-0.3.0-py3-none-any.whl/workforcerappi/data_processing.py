import pandas as pd
from .dbconn import *
from .fetch_data import *
# from wfm_functions import *
import logging
import pandas as pd
from .dbconn import snowflake_connection
from .fetch_data import fetch_orders_data

def read_and_sort_orders(date_range=None, file_path=None):
    """
    Read and sort orders data either from a database using a specified date range or from a parquet file.

    Args:
    - date_range (str, optional): A string representing the date range in "YYYY-MM-DD,YYYY-MM-DD" format.
    - file_path (str, optional): Path to the parquet file containing orders data.

    Returns:
    - pd.DataFrame: A DataFrame containing the sorted orders data.

    Raises:
    - ValueError: If neither date_range nor file_path is provided.
    """
    logging.info("read_and_sort_orders called with date_range=%s, file_path=%s", date_range, file_path)
    # If date_range is provided, fetch data from the database
    if date_range is not None:
        logging.info("Fetching data from the database")
        try:
            conn = snowflake_connection()
            df = fetch_orders_data(conn, date_range=date_range, gmv=True, interval=True)
        except Exception as e:
            logging.error("Error fetching data from the database: %s", e)
            raise
    elif file_path is not None:
        # If file_path is provided, read data from the parquet file
        df = pd.read_parquet(file_path)
    else:
        # If neither date_range nor file_path is provided, raise an error
        raise ValueError("Either date_range or file_path must be provided")

    # Sort the DataFrame by date, interval, and country
    logging.info("Sorting the DataFrame")
    df_ordered = df.sort_values(by=["FECHA", "INTERVALO", "COUNTRY"])
    return df_ordered

import pandas as pd

def preprocess_special_dates(date_range=None, file_path_sp=None):
    """
    Read a CSV file containing special dates and preprocess the dates.

    Args:
    - file_path (str): Path to the file.

    Returns:
    - list: A list of special dates.
    """
    if date_range is not None:
        # If date_range is provided, fetch data from the database
        conn = snowflake_connection()
        special = fetch_special_days(conn,date_range=date_range)
        special.rename(columns={'DATE':'Fecha','EVENT':'FERIADO','COUNTRY':'PAIS','TIER_OPS':'Criticidad'}, inplace=True)
        special=special.filter(['PAIS', 'FERIADO', 'Fecha', 'Criticidad'])
        special['Fecha'] = pd.to_datetime(special['Fecha'], format='%d/%m/%Y').dt.date
        special = special[special["PAIS"].isin(["CO","MX"])]
        special = special[special["Criticidad"] == "TIER_1"]
        special_days = special["Fecha"].to_list()

    elif file_path_sp is not None:
        # If file_path_sp is provided, read data from the parquet file
        special = pd.read_csv(file_path_sp)
        special=special.filter(['PAIS', 'FERIADO', 'Fecha', 'Criticidad'])
        special['Fecha'] = pd.to_datetime(special['Fecha'], format='%d/%m/%Y').dt.date
        special = special[special["PAIS"].isin(["CO","MX"])]
        special = special[special["Criticidad"] == "Alto"]
        special_days = special["Fecha"].to_list()
    
    else:
        # If neither date_range nor file_path is provided, raise an error
        raise ValueError("Either date_range or file_path must be provided")
    
    return special_days
    
    

def filter_special_dates(df, special_days):
    """
    Filter out special dates from a DataFrame.

    Args:
    - df (pd.DataFrame): Input DataFrame containing orders data.
    - special_days (list): List of special dates to be filtered out.

    Returns:
    - pd.DataFrame: Filtered DataFrame.
    """
    df_filtered = df[~df['FECHA'].isin(special_days)]
    df_filtered.reset_index(drop=True, inplace=True)
    return df_filtered


def pivot_orders(df, REGION=None):
    """
    Pivot orders data to get total orders per country per date.

    Args:
    - df (pd.DataFrame): Input DataFrame containing orders data.

    Returns:
    - pd.DataFrame: Pivot table with total orders per country per date.
    """
    if REGION=="SS":
        ordersxregion = pd.pivot_table(df, values='ORDERS', index=['FECHA', 'INTERVALO'], columns=['COUNTRY'], aggfunc='sum')
        ordersxregion = ordersxregion.fillna(0)
        ordersxregion['SS'] = ordersxregion.drop(columns=['BR']).sum(axis=1)
        ordersxregion['BR'] = ordersxregion['BR']
        ordersxregion = ordersxregion.filter(['CO', 'MX', 'EC', 'PE', 'CL', 'AR', 'UY', 'CR', 'BR', 'SS'])
        orders = ordersxregion[["SS", "BR"]].reset_index()
        orders = orders[["FECHA", "SS", "BR"]].groupby(["FECHA"]).sum()
        orders.reset_index(inplace=True)
    
    elif REGION == "BR":
        ordersxregion = pd.pivot_table(df, values='ORDERS', index=['FECHA', 'INTERVALO'], columns=['COUNTRY'], aggfunc='sum')
        ordersxregion = ordersxregion.fillna(0)
        ordersxregion['BR'] = ordersxregion['BR']
        ordersxregion = ordersxregion.filter(['BR'])
        orders = ordersxregion[["BR"]].reset_index()
        orders = orders[["FECHA", "BR"]].groupby(["FECHA"]).sum()
        orders.reset_index(inplace=True)
    else:
        raise ValueError("Either SS or BR must be provided")
    return orders


def create_features(df):
    """
    Create time series features based on the DataFrame index.

    Args:
    - df (pd.DataFrame): Input DataFrame containing orders data.

    Returns:
    - pd.DataFrame: DataFrame with additional time series features.
    """
    df = df.copy()
    df['dayofweek'] = df.index.dayofweek
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofyear'] = df.index.dayofyear
    df['dayofmonth'] = df.index.day
    df['weekofyear'] = df.index.isocalendar().week
    return df

def split_train_test_data(data, startdate):
    """
    Split data into train and test sets based on a start date.

    Args:
    - data (pd.DataFrame): Input DataFrame containing orders data.
    - startdate (str): Start date for the test set in "YYYY-MM-DD" format.

    Returns:
    - tuple: A tuple containing the train and test DataFrames.
    """
    data.index = pd.to_datetime(data.index)
    train = data.loc[data.index < startdate]
    test = data.loc[data.index >= startdate]
    return train, test

def create_future_predictions(model, FEATURES, start_for_pred, end_for_pred, frequency):
    idx = pd.date_range(start=start_for_pred, end=end_for_pred, freq=frequency)
    future_data = pd.DataFrame(index=idx)
    future_data = create_features(future_data)
    future_predictions = model.predict(future_data[FEATURES])
    future_data['prediction'] = future_predictions
    month_to_predict = future_data["prediction"]

    return month_to_predict

def read_cr_aht(date_range=None, file_path=None):
    """
    Read and sort orders data either from a database using a specified date range or from a parquet file.

    Args:
    - date_range (str, optional): A string representing the date range in "YYYY-MM-DD,YYYY-MM-DD" format.
    - file_path (str, optional): Path to the parquet file containing orders data.

    Returns:
    - pd.DataFrame: A DataFrame containing the sorted orders data.

    Raises:
    - ValueError: If neither date_range nor file_path is provided.
    """
    if date_range is not None:
        # If date_range is provided, fetch data from the database
        conn = snowflake_connection()
        df = get_cr_aht(conn, date_range=date_range, interval=True)
    elif file_path is not None:
        # If file_path is provided, read data from the parquet file
        df = pd.read_parquet(file_path)
    else:
        # If neither date_range nor file_path is provided, raise an error
        raise ValueError("Either date_range or file_path must be provided")

    # Sort the DataFrame by date, interval, and country
    # df_ordered = df.sort_values(by=["FECHA", "INTERVALO", "COUNTRY"])
    return df
