import re
import urllib.request

f = urllib.request.urlopen("file:///home/savera/regex assignment/sample-example.html")
text=f.read()
text=text.decode()
appointmentreference = re.findall(r"([A-Z]{2}\d{8}-\d{5})",text)
patientname = re.findall(r">([A-Za-z]{3,}\s[A-Za-z]{3,})",text)
patientaddress = re.findall(r"(\w{1,}\s*\w{1,}\s\w{1,},\s)?(\w{1,}\s)?(\w{1,},\s)?(\w(1,)\s)?(\w{1,}\s)?(\w{1,}\s)?(\w{1,}\s\w{1,},\s)?\w{1,},\s*(\s*|\w{1,})\s\w{1,},\s\w{1,},.\d{5}",text)
patientphone = re.findall(r"\(\d{3}\)\s\d{3}-\d{4}",text)
agentname = re.findall(r">([A-Za-z]{3,}\s[A-Za-z]{3,}|N\/A)",text)
status = re.findall(r"(COMPLETED|CONFIRMED|AVAILABLE)",text)
tracking = re.findall(r"(>\s\d{5,}|n\/a)",text)
dateandtime = re.findall(r"(\d{2}\s[a-zA-Z]{3}\s\d{4}\s\d{2}:\d{2}\s[A-Z]{2})",text)

file = open('tabledata.txt','w')
data = " "
for i in range(34):
    print(i)
    data = appointmentreference[i] + " " + patientname[i] + " " + patientphone[i] + " " + agentname[i] + " " + status[i] + " " +  tracking[i] + " " + dateandtime[i] + "\n"
    file.write(data)
    data = " "
file.close()
