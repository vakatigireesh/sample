# import pandas lib as pd
import pandas as pd
import xml.etree.ElementTree as ET

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



#Step 6 -- Function to convert dev.txt to data frame 
print('#Step 6 -- Function to convert dev.txt to data frame')

#dfTextFile = pd.read_csv('Psm_coverage_psm_dev.txt', memory_map=True, header=None)
dfTextFile = pd.read_fwf('Psm_coverage_psm_dev.txt', memory_map=True, header=None)
print(dfTextFile.info())
for col in dfTextFile:
    print(dfTextFile[col].unique())
