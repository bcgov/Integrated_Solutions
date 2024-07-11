import os, logging

#Set logging level (NOTSET,DEBUG,INFO,WARNING,ERROR,CRITICAL)
logging_level = logging.INFO

import configuration_and_functions as conf

agol_connection = conf.connect_to_agol()
s3_connection = conf.connect_to_s3()

print(agol_connection)