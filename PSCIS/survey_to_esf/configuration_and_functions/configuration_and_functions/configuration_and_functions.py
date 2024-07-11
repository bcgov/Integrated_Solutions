# Import Modules

import sys,os
import os, json, datetime
from arcgis.gis import GIS
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile
from datetime import datetime
import time
from minio import Minio

# %% Logging
import logging
SaveLogsTo = 'Logging'
#Setup logging - levels are DEBUG,INFO,WARNING,ERROR,CRITICAL
logging.basicConfig(level=logging.DEBUG)

agol_username = os.environ["AGO_USER"]
agol_password = os.environ["AGO_PASS"]
agol_url = os.environ["AGO_PORTAL_URL"]

s3_root = os.environ["PSCIS_S3_ROOT"]
#photo_dir = r'W:\srm\sry\Local\projlib\PSCIS\data\proj_packages'
endpoint = os.environ["PSCIS_S3_ENDPOINT"]
access_id = os.environ["PSCIS_S3_ACCESSID"]
secret = os.environ["PSCIS_S3_SECRET"]
bucket = os.environ["PSCIS_S3_BUCKET"]


def connect_to_agol():
    """
    Returns GIS Object. First step for working with ArcGIS API for Python.
    """
    start_time = time.time()
    print(agol_url)
    try:
        gis = GIS(agol_url, agol_username, agol_password, verify_cert=False)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Successfully Connected, Elapsed Time:")
        print(elapsed_time)
        return gis
    except:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Elapsed Time:")
        print(elapsed_time)
        print("Could not Make a Connection to ArcGIS Online")


def connect_to_s3():
    '''
    Create connection to S3 Object Storage
    
            Parameters:
                    env_variable_endpoint (str): REST endpoint for S3 storage
                    env_variable_id (str): Access key ID
                    env_variable_key (str): Secret access key

            Returns:
                    S3Connection (obj): Minio connection to S3 Object Storage bucket
    '''
    logging.info("Creating connection to S3 Object Storage...")
    S3Connection = Minio(endpoint,access_id,secret)
    logging.info("Connection to S3 Object Storage created successfully")
    return(S3Connection)


