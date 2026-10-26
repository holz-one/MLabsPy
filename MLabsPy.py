import pandas as pd

def remove_units(series):
    """Removes non-numeric and non-decimal characters and converts to numeric."""
    series = series.astype(str)
    series = series.str.replace(r'[^0-9\.]+', '', regex=True)
    series = pd.to_numeric(series, errors='coerce')
    return series

def new_df(df1, df2):
    """Rejoins the dataframe parts after cleaning."""
    return pd.concat([df1, df2], axis=1)

def rc_col(df):
    """Returns the Record Time column."""
    return df['Record Time']

def unit_clean(df):
    """Removes the Record Time col and cleans the units from the data."""
    return df.drop(columns='Record Time').apply(remove_units)

def fix_MLabs_logfile(df):
    """Cleans a DataFrame loaded from a Motion Labs log format."""
    df_rc = rc_col(df)
    df_fix = unit_clean(df)
    return new_df(df_rc, df_fix)

def load_ml_log(file, s=2):
    """Loads logfile with pandas."""
    return pd.read_csv(file, sep=';', skiprows=s).drop(columns='Unnamed: 45', errors='ignore')

def clean_load(file):
    """Loads and cleans a log file."""
    df = load_ml_log(file)
    df.columns = df.columns.str.strip()
    return fix_MLabs_logfile(df)
