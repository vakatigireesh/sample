# import pandas lib as pd
import pandas as pd
import xml.etree.ElementTree as ET

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# Step 3 -- Function to find the Parameter in the xml data frame
print('Function to find the Parameter in the xml data frame')
def findParameterFromXMLDataFrame(xmlToDf, searchString):
    print(xmlToDf[xmlToDf['Object'].str.contains(searchString)])

searchString='RTDB_GP_ESWITCH_OUTPUTS_E'
findParameterFromXMLDataFrame(xmlToDf,searchString)
