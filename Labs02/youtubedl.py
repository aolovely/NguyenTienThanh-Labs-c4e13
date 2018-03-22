# cai thu vien pip install youtube-dl
from youtube_dl import YoutubeDL
# tai 1 video
# dl = YoutubeDL()
# dl.download(["https://www.youtube.com/watch?v=nHK0u40Ompc"])
#
# # tai nhieu video
# dl = YoutubeDL()
# dl.download(["https://www.youtube.com/watch?v=nHK0u40Ompc", "https://www.youtube.com/watch?v=jpKC2PbfUKU"])
#  # tai tep am thanh

# options = {
#     "format" : "bestaudio / audio"
# }
# dl = YoutubeDL(options)
# dl.download(["https://www.youtube.com/watch?v=nHK0u40Ompc"])

#tim kiem va tai video dau tien
# options = {
#     "default_search": "ytsearch", # tell downloader để tìm kiếm thay vì tải trực tiếp
#     "max_downloads" : 1  # Nói với người downloader chỉ tải về mục nhập đầu tiên (video)
# }
# dl = YoutubeDL (options)
# dl.download (["ngan nain"])
#tim kiem tai am thanh dau tien
options = {
    "default_search": "ytsearch",
    "max_downloads" : 1,
    "format" : "bestaudio / audio"
}
dl = YoutubeDL (options)
dl.download (["ngam hoa le roi"])
