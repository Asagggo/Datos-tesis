#Cargamos las librerias necesarias
import os
from cif import cif
import pandas as pd
import re
import datetime
import warnings
from IPython.display import Image

#Seleccionamos el país de interés
productivity= cif.createDataFrameFromOECD(countries = ['USA'], dsname = 'PDB_GR')
print (productivity)

