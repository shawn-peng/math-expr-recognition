import os
import time

import requests
from pyquery import PyQuery as pq
folder = "./backslash/"
if not os.path.exists(folder):
    os.mkdir(folder)

_id = 949
# trainingset
tab = "trainingset"
page = 1
download_url = "http://www.martin-thoma.de/write-math"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

i = 0
while 1:
    url = "http://www.martin-thoma.de/write-math/symbol?id=%s&tab=%s&page=%s"%(_id, tab, page)
    d = pq(url=url)

    t = d(".thumb img")
    if len(t) < 1:
        break

    for ele in t:
        img_src = d(ele).attr("src")
        d_url = download_url + img_src[2:]
        print d_url
        r = requests.get(d_url, headers=headers)
        time.sleep(1.2)
        with open(folder+str(i)+".svg", 'wb') as f:
            f.write(r.text)
        i += 1
    print page
    page += 1
