#1. Download wed page
from urllib.request import urlopen
html = urlopen("http://dantri.com.vn/").read().decode('utf-8')
print(html)
# luu trang html vua tai ve may
import urllib.request
urllib.request.urlretrieve("http://dantri.com.vn/", "test1.html")
#2. Extract ROI(Region of interest)

#3. Extract info
