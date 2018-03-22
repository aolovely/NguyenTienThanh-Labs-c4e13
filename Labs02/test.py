from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "http://dantri.com.vn/"
# #1.1 open web page
# conn =  urlopen(url)
#
# #1.2 read
# data = conn.read()
# print(data)
# #1.3 decode chuyen ve dinh dang UTF-8
# html = data.decode("utf8")
html = urlopen("http://dantri.com.vn").read().decode("utf8")
#
# print(html)
#
# #save html5
# htmlFile = open("dantri.com", "wb")
# htmlFile.write(html)
# htmlFile.close()


#2.ROI
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify()) #lam cho hien thi nhin dep hon vs ham prettify()
ul = soup.find("ul", "ul1 ulnew") #tim the ul co class ul1 ulnew
# print(ul.prettify())

#3.Extract info
li_list = ul.find_all("li")
# for li in li_list:
#     print(li.prettify())
#     print("*" * 30)

li = li_list[0]
# h4 = li.find("h4") # ~ h4 = li.h4
# a = h4.find("a") # a = h4.a
datas =[]
for li in li_list:
    data = {}
    a = li.h4.a
    # print(a)
    # print(a.string)
    # print(url + a["href"])
    data["title"] = a.string
    data["links"] = url + a["href"]
    datas.append(data)
pyexcel.save_as(records=datas, dest_file_name="test13.xlsx")
