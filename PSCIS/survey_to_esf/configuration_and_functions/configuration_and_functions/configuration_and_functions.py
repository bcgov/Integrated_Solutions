# Import Modules

import sys,os
import os, json, datetime
from arcgis.gis import GIS
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile
from datetime import datetime
import time

agol_username = os.environ["AGO_USER"]
agol_password = os.environ["AGO_PASS"]
agol_url = os.environ["AGO_PORTAL_URL"]


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