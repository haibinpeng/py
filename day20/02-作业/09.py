# 作者: Michael(phb)
# 2022年06月23日22时36分00秒
import re
s = """
http://www.interoem.com/messageinfo.asp?id=35`
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
"""
ret = re.findall(r'//[a-zA-Z0-9.-]*/', s)
for i in ret:
    ret_s = re.sub(r'/+', '', i)
    print(ret_s)
