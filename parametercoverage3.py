# import pandas lib as pd
import pandas as pd
import xml.etree.ElementTree as ET

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def convertXMLtoDataFrame():
    print("convertXMLtoDataFrame")
    prstree = ET.parse('config.xml')
    root = prstree.getroot()

    store_items = []
    all_items = []
    for storeno in root.find('POOL').findall('Parameter'):  
        obj=storeno.attrib.get('obj')
        no= storeno.find('No').attrib.get('Nsp')
        res= storeno.find('Responsible').text
        store_items = [obj,no,res]
        all_items.append(store_items)
  
    xmlToDf = pd.DataFrame(all_items,columns=['Object','Number','Responsible'])        
    return xmlToDf;

xmlToDf= convertXMLtoDataFrame()

# Step 3 -- Function to find the Parameter in the xml data frame
print('Function to find the Parameter in the xml data frame')
def findParameterFromXMLDataFrame(xmlToDf, searchString):
    print(xmlToDf[xmlToDf['Object'].str.contains(searchString)])

searchString='RTDB_GP_ESWITCH_OUTPUTS_E'
findParameterFromXMLDataFrame(xmlToDf,searchString)
