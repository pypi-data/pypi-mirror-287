from abc import ABC, abstractmethod

import pandas as pd
import xarray as xr
import numpy as np
import subprocess
import os 

from .aux_funcs import *

def ERA5_ts(self, save_csv = False, save_nc=False):
    """
    Extract times series of  the nearest gird point (lon,lat) from
    ERA5 reanalysis and save it as netcdf.
    """
    filename = download_era5_from_cds(self.start_time, self.end_time, self.lon, self.lat,self.variable, folder='cache')
    ds = xr.open_mfdataset(filename)
    df = create_dataframe(product=self.product,ds=ds, lon_near=ds.longitude.values[0], lat_near=ds.latitude.values[0], outfile=self.datafile, variable=self.variable, start_time = self.start_time, end_time = self.end_time, save_csv=save_csv, height=self.height)
    
    return df

def GTSM_ts(self, save_csv=False, save_nc=False):
    """
    Extract times series of the nearest grid point (lon, lat) from
    GTSM water level and save it as netcdf.
    """
    filenames = download_gtsm_from_cds(self.start_time, self.end_time, self.lon, self.lat, self.variable, folder='cache')

    if not isinstance(filenames, list):
        filenames = [filenames]

    all_nc_files = []
    for filename in filenames:
        temppath = os.path.dirname(filename)
        # Unpack the tar.gz file.
        nc_files = subprocess.run(['tar', '-ztf', filename], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')[0:-1]
        nc_files = sorted([ff.strip('\r') for ff in nc_files])
        subprocess.run(['tar', '-xzvf', filename, '--directory', temppath], stdout=subprocess.PIPE) # Extract tar file
        all_nc_files.extend([os.path.join(temppath, file) for file in nc_files])

    # Open multiple netCDF files as a single xarray dataset
    ds = xr.open_mfdataset(all_nc_files)
    # Calculate the distance to each station
    distances = np.sqrt((ds.station_x_coordinate - self.lon)**2 + (ds.station_y_coordinate - self.lat)**2)
    # Find the index of the nearest station
    nearest_station_index = distances.argmin().values
    # Extract the data for the nearest station
    ds = ds.isel(stations=nearest_station_index)
    df = create_dataframe(product=self.product, ds=ds, lon_near=ds.stations.station_x_coordinate.values, lat_near=ds.stations.station_y_coordinate.values, outfile=self.datafile, variable=self.variable, start_time=self.start_time, end_time=self.end_time, save_csv=save_csv, height=self.height)

    return df


def download_era5_from_cds(start_time, end_time, lon, lat, variable,  folder='cache') -> str:
    import cdsapi
    """Downloads ERA5 data from the Copernicus Climate Data Store for a
    given point and time period"""
    start_time = pd.Timestamp(start_time)
    end_time = pd.Timestamp(end_time)
    c = cdsapi.Client()


    # Create directory
    try:
        # Create target Directory
        os.mkdir(folder)
        print("Directory " , folder ,  " Created ")
    except FileExistsError:
        print("Directory " , folder ,  " already exists")

    days = get_date_list('ERA5',start_time, end_time)
    # Create string for dates
    dates = [days[0].strftime('%Y-%m-%d'), days[-1].strftime('%Y-%m-%d')]
    dates = '/'.join(dates)
    filename_list = []
    for i in range(len(variable)):
        filename = f'{folder}/ERA5_'+"lon"+str(lon)+"lat"+str(lat)+"_"+days[0].strftime('%Y%m%d')+'_'+days[-1].strftime('%Y%m%d')+'_'+variable[i]+".nc"
        filename_list = np.append(filename_list,filename)
        cds_command = {
            'product_type': 'reanalysis',
            'format': 'netcdf',
            'variable': variable[i],
            'date': dates,
            'time': [
                '00:00', '01:00', '02:00',
                '03:00', '04:00', '05:00',
                '06:00', '07:00', '08:00',
                '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00',
                '15:00', '16:00', '17:00',
                '18:00', '19:00', '20:00',
                '21:00', '22:00', '23:00',
            ],
            'area': [
                lat+0.001, lon-0.001, lat-0.001,lon+0.001,
                #53.33, 1.31, 53.31,1.33,
            ],
        }
        print('Download variable('+str(i+1)+'/'+str(len(variable)) +')' +':'+variable[i] ) 
        c.retrieve('reanalysis-era5-single-levels', cds_command, filename)
    return filename


def download_gtsm_from_cds(start_time, end_time, lon, lat, variable,  folder='cache') -> str:
    import cdsapi
    """Downloads GTSM model water level data from the Copernicus Climate Data Store for a
    given point and time period"""
    filename = []
    filename_list = []
    start_time = pd.Timestamp(start_time)
    end_time = pd.Timestamp(end_time)
    c = cdsapi.Client()

    days = get_date_list('ERA5',start_time, end_time)
    years = days.year
    years = years.unique()
    years = [str(year) for year in years]

    months = days.month
    months = months.unique()
    months = [f'{month:02}'  for month in months]
    
    # Create directory
    try:
        # Create target Directory
        os.mkdir(folder)
        print("Directory " , folder ,  " Created ")
    except FileExistsError:
        print("Directory " , folder ,  " already exists")

    for year in years:
        for var in variable:
            if var == 'tidal_elevation':
                experiment = 'historical'
            else:
                experiment = 'reanalysis'
            filename = f'{folder}/EC_GTSM_ERA5_{var}_{year}.tar.gz'
            cds_command = {
                'experiment': experiment,
                'format': 'tgz',
                'variable': var,
                'year': year, # 1950-2013
                'month': months,
                'temporal_aggregation' : '10_min',
                #'model': 'CMCC-CM2-VHR4',
            
            }
            print(f'Download variable:',var, year)
            c.retrieve('sis-water-level-change-timeseries-cmip6', cds_command, filename)
            filename_list.append(filename)          
    return filename_list

