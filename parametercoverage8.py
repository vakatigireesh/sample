# import pandas lib as pd
import pandas as pd
import xml.etree.ElementTree as ET

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


#Step 8 -- Function compare average parameter data frame to excel data frame 
print('#Step 8 -- Function compare average parameter data frame to excel data frame')

    
#Step 9 -- Function to pass or fail the build depending on the previous step 
print('#Step 9 -- Function to pass or fail the build depending on the previous step')
buildStatus=''
if resultDataFrame.size>0:
    buildStatus='PASS'
    print('PASS')
else:
    buildStatus='FAIL'
    print('FAIL')
    
