# import os
# import requests
# from urllib.parse import urljoin
# from bs4 import BeautifulSoup
#
##DOWNLOADING PDF FILE FROM SINGLE URL

import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = "http://cercind.gov.in/recent_orders_rops2014.html"

#If there is no such folder, the script will create one automatically
folder_location = "D:/KrtrimaIQ/test"
if not os.path.exists(folder_location):os.mkdir(folder_location)
print("created")
response = requests.get(url)
soup= BeautifulSoup(response.text, "html.parser")     
for link in soup.select("a[href$='.pdf']"):
    #Name the pdf files using the last portion of each link which are unique in this case
    filename = os.path.join(folder_location,link['href'].split('/')[-1])
    print(filename)
    with open(filename, 'wb') as f:
        print("in porcess")
        f.write(requests.get(urljoin(url,link['href'])).content)
