# import pandas lib as pd
import pandas as pd
import xml.etree.ElementTree as ET

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


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


# Step 5 -- Function to develop a report and send an email 
print('Function to develop a report and send an email')
print(buildStatus)
msg = MIMEMultipart()
msg['From'] = "giri.vakati@gmail.com"
msg['To'] = "venkateswarluec@gmail.com" 
msg['Subject'] = "Build status" 
body = """Hi Team, Please find the build status 
Build is {}"""
msg.attach(MIMEText(body, 'plain'))
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() # for security
s.login("giri.vakati@gmail.com", "atrtxgutxyaxnuxv") 
text = msg.as_string() 
# sending the mail 
s.sendmail("giri.vakati@gmail.com", "venkateswarluec@gmail.com" , text.format(buildStatus))
s.quit()
print('EMAIL sent')
