# import pandas lib as pd
import pandas as pd
import xml.etree.ElementTree as ET

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# Step 4-- Function to pass or fail the build depending on the previous step 

print('Function to pass or fail the build depending on the previous step')
def findParameterFromXMLDataFrame(xmlToDf, searchString):
    return xmlToDf[xmlToDf['Object'].str.contains(searchString)]
    
searchString='RTDB_GP_ESWITCH_OUTPUTS_E1'
resultDataFrame=findParameterFromXMLDataFrame(xmlToDf,searchString)
print(resultDataFrame.size)
buildStatus=''
if resultDataFrame.size>0:
    buildStatus='PASS'
    print('PASS')
else:
    buildStatus='FAIL'
    print('FAIL')
