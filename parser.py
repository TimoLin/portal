import json
import base64
from urllib.request import urlopen


subs = [
        #"https://iwxf.netlify.app",
        #"https://raw.githubusercontent.com/freefq/free/master/v2",
        #"https://raw.githubusercontent.com/ssrsub/ssr/master/ss-sub"
        #"https://raw.githubusercontent.com/ssrsub/ssr/master/V2Ray"
        #"https://raw.githubusercontent.com/vveg26/GetNode/master/Eternity"
        #"https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/Eternity"
        #"https://ghproxy.com//raw.githubusercontent.com/yaney01/Yaney01/main/yaney_01"
        "https://raw.githubusercontent.com/mfuu/v2ray/master/v2ray"
        ]

def str2Bas64(link):
    return base64.urlsafe_b64encode(link.encode('utf-8')).decode()

def main():
    nodeLinks = ''
    for subLink in subs:
        fetchContent = urlopen(subLink).read()
        fetchLinks = base64.b64decode(fetchContent).decode('utf-8')
        nodeLinks += fetchLinks

    content = str2Bas64(nodeLinks)
    
    with open("index.html",'w') as f:
        f.write(content)

    # Return node numbers
    print (len(nodeLinks.splitlines()))

if __name__ == "__main__":
    main()
