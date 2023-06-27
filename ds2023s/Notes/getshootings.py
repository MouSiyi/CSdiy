#A complete version of lec4-danmu
import urllib.request
import json
import zlib
import xml.dom.minidom



#封装得到bv号步骤
def get_bv_from_url(url):
    urlsplitted = url.split('/')
    halfbv=None
    for w in urlsplitted:
        if 'BV' in w:
            halfbv=w
    if halfbv==None:
        raise Exception("这个url里没得bv号qwq")
    if '?' in halfbv:
        qmark=halfbv.find("?")
        bv=halfbv[:qmark]
        return bv
    else:
        bv=halfbv
        return bv


#封装得到cid步骤
def get_cid_from_bv(bv):
    api="https://api.bilibili.com/x/web-interface/view?bvid="
    url=api+bv
    #获取该视频信息的接口地址
    response=urllib.request.urlopen(url)
    string=response.read()
    html=string.decode("utf-8")
    doc=json.loads(html)
    cid=doc["data"]["cid"]
    return cid

#封装得到弹幕的xml形式步骤
def get_xml_from_cid(cid):
    api = "https://api.bilibili.com/x/v1/dm/list.so?oid="
    url = api + str(cid)
    response = urllib.request.urlopen(url)
    response.getheader("Content-Encoding")
    string = response.read()
    html = zlib.decompress(string, wbits=-zlib.MAX_WBITS).decode('utf-8')
    xml2 = xml.dom.minidom.parseString(html)
    xml_pretty_str = xml2.toprettyxml()
    return xml_pretty_str

def filter_line(line):
    if line.startswith("\t<d"):
        return True
    else:
        return False


def clean_line(line):
    start=line.find('">')
    end=line.find("</d>")
    shootings=line[start+2:end]
    return shootings
    
url1 = "https://www.bilibili.com/video/BV1nL411x7jH"
url2 = "https://www.bilibili.com/video/BV1nL411x7jH?from=search&seid=13994942816196159115&spm_id_from=333.337.0.0"
url3 = "https://www.bilibili.com/video/BV1nL411x7jH/?spm_id_from=333.788"
url4 = "https://www.bilibili.com/video/av463010182"
#url形式可能性

bv=get_bv_from_url(url1)
cid=get_cid_from_bv(bv)
xml_pretty_str=get_xml_from_cid(cid)
lines=xml_pretty_str.split("\n")
it=filter(filter_line,lines)
shootings=map(clean_line,it)
print(list(shootings))




