import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import random

## plot graph
df = False

view_data = ['Cols', 'Shape', 'Discribe']

#    removes the un needed units, they will be added when i plot
def remove_units(series):
    # Convert the series to string type
    series = series.astype(str)
    # Replace all non-numeric and non-decimal characters with an empty string
    series = series.str.replace('[^0-9\.]+', '', regex=True)
    # Convert the string series to a numeric series
    series = pd.to_numeric(series, errors='coerce')
    return series


# rejoin the data after cleaning

def new_df(df1, df2):
    return pd.concat([df1, df2], axis=1)

    
# used with widgets, load file and run commands
def data_describe():
    global df
    return df.describe()

def data_shape():
    global df
    return df.shape

def data_cols():
    global df
    return df.columns



def graph_types():
    return [ 'line', 'hist', 'bar', 'barh', 'box', 'kde', 'density', 'area', 'pie', 'scatter', 'hexbin' ]
    

def pplot(new, x, color='', title="Plot some data", plot='line'):    
    figsize=(18, 10)
    # Visuals
    if plot == 'line':      # line plot (default)
        return new.plot.line(x=x, color=color, title=title, figsize=figsize)
    elif plot == 'hist':    # histogram
        return new.plot.hist(x=x, color=color, title=title, alpha=0.7, figsize=figsize)
    elif plot == 'bar':     # ‘bar’ : vertical bar plot
        return new.plot.bar(x=x, color=color, title=title, figsize=figsize)
    elif plot == 'barh':    # ‘barh’ : horizontal bar plot
        return new.plot.barh(x=x, color=color, title=title, figsize=figsize)
    elif plot == 'box':     # ‘box’ : boxplot
        return new.plot.box(by=x,  title=title, figsize=figsize)
    elif plot == 'kde':     # ‘kde’ : Kernel Density Estimation plot
        return new.plot.kde(x=x, color=color, title=title, figsize=figsize)
    elif plot == 'density': # ‘density’ : same as ‘kde’
        return new.plot.density(x=x, color=color, title=title, figsize=figsize)
    elif plot == 'area':    # ‘area’ : area plot
        return new.plot.area(x=x, color=color, title=title, figsize=figsize)
    elif plot == 'pie':     # ‘pie’ : pie plot
        return new.plot.pie(x=x, color=color, title=title, figsize=figsize)
    elif plot == 'scatter': # ‘scatter’ : scatter plot (DataFrame only)
        return new.plot.scatter(x=x, color=color, title=title, figsize=figsize)
    elif plot == 'hexbin':  # ‘hexbin’ : hexbin plot (DataFrame only)],
        return new.plot.hexbin(x=x, color=color, title=title, figsize=figsize)

def view_pd_data(data):
    if data == 'Cols':
        print("#Data Columns: \n")
        return data_cols()
        
    elif data == 'Shape':
        print("#View Data Shape: \n")
        return data_shape()
        
    elif data == 'Discribe':
        print("#View Data Discription: \n")
        return data_describe()

def clean_load(file):
    print(file)
    df = load_ml_log(file)
    df.columns = df.columns.str.strip()
    return fix_MLabs_logfile(df)


def set_file(file):
    global df
    df = clean_load(file)


# assumes that there is a 'Record Time' col in the DataFrame, this is one of the fields in the Motions Labs log format
def fix_MLabs_logfile(df):
    df_rc = rc_col(df)
    df_fix = unit_clean(df)
    return new_df(df_rc, df_fix)


# load logfile
def load_ml_log(file, s=2):
    return pd.read_csv(file, sep=';',skiprows=s).drop(columns='Unnamed: 45')


# return the record time col
def rc_col(df):
    return df['Record Time']


# remove the Record Time col and clean the units from the data
def unit_clean(df):
    return df.drop(columns='Record Time').apply(remove_units)


def get_color(ptype='v120'):
    global color
    if ptype in color:
        return color[ptype]
    else:
        return color['v120']



def get_title(ptype):
    global title
    if ptype in title:
        return title[ptype]
    else:
        return title['v120']

def plot_data(ptype='v120', plot='line'):
    # Data Select
    global new
    return pplot(new[ptype], 'Record Time', get_color(ptype), get_title(ptype), plot)
