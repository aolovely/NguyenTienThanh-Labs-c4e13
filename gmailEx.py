from gmail import GMail, Message
from random import choice
import datetime
gmail = GMail("lolhyvl@gmail.com","khuelovely")

htmlTemplate = """
<h2>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span style="color: #ff00ff;"> &nbsp; &nbsp;<strong>Đơn Xin Nghỉ Học</strong></span></h2>
<p><span style="color: #0000ff;"><strong>Em ch&agrave;o thầy</strong></span></p>
<p><span style="color: #0000ff;"><strong>Em t&ecirc;n l&agrave;: <span style="color: #ff0000;"><em>Nguyễn Tiến Th&agrave;nh</em></span></strong></span></p>
<p><span style="color: #0000ff;"><strong>H&ocirc;m nay {{sickness}} em xin thầy cho em nghỉ 1 buổi.</strong></span></p>
<p><span style="color: #0000ff;"><strong></strong></span></p>
"""
reasons = ["đau bụng", "ốm","BUỒN NGỦ"]
reason = choice(reasons)
htmlContent = htmlTemplate.replace("{{sickness}}", reason)
msg = Message("hello",to="nguyentienthanh3010@gmail.com", html = htmlContent)

while True:
    now = datetime.datetime.now()
    if now.hour == 7:
        gmail.send(msg)
        break
