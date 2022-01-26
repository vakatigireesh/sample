# import pandas lib as pd
import pandas as pd
import xml.etree.ElementTree as ET

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# read by default 1st sheet of an excel file
#dataframe1 = pd.read_excel('individualparametercoverage.xlsx')
#dateframe2 = dataframe1.parse('Sheet1', skiprows=4, index_col=None, na_values=['NA'])
#Step 1
xls = pd.ExcelFile('individualparametercoverage.xlsx')

df = xls.parse('Sheet1', skiprows=5,usecols="B,C", index_col=None, na_values=['NA'])
print(df)
