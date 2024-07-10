import os, logging

#Set logging level (NOTSET,DEBUG,INFO,WARNING,ERROR,CRITICAL)
logging_level = logging.INFO

print("Hello World")

import configuration_and_functions as conf

agol_connection = conf.connect_to_agol()

print(agol_connection)