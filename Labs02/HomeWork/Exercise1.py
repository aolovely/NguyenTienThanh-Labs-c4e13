from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

#part1:
url = "https://www.apple.com/itunes/charts/songs/"
html = urlopen(url).read().decode("utf8")
soup = BeautifulSoup(html, "html.parser")
section = soup.find("section", "section chart-grid")

li_list = section.find_all("li")
datas = []

for li in li_list:
    data = {}
    data["songs"] = li.h3.a.string
    data["artists"] = li.h4.a.string
    datas.append(data)

pyexcel.save_as(records=datas, dest_file_name="fileitunes.xlsx")

#part2:

options = {
    "default_search": "ytsearch",
    "format" : "bestaudio / audio"
}
dl = YoutubeDL (options)

for data in datas:
    dl.download([data["songs"] + data["artists"]])
